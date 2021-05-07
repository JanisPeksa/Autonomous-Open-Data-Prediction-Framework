from Program.DataHandler import DataHandler
from Program.TimeHandler import TimeHandler
from Program.DataFiller import DataFiller
from Program.MySQLClient import MySQLClient
from Program.ForecastingModel import ForecastingModel
from Program.KF import KF_1D
from Program.Cluster import Cluster
from sklearn.metrics import mean_squared_error
from math import sqrt
import os
from matplotlib import pyplot as plt
import datetime
import pandas as pd


# dates = ["2020-01-19", "2020-02-19", "2020-03-19", "2020-04-19", "2020-05-19", "2020-06-19", "2020-07-19",
#          "2020-08-19", "2020-09-19", "2020-10-19", "2020-11-19", "2020-12-19", "2021-01-19"]


class Test:
    def __init__(self, date_from: str, date_till: str, using_second_data_type: bool):
        self.date_from = date_from
        self.date_till = date_till
        self.using_second_data_type = using_second_data_type

    def make_test(self):

        def get_forecast_accuracy_with_real_data(forecast_list, actual_list):
            return sqrt(mean_squared_error(actual_list, forecast_list))

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Test is started {current_time}\n")

        sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'login', 'password', 'dbname')
        station_locations_rec = sql_client.get_latitude_and_longitude()
        value = "Dew Point"

        use_second_data_type = True

        datetime_unit_of_measure = "minute"
        period_value = 11

        steps = 10

        optimize = True

        rmse_results_with_KF = {}
        rmse_results_without_KF = {}

        models_with_KF = {}
        models_without_KF = {}

        time_handler = TimeHandler(self.date_from, self.date_till, datetime_unit_of_measure, period_value)

        for num in range(1, 55):

            station_code = "LV"
            if len(str(num)) == 1:
                station_code += "0" + str(num)
            else:
                station_code += str(num)

            using_Kalman_Filter_values = [True, False]

            for using_Kalman_Filter in using_Kalman_Filter_values:

                # create the folder
                path = "Test_results"

                isFile = os.path.isdir(path)
                if isFile is False:
                    os.mkdir(path)

                path = "Test_results/" + "{}_{}_{}".format(self.date_from, self.date_till, current_time)
                isFile = os.path.isdir(path)
                if isFile is False:
                    os.mkdir(path)

                if os.path.isdir(path + "/Contains_None_values") is False:
                    os.mkdir(path + "/Contains_None_values")

                if os.path.isdir(path + "/Has_no_None_values") is False:
                    os.mkdir(path + "/Has_no_None_values")

                records = sql_client.get_info_by_station(station_code)
                if not records:
                    continue

                list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
                list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

                data_df = time_handler.get_datetime_and_measurements_dataframe(list_of_datetime,
                                                                               list_of_measurements)
                actual_data_df = time_handler. \
                    get_real_data_for_comparing_with_forecast(list_of_datetime, list_of_measurements,
                                                              date_from_for_actual_data=time_handler.date_till,
                                                              steps=steps)

                print(f"Station {station_code}")
                if data_df.empty:
                    print("{} is completely empty\n".format(station_code))
                    continue

                contains_none_values = False

                if data_df.isnull().values.any() or actual_data_df.isnull().values.any():
                    print("{} contains None values".format(station_code))
                    contains_none_values = True

                    isFile = os.path.isdir(path + "/Clustering_results")
                    if isFile is False:
                        os.mkdir(path + "/Clustering_results")

                    station_clusters_df = Cluster(station_locations_rec,
                                                  path_to_save=path + "/Clustering_results").get_stations_clusters_df()

                    if data_df.isnull().values.any() or actual_data_df.isnull().values.any():
                        data_df, actual_data_df = DataFiller(data_df, actual_data_df, station_clusters_df,
                                                             station_code,
                                                             steps, time_handler, sql_client, station_locations_rec,
                                                             use_second_data_type=use_second_data_type).fill_data_none_values(
                            value)

                    print("{} --> None values were filled".format(station_code))
                    if data_df.isnull().values.any():
                        print("{} --> still has some None values\n".format(station_code))
                        continue
                else:
                    print("{} doesn't contain None values".format(station_code))

                # using Kalman Filter
                if using_Kalman_Filter is True:
                    filtered_values_list = KF_1D(
                        DataHandler.get_list_of_dataframe_values(data_df.values)).get_filtered_values()
                    data_df = time_handler.get_datetime_and_measurements_dataframe(list_of_datetime,
                                                                                   list_of_measurements)
                    data_df_values_list = DataHandler.get_list_of_dataframe_values(data_df.values)
                    data_df["Measurements"] = filtered_values_list

                data_df.sort_index(inplace=True)

                if contains_none_values:
                    path += "/Contains_None_values"
                else:
                    path += "/Has_no_None_values"

                # create the folder
                path += "/" + station_code

                isFile = os.path.isdir(path)
                if isFile is False:
                    os.mkdir(path)

                if using_Kalman_Filter is True:
                    path += "/With_KF"
                else:
                    path += "/Without_KF"

                isFile = os.path.isdir(path)
                if isFile is False:
                    os.mkdir(path)

                path += "/"

                bx = plt.gca()
                data_df.plot(color="green", ax=bx)
                plt.title("{} - {}, {} {} points".format(self.date_from, self.date_till, station_code, len(data_df)))
                plt.xlabel("Date and time")
                plt.ylabel("Dew point")
                name = "Data_{}.png".format(station_code)
                plt.savefig(path + name)
                plt.close()

                print("All models for {}".format(station_code))

                arima_model = ForecastingModel("ARIMA", data_df, steps, optimize, station_code, path)
                forecast_arima = arima_model.get_forecast()
                arima_data_points = arima_model.data_points_to_use
                arima_model_order = arima_model.best_model_order
                print("ARIMA - {}".format(arima_model_order))

                arma_model = ForecastingModel("ARMA", data_df, steps, optimize, station_code, path)
                forecast_arma = arma_model.get_forecast()
                arma_data_points = arma_model.data_points_to_use
                arma_model_order = arma_model.best_model_order
                print("ARMA - {}".format(arma_model_order))

                ar_model = ForecastingModel("AR", data_df, steps, optimize, station_code, path)
                forecast_ar = ar_model.get_forecast()
                ar_data_points = ar_model.data_points_to_use
                ar_model_order = ar_model.best_model_order
                print("AR - {}".format(ar_model_order))

                ma_model = ForecastingModel("MA", data_df, steps, optimize, station_code, path)
                forecast_ma = ma_model.get_forecast()
                ma_data_points = ma_model.data_points_to_use
                ma_model_order = ma_model.best_model_order
                print("MA - {}".format(ma_model_order))

                ax = plt.gca()

                filtered_data_for_graph_df = data_df[-(100 + steps):]

                filtered_data_for_graph_df.plot(color="green", ax=ax)
                actual_data_df.plot(color="red", ax=ax)

                plot_legend_result = list()
                plot_legend_result.append("Data 1")
                plot_legend_result.append("Data 2")

                plot_text_result = ""

                if forecast_arima is not None:
                    arima_rmse = get_forecast_accuracy_with_real_data(forecast_arima, actual_data_df.values)
                    forecast_arima_df = DataHandler.duplicate_dataframe_using_real_datafrme(actual_data_df,
                                                                                            forecast_arima)
                    forecast_arima_df.plot(color="blue", ax=ax)
                    arima_results_string = "ARIMA{} RMSE:{:.2f}".format(arima_model_order, arima_rmse)
                    plot_text_result += "ARIMA{} RMSE:{:.2f}, data points used:{}\n".format(arima_model_order,
                                                                                            arima_rmse,
                                                                                            arima_data_points)
                    plot_legend_result.append(arima_results_string)
                else:
                    arima_results_string = "ARIMA model was not defined"
                    plot_text_result += arima_results_string + "\n"
                    arima_rmse = None

                if forecast_arma is not None:
                    arma_rmse = get_forecast_accuracy_with_real_data(forecast_arma, actual_data_df.values)
                    forecast_arma_df = DataHandler.duplicate_dataframe_using_real_datafrme(actual_data_df,
                                                                                           forecast_arma)
                    forecast_arma_df.plot(color="cyan", ax=ax)
                    arma_results_string = "ARMA{} RMSE:{:.2f}".format(arma_model_order, arma_rmse)
                    plot_text_result += "ARMA{} RMSE:{:.2f}, data points used:{}\n".format(arma_model_order,
                                                                                           arma_rmse,
                                                                                           arma_data_points)
                    plot_legend_result.append(arma_results_string)
                else:
                    arma_results_string = "ARMA model was not defined"
                    plot_text_result += arma_results_string + "\n"
                    arma_rmse = None

                if forecast_ar is not None:
                    ar_rmse = get_forecast_accuracy_with_real_data(forecast_ar, actual_data_df.values)
                    forecast_ar_df = DataHandler.duplicate_dataframe_using_real_datafrme(actual_data_df,
                                                                                         forecast_ar)
                    forecast_ar_df.plot(color="black", ax=ax)
                    ar_results_string = "AR{} RMSE:{:.2f}".format(ar_model_order, ar_rmse)
                    plot_text_result += "AR{} RMSE:{:.2f}, data points used:{}\n".format(ar_model_order, ar_rmse,
                                                                                         ar_data_points)
                    plot_legend_result.append(ar_results_string)
                else:
                    ar_results_string = "AR model was not defined"
                    plot_text_result += ar_results_string + "\n"
                    ar_rmse = None

                if forecast_ma is not None:
                    ma_rmse = get_forecast_accuracy_with_real_data(forecast_ma, actual_data_df.values)
                    forecast_ma_df = DataHandler.duplicate_dataframe_using_real_datafrme(actual_data_df,
                                                                                         forecast_ma)
                    forecast_ma_df.plot(color="purple", ax=ax)
                    ma_results_string = "MA{} RMSE:{:.2f}".format(ma_model_order, ma_rmse)
                    plot_text_result += "MA{} RMSE:{:.2f}, data points used:{}\n".format(ma_model_order, ma_rmse,
                                                                                         ma_data_points)
                    plot_legend_result.append(ma_results_string)
                else:
                    ma_results_string = "MA model was not defined"
                    plot_text_result += ma_results_string + "\n"
                    ma_rmse = None

                if using_Kalman_Filter:
                    models_with_KF[station_code] = [arima_model_order, arma_model_order, ar_model_order,
                                                    ma_model_order]
                    rmse_results_with_KF[station_code] = [arima_rmse, arma_rmse, ar_rmse, ma_rmse]
                else:
                    models_without_KF[station_code] = [arima_model_order, arma_model_order, ar_model_order,
                                                       ma_model_order]
                    rmse_results_without_KF[station_code] = [arima_rmse, arma_rmse, ar_rmse, ma_rmse]

                print(plot_text_result + "\n")

                plt.legend(plot_legend_result)

                plt.title("{} - {}, forecast for {} points".format(self.date_from, self.date_till, steps))
                plt.xlabel("Date and time")
                plt.ylabel("Dew point")

                name = "Forecast_{}.png".format(station_code)
                plt.savefig(path + name)
                plt.close()

        results_with_KF_df = pd.DataFrame(rmse_results_with_KF, index=["ARIMA", "ARMA", "AR", "MA"])
        results_without_KF_df = pd.DataFrame(rmse_results_without_KF, index=["ARIMA", "ARMA", "AR", "MA"])
        models_with_KF_df = pd.DataFrame(models_with_KF, index=["ARIMA", "ARMA", "AR", "MA"])
        models_without_KF_df = pd.DataFrame(models_without_KF, index=["ARIMA", "ARMA", "AR", "MA"])

        writer = pd.ExcelWriter("results_{}_{}.xlsx".format(self.date_from, self.date_till), engine='xlsxwriter')
        results_with_KF_df.to_excel(writer, sheet_name='RMSE_with_KF')
        results_without_KF_df.to_excel(writer, sheet_name='RMSE_without_KF')
        models_with_KF_df.to_excel(writer, sheet_name='models_with_KF')
        models_without_KF_df.to_excel(writer, sheet_name='models_without_KF')
        writer.save()

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Test is ended {current_time}")
