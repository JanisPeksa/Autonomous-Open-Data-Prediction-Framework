from Program.DataHandler import DataHandler
from Program.TimeHandler import TimeHandler
from Program.DataFiller import DataFiller
from Program.MySQLClient import MySQLClient
from Program.Forecasting_Model import Forecasting_Model
from Program.KF import KF_1D
from Program.Cluster import Cluster
from sklearn.metrics import mean_squared_error
from math import sqrt
import datetime


# dates = ["2020-01-19", "2020-02-19", "2020-03-19", "2020-04-19", "2020-05-19", "2020-06-19", "2020-07-19",
#          "2020-08-19", "2020-09-19", "2020-10-19", "2020-11-19", "2020-12-19", "2021-01-19"]


class Test:
    def __init__(self, date_from: str, date_till: str, use_second_data_type: bool):
        self.date_from = date_from
        self.date_till = date_till
        self.use_second_data_type = use_second_data_type

    @staticmethod
    def get_forecast_accuracy_with_real_data(forecast_list, actual_list):
        return sqrt(mean_squared_error(actual_list, forecast_list))

    def make_test(self):
        result_json = {}

        steps = 10
        value = "Dew Point"

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result_json["Test started: "] = current_time
        result_json["Value: "] = value
        result_json["Steps in the future"] = steps
        result_json["Use second data type: "] = self.use_second_data_type

        sql_client = MySQLClient("xxx.xxx.xxx.xxx", "login", "pwd", "dbname")
        station_locations_rec = sql_client.get_latitude_and_longitude()

        datetime_unit_of_measure = "minute"
        period_value = 11

        optimize = True

        time_handler = TimeHandler(datetime_unit_of_measure, period_value, self.date_from, self.date_till)

        for num in range(1, 55):

            station_code = "LV"
            if len(str(num)) == 1:
                station_code += "0" + str(num)
            else:
                station_code += str(num)

            print(station_code)

            station_data = {}

            records = sql_client.get_info_by_station(station_code)

            if not records:
                station_data["Data points: "] = 0
                continue

            list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
            list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

            data_df = time_handler.get_datetime_and_measurements_dataframe(list_of_datetime, list_of_measurements)
            data_df = data_df[~data_df.index.duplicated(keep='first')]

            if data_df.empty:
                station_data["Data points: "] = 0
                continue

            station_data["Data points: "] = len(data_df)

            actual_data_df = time_handler. \
                get_real_data_for_comparing_with_forecast(list_of_datetime, list_of_measurements,
                                                          date_from_for_actual_data=time_handler.date_till,
                                                          steps=steps)

            if data_df.isnull().values.any() or actual_data_df.isnull().values.any():
                station_data["None values: "] = int(data_df.isna().sum()["Measurements"])

                station_clusters_df = Cluster(station_locations_rec).get_stations_clusters_df()

                if data_df.isnull().values.any() or actual_data_df.isnull().values.any():
                    data_df, actual_data_df = DataFiller(data_df, station_clusters_df,
                                                         station_code, time_handler, sql_client,
                                                         station_locations_rec, self.use_second_data_type,
                                                         actual_data_df, steps).fill_data_none_values(value)

                station_data["None values after filling: "] = int(data_df.isna().sum()["Measurements"])
                if data_df.isnull().values.any():
                    continue
            else:
                station_data["None values: "] = 0

            use_kf_values = [False, True]

            result_json[station_code] = station_data

            station_rmse_and_model_results = {}

            # Kalman Filter
            for use_fk in use_kf_values:

                # using Kalman Filter
                if use_fk:
                    filtered_values_list = KF_1D(DataHandler.get_list_of_dataframe_values(data_df.values)).get_filtered_values()

                    data_df["Measurements"] = filtered_values_list

                data_df.sort_index(inplace=True)

                arima_model = Forecasting_Model("ARIMA", data_df, steps, station_code, optimize)
                forecast_arima = arima_model.get_forecast()

                if forecast_arima is not None:
                    arima_rmse = self.get_forecast_accuracy_with_real_data(forecast_arima, actual_data_df.values)
                    arima_model_order = arima_model.best_model_order
                else:
                    arima_rmse = None
                    arima_model_order = None

                if use_fk:
                    station_rmse_and_model_results["With Kalman Filter: "] = {"RMSE: ": arima_rmse,
                                                                              "ARIMA model": arima_model_order}
                else:
                    station_rmse_and_model_results["Without Kalman Filter: "] = {"RMSE: ": arima_rmse,
                                                                                 "ARIMA model": arima_model_order}

                station_data["Forecast results: "] = station_rmse_and_model_results
                result_json[station_code] = station_data

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result_json["Test ended: "] = current_time
        return result_json
