import math
import pandas
from Program.DataHandler import DataHandler
from Program.MySQLClient import MySQLClient
from Program.TimeHandler import TimeHandler
from Program.LVGMC_stations import LVGMS_stations


class DataFiller:

    def __init__(self, data_df, actual_data_df, station_clusters_df, station_code: str, steps: int,
                 time_handler: TimeHandler, sql_client: MySQLClient, station_locations_rec, use_second_data_type=False):

        self.station_code = station_code
        self.steps = steps

        self.sql_client = sql_client
        self.time_handler = time_handler

        self.data_df = data_df
        self.actual_data_df = actual_data_df
        self.station_clusters_df = station_clusters_df

        self.use_second_data_type = use_second_data_type

        if use_second_data_type:
            self.lvgmc_station = LVGMS_stations(station_code, station_locations_rec)

    def get_list_of_stations_codes_to_use(self):
        cluster_position = self.station_clusters_df.loc[self.station_code]["cluster"]
        stations_to_use = self.station_clusters_df[(self.station_clusters_df["cluster"] == cluster_position)
                                                   & (self.station_clusters_df.index != self.station_code)]

        return list(stations_to_use.index)

    def fill_data_none_values(self, value):
        stations_codes_to_use_list = self.get_list_of_stations_codes_to_use()
        df_s = []
        act_df_s = []
        for station_code in stations_codes_to_use_list:
            records = self.sql_client.get_info_by_station(station_code)
            if not records:
                continue

            list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
            list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]
            df = self.time_handler.get_datetime_and_measurements_dataframe(list_of_datetime, list_of_measurements)

            if not df.empty:
                df_s.append(df)

            act_df = self.time_handler. \
                get_real_data_for_comparing_with_forecast(list_of_datetime, list_of_measurements,
                                                          date_from_for_actual_data=self.time_handler.date_till, steps=self.steps)

            if not act_df.empty:
                act_df_s.append(act_df)

        for datetime, measurement in self.data_df[self.data_df["Measurements"].isnull()].iterrows():
            temp_measurement = 0
            i_temp = 0

            for df in df_s:
                temp_datetime = self.time_handler.\
                    get_datetime_from_dataframe_with_delta_limitation(df, datetime, self.time_handler.period_value)

                if temp_datetime != -1:
                    temp_value = df.loc[temp_datetime]["Measurements"]
                    if type(temp_value) == pandas.Series:
                        continue
                    if temp_value is not None and not math.isnan(temp_value):
                        temp_measurement += temp_value
                        i_temp += 1

            if i_temp != 0:
                temp_measurement = temp_measurement / i_temp
                if self.use_second_data_type:
                    self.lvgmc_station.get_lvgmc_station_data()
                    second_data_type_value = self.lvgmc_station.get_second_data_type_value(datetime)
                    if second_data_type_value is not None:
                        temp_measurement = (temp_measurement + second_data_type_value) / 2
                self.data_df.loc[datetime]["Measurements"] = temp_measurement

        for datetime, measurement in self.actual_data_df[self.actual_data_df["Measurements"].isnull()].iterrows():
            temp_measurement = 0
            i_temp = 0
            for act_df in act_df_s:
                temp_datetime = self.time_handler. \
                    get_datetime_from_dataframe_with_delta_limitation(act_df, datetime, self.time_handler.period_value)

                if temp_datetime != -1:
                    temp_value = act_df.loc[temp_datetime]["Measurements"]
                    if type(temp_value) == pandas.Series:
                        continue
                    if temp_value is not None and not math.isnan(temp_value):
                        temp_measurement += temp_value
                        i_temp += 1

            if i_temp != 0:
                temp_measurement = temp_measurement / i_temp
                if self.use_second_data_type:
                    self.lvgmc_station.get_lvgmc_station_data()
                    second_data_type_value = self.lvgmc_station.get_second_data_type_value(datetime)
                    if second_data_type_value is not None:
                        temp_measurement = (temp_measurement + second_data_type_value) / 2
                self.actual_data_df.loc[datetime]["Measurements"] = temp_measurement

        return self.data_df, self.actual_data_df
