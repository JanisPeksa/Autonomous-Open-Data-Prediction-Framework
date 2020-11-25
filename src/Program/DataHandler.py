import datetime
import pandas as pd
import numpy as np


class DataHandler:

    @staticmethod
    def get_list_of_float_numbers_and_station(list_of_values: list) -> list:
        list_of_data = []

        for value in list_of_values:
            try:
                list_of_data.append(float(value))
            except ValueError:
                list_of_data.append(value)

        return list_of_data

    @staticmethod
    def get_corresponding_list_of_time(data_list: list) -> list:
        list_of_time = []
        temp_list = []
        for list_of_dicts in data_list:
            for data_dict in list_of_dicts:
                temp_list.append(data_dict['Time'])
            else:
                temp_list.append(data_dict['Station'])
            list_of_time.append(temp_list)
            temp_list = []
        return list_of_time

    @staticmethod
    def zip_time_and_values(lists_of_values: list, lists_of_time: list) -> list:
        zipped_list = []
        temp_list1 = []
        temp_list2 = []
        temp_list3 = []
        station_names = []

        for list_of_values in lists_of_values:
            station_names.append(list_of_values[len(list_of_values) - 1])
            list_of_values.pop(len(list_of_values) - 1)
            temp_list1.append(list_of_values)
        else:
            for list_of_time in lists_of_time:
                list_of_time.pop(len(list_of_time) - 1)
                temp_list2.append(list_of_time)

            for value, time, station_name in zip(temp_list1, temp_list2, station_names):
                temp_list3.append(station_name)
                temp_list3.append(value)
                temp_list3.append(time)
                zipped_list.append(temp_list3)
                temp_list3 = []

        return zipped_list

    @staticmethod
    def get_station_names(list_of_lists_of_data: list) -> list:
        list_of_station_names = []

        for list_of_data in list_of_lists_of_data:
            list_of_station_names.append(list_of_data[-1])

        return list_of_station_names

    @staticmethod
    def get_lists_of_chosen_values_with_station_names(lists_of_dicts: list, value_name: str) -> list:
        list_of_values = []
        temp_list = []

        for list_of_dicts in lists_of_dicts:
            for data_dict in list_of_dicts:
                temp_list.append(data_dict[value_name])
            else:
                temp_list.append(data_dict['Station'])
            list_of_values.append(temp_list)
            temp_list = []

        return list_of_values

    @staticmethod
    def get_lists_of_measurements_with_station_names(lists_of_values: list) -> list:
        lists_of_measurements = []

        for list_of_values in lists_of_values:
            if '-' in list_of_values or '' in list_of_values:
                list_of_values.pop()
                if DataHandler.is_possible_to_fill_missing_data(list_of_values):
                    indexes = DataHandler.get_indexes_for_filling(list_of_values)
                    list_of_values = DataHandler.fill_missing_data_in_list(list_of_values, indexes)
                else:
                    continue
            lists_of_measurements.append(DataHandler.get_list_of_float_numbers_and_station(list_of_values))

        return lists_of_measurements

    @staticmethod
    def get_lists_of_measurements_without_station_names(
            list_of_lists_of_measurements_with_station_names: list) -> list:
        list_of_lists_of_measurements_without_station_names = []

        for list_of_measurements in list_of_lists_of_measurements_with_station_names:
            list_of_measurements.pop(len(list_of_measurements) - 1)
            list_of_lists_of_measurements_without_station_names.append(list_of_measurements)

        return list_of_lists_of_measurements_without_station_names

    @staticmethod
    def get_prepared_lists_for_estimation(main_data, value: str = 'Dew Point') -> tuple:
        lists_of_chosen_values = DataHandler.get_lists_of_chosen_values_with_station_names(main_data, value)

        lists_of_measurements_with_station_names = DataHandler.get_lists_of_measurements_with_station_names(
            lists_of_chosen_values)

        list_of_station_names = DataHandler.get_station_names(lists_of_measurements_with_station_names)

        lists_of_measurements_without_station_names = DataHandler.get_lists_of_measurements_without_station_names(
            lists_of_measurements_with_station_names)

        return lists_of_measurements_without_station_names, list_of_station_names

    @staticmethod
    def get_estimation_accuracy(lists_of_estimates: list, lists_of_measurements: list, station_names: list):
        from math import sqrt

        dict_of_accuracy = {}

        number_of_estimations = len(lists_of_measurements)

        for estimates, measurements, station_name in zip(lists_of_estimates, lists_of_measurements, station_names):
            sum_of_differences = 0

            for estimate, measurement in zip(estimates, measurements):
                sum_of_differences += estimate - measurement
            else:
                dict_of_accuracy[station_name] = sqrt((sum_of_differences ** 2) / number_of_estimations)

        return dict_of_accuracy

    @staticmethod
    def get_json_of_chosen_values(lists_of_values):
        json_dict = {}
        temp_list = []

        for list_of_values in lists_of_values:
            for value in list_of_values[0:-2]:
                temp_list.append(value)
            else:
                json_dict[list_of_values[-1]] = temp_list
                temp_list = []

        return json_dict

    @staticmethod
    def get_json_of_existing_values():
        return {'Values': ['Station',
                           'Time',
                           'Air Temperature',
                           'Air Temperature(-1 h)',
                           'Humidity',
                           'Dew Point',
                           'Precipitation',
                           'Intensity',
                           'Visibility',
                           'Road Temperature',
                           'Road Temperature(-1 h)',
                           'Road Condition',
                           'Road Warning',
                           'Freezing Point',
                           'Road Temperature 2',
                           'Road Temperature 2(-1 h)',
                           'Road Condition 2',
                           'Road Warning 2',
                           'Freezing Point 2']}

    @staticmethod
    def get_json_of_station_names():
        return {'Stations': ['A1 km 12 Ādaži',
                             'A1 km 21 Lilaste',
                             'A1 km 39 Skulte',
                             'A1 km 45 Dunte',
                             'A1 km 57 Tūja',
                             'A1 km 71 Vitrupe',
                             'A1 km 9 Ādaži',
                             'A1 km 97 Ainaži',
                             'A2 km 102 Rauna',
                             'A2 km 126 Smiltene',
                             'A2 km 156 Vireši',
                             'A2 km 27 Garkalne',
                             'A2 km 57 Sigulda',
                             'A2 km 76 Melturi',
                             'A3 km 102 Strenči',
                             'A3 km 24 Inciems',
                             'A3 km 41 Stalbe',
                             'A3 km 62 Valmiera',
                             'A4 km 7 Mucenieki',
                             'A5 km 23 Apvedceļš',
                             'A5 km 8 Ķekava',
                             'A6 km 109 Ādmiņi',
                             'A6 km 163 Līvāni',
                             'A6 km 200 Nīcgale',
                             'A6 km 22 Saulkalne',
                             'A6 km 236 Daugavpils',
                             'A6 km 280 Krāslava',
                             'A6 km 63 Kaibala',
                             'A7 km 32 Bērziņi',
                             'A7 km 53 Zariņi',
                             'A7 km 71 Ceraukste',
                             'A7 km 82 Grenctāle',
                             'A8 km 27 Dalbe',
                             'A8 km 43 Vircava',
                             'A8 km 72 Eleja',
                             'A9 km 113 Saldus',
                             'A9 km 13 Lāči',
                             'A9 km 138 Rudbārži',
                             'A9 km 154 Kalvene',
                             'A9 km 178 Durbe',
                             'A9 km 24 Kalnciems',
                             'A9 km 39 Apšupe',
                             'A9 km 62 Annenieki',
                             'A10 km 104 Talsi',
                             'A10 km 138 Usma',
                             'A10 km 169 Pope',
                             'A10 km 17 Jūrmala',
                             'A10 km 36 Sloka',
                             'A10 km 45 Ķemeri',
                             'A10 km 80 Pūre',
                             'A11 km 38 Nīca',
                             'A12 km 155 Zilupe',
                             'A12 km 38 Atašiene',
                             'A12 km 68 Viļāni',
                             'A12 km 96 Rēzekne',
                             'A13 km 11 Kārsava',
                             'A13 km 81 Feimaņi',
                             'P80 km 13 Ogresgals',
                             'P80 km 35 Zādzene']}

    @staticmethod
    def is_missing_data_present(list_of_values: list):
        for x in list_of_values:
            if x is not float:
                return True
        else:
            return False

    @staticmethod
    def is_possible_to_fill_missing_data(list_of_values: list) -> bool:
        index = 0
        adder = 1

        while adder < 5 and index < len(list_of_values) - 1 and index + adder < len(list_of_values):
            if list_of_values[index] == '-' and list_of_values[index + adder] == '-':
                adder += 1
            else:
                index += adder
                adder = 1
        else:
            if '' in list_of_values:
                return False

            if adder > 4:
                return False
            elif 1 < adder < 5 and adder == len(list_of_values):
                return False
            else:
                return True

    @staticmethod
    def get_indexes_for_filling(list_of_values: list) -> tuple:

        index = 0
        adder = 1

        indexes = []

        while adder < 5 and index < len(list_of_values) - 1 and index + adder < len(list_of_values):
            if adder == 1 and list_of_values[index] == '-' and list_of_values[index + 1] != '-':
                indexes.append([index, 'one'])

            if list_of_values[index] == '-' and list_of_values[index + adder] == '-':
                adder += 1
            elif adder != 1:
                indexes.append([index - 1, index + adder, 'normal'])
                index += adder
                adder = 1
            else:
                index += adder
                adder = 1
        else:
            if adder != 1:
                indexes.append([index - 1, index + adder, 'in the end'])

        return tuple(indexes)

    @staticmethod
    def fill_missing_data_in_list(list_of_values: list, indexes: tuple) -> list:
        for index_list in indexes:
            if index_list[-1] == 'normal':
                average = (list_of_values[index_list[0]] + list_of_values[index_list[1]]) / 2

                for i in range(index_list[0] + 1, index_list[1]):
                    list_of_values[i] = average
            elif index_list[-1] == 'one':
                average = (list_of_values[index_list[0] - 1] + list_of_values[index_list[0] + 1]) / 2
                list_of_values[index_list[0]] = average
            elif index_list[-1] == 'in the end':
                for i in range(index_list[0], index_list[1]):
                    list_of_values[i] = list_of_values[index_list[0]]

        return list_of_values

    @staticmethod
    def get_exact_value_from_my_sql_records(records: tuple, index: int) -> list:
        values = []

        for record in records:
            values.append(record[index])

        return values

    @staticmethod
    def get_exact_value_from_many_my_sql_records(list_of_records: list, index: int) -> list:
        values = []

        for records in list_of_records:
            values.append(DataHandler.get_exact_value_from_my_sql_records(records, index))

        return values

    @staticmethod
    def get_index_of_value(value: str = 'Dew Point') -> int:
        if value == 'id':
            return 0
        elif value == 'Station code':
            return 1
        elif value == 'Datetime':
            return 2
        elif value == 'Air Temperature':
            return 3
        elif value == 'Air Temperature(-1 h)':
            return 4
        elif value == 'Humidity':
            return 5
        elif value == 'Dew Point':
            return 6
        elif value == 'Precipitation':
            return 7
        elif value == 'Intensity':
            return 8
        elif value == 'Visibility':
            return 9
        elif value == 'Road Temperature':
            return 10
        elif value == 'Road Temperature(-1 h)':
            return 11
        elif value == 'Road Condition':
            return 12
        elif value == 'Road Warning':
            return 13
        elif value == 'Freezing Point':
            return 14
        elif value == 'Road Temperature 2':
            return 15
        elif value == 'Road Temperature 2(-1 h)':
            return 16
        elif value == 'Road Condition 2':
            return 17
        elif value == 'Road Warning 2':
            return 18
        elif value == 'Freezing Point 2':
            return 19
        else:
            raise Exception

    @staticmethod
    def get_list_of_floats(list_of_values: list) -> list:

        for x in range(len(list_of_values)):
            try:
                list_of_values[x] = float(list_of_values[x])
            except TypeError:
                continue

        return list_of_values

    @staticmethod
    def get_lists_of_floats(lists_of_values: list) -> list:
        __list = []
        for list_of_values in lists_of_values:
            __list.append(DataHandler.get_list_of_floats(list_of_values))

        return __list

    @staticmethod
    def get_date() -> str:
        from datetime import datetime

        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day

        return 'Year: {} Month: {} Day: {}'.format(year, month, day)

    @staticmethod
    def get_data_dicts(data_lists) -> list:
        data_dicts = []

        for data in data_lists:
            data_dict = {'Station': data[0],
                         'Time': data[1],
                         'Date': DataHandler.get_date(),
                         'Air Temperature': data[2],
                         'Air Temperature(-1 h)': data[3],
                         'Humidity': data[4],
                         'Dew Point': data[5],
                         'Precipitation': data[6],
                         'Intensity': data[7],
                         'Visibility': data[8],
                         'Road Temperature': data[9],
                         'Road Temperature(-1 h)': data[10],
                         'Road Condition': data[11],
                         'Road Warning': data[12],
                         'Freezing Point': data[13],
                         'Road Temperature 2': data[14],
                         'Road Temperature 2(-1 h)': data[15],
                         'Road Condition 2': data[16],
                         'Road Warning 2': data[17],
                         'Freezing Point 2': data[18]}
            data_dicts.append(data_dict)

        return data_dicts

    @staticmethod
    def replace_none_with_dash(lists_of_measurements: list) -> list:
        i = 0

        for list_of_measurements in lists_of_measurements:
            for _ in list_of_measurements:
                if list_of_measurements[i] is None:
                    list_of_measurements[i] = '-'
                i += 1
            i = 0

        return lists_of_measurements

    @staticmethod
    def replace_in_list_none_with_dash(list_of_measurements: list) -> list:
        i = 0

        for _ in list_of_measurements:
            if list_of_measurements[i] is None:
                list_of_measurements[i] = '-'
            i += 1
        i = 0

        return list_of_measurements

    @staticmethod
    def fill_missing_data_in_lists(lists_of_measurements: list) -> list:
        i = 0
        for list_of_measurement in lists_of_measurements:
            if DataHandler.is_possible_to_fill_missing_data(list_of_measurement):
                indexes = DataHandler.get_indexes_for_filling(list_of_measurement)
                list_of_measurement = DataHandler.fill_missing_data_in_list(list_of_measurement, indexes)
                lists_of_measurements[i] = list_of_measurement
                i += 1
            else:
                i += 1
        return lists_of_measurements

    @staticmethod
    def get_station_codes() -> list:
        station_codes = []

        for i in range(1, 65):
            station_code = 'LV{:02d}'.format(i)
            station_codes.append(station_code)

        return station_codes

    @staticmethod
    def zip_codes_and_measurements(station_codes: list, lists_of_measurements: list) -> tuple:
        stop = len(lists_of_measurements)
        i = 0

        while i < stop:
            if '-' in lists_of_measurements[i] or not bool(lists_of_measurements[i]):
                lists_of_measurements.pop(i)
                station_codes.pop(i)
                stop -= 1
                i = 0
            else:
                i += 1

        return station_codes, lists_of_measurements

    @staticmethod
    def get_lists_of_ints(lists_of_values) -> list:
        for values in lists_of_values:
            i = 0
            while i < len(values):
                values[i] = int(values[i])
                i += 1

        return lists_of_values

    @staticmethod
    def get_accuracy(measurements: list, estimates: list) -> float:
        from sklearn.metrics import accuracy_score

        return accuracy_score(measurements, estimates)

    @staticmethod
    def get_accuracies(lists_of_measurements: list, lists_of_estimates: list) -> list:
        accuracies = []

        lists_of_estimates = DataHandler.get_lists_of_ints(lists_of_estimates)
        lists_of_measurements = DataHandler.get_lists_of_ints(lists_of_measurements)

        for measurements, estimates in zip(lists_of_measurements, lists_of_estimates):
            accuracies.append(DataHandler.get_accuracy(measurements, estimates))

        return accuracies

    @staticmethod
    def get_datetime_format(date_time: str):
        date_time = datetime.datetime.strptime(date_time, format('%Y-%m-%d %H:%M:%S'))
        return date_time

    @staticmethod
    def get_datetime_from_dataframe(data_df, date_from_request):
        while data_df.loc[data_df['Datetime'] == date_from_request].empty:
            date_from_request += datetime.timedelta(minutes=1)

        return date_from_request

    @staticmethod
    def get_datetime_and_measurements_dataframe(lists_of_datetime, lists_of_measurements, date_from, date_till):
        data_df = pd.DataFrame()
        data_df['Datetime'] = lists_of_datetime
        data_df['Measurements'] = lists_of_measurements

        date_from = DataHandler.get_datetime_from_dataframe(data_df, date_from)
        date_till = DataHandler.get_datetime_from_dataframe(data_df, date_till)

        data_df.set_index('Datetime', inplace=True)

        data_df = data_df.loc[date_from:date_till]

        return data_df

    @staticmethod
    def get_real_data_for_comparing_with_forecast(lists_of_datetime, lists_of_measurements,
                                                  date_from_for_actual_data, steps):
        actual_data_df = pd.DataFrame()
        actual_data_df['Datetime'] = lists_of_datetime
        actual_data_df['Measurements'] = lists_of_measurements

        date_from_for_real_data = DataHandler.get_datetime_from_dataframe(actual_data_df, date_from_for_actual_data)

        actual_data_df.set_index('Datetime', inplace=True)

        actual_data_df = actual_data_df.loc[date_from_for_real_data:][:steps]

        return actual_data_df

    @staticmethod
    def duplicate_dataframe_using_real_datafrme(actual_data_df, forecast_list):
        forecast_df = pd.DataFrame()
        forecast_df['Datetime'] = actual_data_df.index
        forecast_df['Measurements'] = forecast_list

        forecast_df.set_index('Datetime', inplace=True)

        return forecast_df
