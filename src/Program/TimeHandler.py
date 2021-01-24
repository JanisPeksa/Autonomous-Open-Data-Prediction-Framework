import pandas as pd
import datetime
import dateutil.relativedelta


class TimeHandler:

    def __init__(self, datetime_unit_of_measure: str, period_value: int,
                 date_from: str = None, date_till: str = None, list_of_datetime: list = None):

        if date_from is None:
            if list_of_datetime is None:
                raise Exception("Missing list_of_datetime value")
            else:
                self.date_from = list_of_datetime[0]
        else:
            self.date_from = self.get_datetime_format(date_from)

        if date_till is None:
            if list_of_datetime is None:
                raise Exception("Missing list_of_datetime value")
            else:
                self.date_till = list_of_datetime[-1]
        else:
            self.date_till = self.get_datetime_format(date_till)

        # datetime delta number
        self.period_value = period_value

        # minute, year, second, hour ...
        self.datetime_unit_of_measure = datetime_unit_of_measure
        # 1 minute
        self.datetime_value_of_one_unit = self.get_datetime_value_of_one_unit()
        # 11 minutes, 1 hour, 15 days ...
        self.datetime_delta_value = self.get_datetime_delta_value()

    @staticmethod
    def get_datetime_format(date_time: str):
        if len(date_time) == 10:
            date_time += " 00:00:00"
        else:
            date_time += ":00"
        date_time = datetime.datetime.strptime(date_time, format("%Y-%m-%d %H:%M:%S"))
        return date_time

    def get_datetime_from_series(self, data_series, date_from_request):

        max_number_of_iterations = TimeHandler.get_max_number_of_iterations(self.datetime_unit_of_measure)
        i = 0
        while data_series.loc[data_series.index == date_from_request].empty:
            date_from_request += self.datetime_value_of_one_unit
            i += 1
            if i >= max_number_of_iterations:
                return -1

        return date_from_request

    def get_datetime_from_dataframe_with_delta_limitation(self, data_df, date_from_request,
                                                          delta_limitation: int):
        i = 0
        while data_df.loc[data_df.index == date_from_request].empty:
            date_from_request += self.datetime_value_of_one_unit
            i += 1
            if i >= delta_limitation:
                return -1

        return date_from_request

    def get_datetime_and_measurements_series(self, list_of_measurements, list_of_datetime):

        data_series = pd.Series(list_of_measurements, index=list_of_datetime, dtype=float)

        date_from = self.get_datetime_from_series(data_series, self.date_from)
        date_till = self.get_datetime_from_series(data_series, self.date_till)

        if date_from == -1 or date_till == -1:
            return pd.Series()

        data_series = data_series.loc[date_from:date_till]

        return data_series

    @staticmethod
    def get_data_series(list_of_measurements, lists_of_datetime):
        data_series = pd.Series(list_of_measurements, index=lists_of_datetime, dtype=float)
        return data_series

    def get_datetime_delta_value(self):
        if self.datetime_unit_of_measure == "second":
            datetime_delta_value = datetime.timedelta(seconds=self.period_value)
            return datetime_delta_value
        elif self.datetime_unit_of_measure == "minute":
            datetime_delta_value = datetime.timedelta(minutes=self.period_value)
            return datetime_delta_value
        elif self.datetime_unit_of_measure == "hour":
            datetime_delta_value = datetime.timedelta(hours=self.period_value)
            return datetime_delta_value
        elif self.datetime_unit_of_measure == "day":
            datetime_delta_value = datetime.timedelta(days=self.period_value)
            return datetime_delta_value
        elif self.datetime_unit_of_measure == "month":
            datetime_delta_value = dateutil.relativedelta.relativedelta(months=self.period_value)
            return datetime_delta_value
        elif self.datetime_unit_of_measure == "year":
            datetime_delta_value = dateutil.relativedelta.relativedelta(years=self.period_value)
            return datetime_delta_value
        else:
            raise Exception("Parameter time_period_unit must be timedelta value")

    def get_datetime_value_of_one_unit(self):
        delta_value = 1
        if self.datetime_unit_of_measure == "second":
            datetime_value_of_one_unit = datetime.timedelta(seconds=delta_value)
            return datetime_value_of_one_unit
        elif self.datetime_unit_of_measure == "minute":
            datetime_value_of_one_unit = datetime.timedelta(minutes=delta_value)
            return datetime_value_of_one_unit
        elif self.datetime_unit_of_measure == "hour":
            datetime_value_of_one_unit = datetime.timedelta(hours=delta_value)
            return datetime_value_of_one_unit
        elif self.datetime_unit_of_measure == "day":
            datetime_value_of_one_unit = datetime.timedelta(days=delta_value)
            return datetime_value_of_one_unit
        elif self.datetime_unit_of_measure == "month":
            datetime_value_of_one_unit = dateutil.relativedelta.relativedelta(months=delta_value)
            return datetime_value_of_one_unit
        elif self.datetime_unit_of_measure == "year":
            datetime_value_of_one_unit = dateutil.relativedelta.relativedelta(years=delta_value)
            return datetime_value_of_one_unit
        else:
            raise Exception("Parameter time_period_unit must be timedelta value")

    @staticmethod
    def get_max_number_of_iterations(datetime_unit_of_measure):
        if datetime_unit_of_measure == "second":
            return 60
        elif datetime_unit_of_measure == "minute":
            return 60
        elif datetime_unit_of_measure == "hour":
            return 24
        elif datetime_unit_of_measure == "day":
            return 31
        elif datetime_unit_of_measure == "month":
            return 12
        elif datetime_unit_of_measure == "year":
            return 10
        else:
            raise Exception("Parameter time_period_unit must be timedelta value")

    def get_forecast_dict_with_datetime(self, forecast_list, last_datetime):
        forecast_dict = dict()
        for value in forecast_list:
            last_datetime += self.datetime_delta_value
            forecast_dict[str(last_datetime)] = round(value, 4)
        return forecast_dict
