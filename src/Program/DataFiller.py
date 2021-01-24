import math
import pandas
from Program.DataHandler import DataHandler
from Program.MySQLClient import MySQLClient
from Program.TimeHandler import TimeHandler


class DataFiller:

    def __init__(self, data_series, station_clusters_df, station_code,
                 time_handler: TimeHandler, sql_client: MySQLClient):

        self.station_code = station_code

        self.sql_client = sql_client
        self.time_handler = time_handler

        self.data_series = data_series
        self.station_clusters_df = station_clusters_df

    def get_list_of_stations_codes_to_use(self):
        cluster_position = self.station_clusters_df.loc[self.station_code]["cluster"]
        stations_to_use = self.station_clusters_df[(self.station_clusters_df["cluster"] == cluster_position)
                                                   & (self.station_clusters_df.index != self.station_code)]

        return list(stations_to_use.index)

    def fill_the_data_none_values(self, value):
        stations_codes_to_use_list = self.get_list_of_stations_codes_to_use()

        series_s = []

        for station_code in stations_codes_to_use_list:
            records = self.sql_client.get_info_by_station(station_code)
            if not records:
                continue

            list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
            list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]
            series = self.time_handler.get_datetime_and_measurements_series(list_of_measurements, list_of_datetime)

            if not series.empty:
                series_s.append(series)

        for datetime, measurement in self.data_series[self.data_series.isnull()].items():
            temp_measurement = 0
            i_temp = 0
            for series in series_s:
                temp_datetime = self.time_handler.\
                    get_datetime_from_dataframe_with_delta_limitation(series, datetime, self.time_handler.period_value)

                if temp_datetime != -1:
                    temp_value = series.loc[temp_datetime]
                    if type(temp_value) == pandas.Series:
                        continue
                    if temp_value is not None and not math.isnan(temp_value):
                        temp_measurement += temp_value
                        i_temp += 1

            if i_temp != 0:
                temp_measurement = temp_measurement / i_temp
                self.data_series.loc[datetime] = temp_measurement

        return self.data_series
