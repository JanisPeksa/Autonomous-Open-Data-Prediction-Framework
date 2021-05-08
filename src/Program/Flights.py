from pyflightdata import FlightData
import pandas as pd
from datetime import datetime, timedelta
import pytz


class Flights:
    def __init__(self, login: str, password: str):

        self.flight_data = self.sign_in(login, password)

        self.departure_airport = None
        self.arrival_airport = None

        self.preferred_time_from = None
        self.preferred_time_to = None

        self.time_delta_departure_with_utc = None
        self.time_delta_arrival_with_utc = None

    @staticmethod
    def sign_in(login, password):
        flight_data = FlightData()
        flight_data.login(login, password)
        return flight_data

    def get_all_flight_numbers_from_to(self):
        flights = self.flight_data.get_flights_from_to(self.departure_airport, self.arrival_airport)
        f_list = []
        for f in flights:
            flight_number = f["identification"]["number"]["default"]
            if flight_number in f_list:
                continue
            else:
                f_list.append(flight_number)
        return f_list

    def get_history_by_the_flight_number(self, flight_number: str):
        history_by_flight_number = self.flight_data.get_history_by_flight_number(flight_number)
        flights_history_df = self.get_df_from_flight_history(history_by_flight_number, flight_number)
        return flights_history_df

    def get_df_from_flight_history(self, history: list, flight_number: str):
        departure_date_and_time_scheduled = []
        departure_date_and_time_real = []
        duration_list = []
        for flight in history:
            if "departure_date" not in flight["time"]["scheduled"] or \
                    "departure_time" not in flight["time"]["scheduled"]:
                continue

            duration = flight["time"]["other"]["duration"]

            if flight["time"]["real"]["departure"] == "None":
                departure_date_and_time_real.append("None")
            else:
                date_real = self.get_date_str_format(flight["time"]["real"]["departure_date"])
                time_real = self.get_time_str_format(flight["time"]["real"]["departure_time"])

                # if already started to fly, but hasn't landed
                if duration == "None" and date_real != "None":
                    continue
                else:
                    departure_date_and_time_real.append(date_real + " " + time_real)
            if duration == "None":
                duration_list.append(duration)
            else:
                duration_list.append(int(duration))

            date_scheduled = self.get_date_str_format(flight["time"]["scheduled"]["departure_date"])
            time_scheduled = self.get_time_str_format(flight["time"]["scheduled"]["departure_time"])
            departure_date_and_time_scheduled.append(date_scheduled + " " + time_scheduled)

        df = pd.DataFrame({"departure_date_time_scheduled": departure_date_and_time_scheduled,
                           "departure_date_time_real": departure_date_and_time_real,
                           "duration_in_seconds": duration_list})

        df.index.name = flight_number

        return df

    @staticmethod
    def get_date_str_format(date: str):
        return date[:4] + "." + date[4:6] + "." + date[6:]

    @staticmethod
    def get_time_str_format(time: str):
        return time[:2] + ":" + time[2:] + ":00"

    def get_dict_for_planned_flights(self):
        flight_numbers_from_to = self.get_all_flight_numbers_from_to()
        if not flight_numbers_from_to:
            return {}, {}
        else:
            forecast_in_utc_dict = {}
            data_info = {}
            for flight_number in flight_numbers_from_to:
                history_df = self.get_history_by_the_flight_number(flight_number)
                history_of_planned_flights = history_df[history_df["duration_in_seconds"] == "None"]
                num_of_planned_flights = len(history_of_planned_flights)
                if num_of_planned_flights <= 0:
                    continue

                duration_average = int(history_df[history_df["duration_in_seconds"] != "None"].mean(skipna=True))
                duration_var = int(history_df[history_df["duration_in_seconds"] != "None"].var(skipna=True))

                delay_average, delay_var = self.get_average_and_var_of_delay(history_df)
                delay_average = int(delay_average)
                delay_var = int(delay_var)

                dep_and_arr_in_utc_list = self.get_predicted_time_of_arrival_in_utc(history_of_planned_flights,
                                                                                    duration_average, delay_average)

                forecast_in_utc_dict[flight_number] = dep_and_arr_in_utc_list
                if flight_number not in data_info:
                    data_info[flight_number] = {"Duration average": duration_average,
                                                "Duration variation": duration_var,
                                                "Delay average": delay_average,
                                                "Delay variation": delay_var}

            return forecast_in_utc_dict, data_info

    @staticmethod
    def get_forecast_df_in_utc(forecast_dict: dict):
        df_forecast_in_utc = pd.DataFrame()
        for flight_number, forecast in forecast_dict.items():
            df = pd.DataFrame({"flight_number": [flight_number] * len(forecast[0]),
                               "departure": forecast[0],
                               "arrival": forecast[1]})
            df_forecast_in_utc = df_forecast_in_utc.append(df, ignore_index=True)

        df_forecast_in_utc["departure"] = pd.to_datetime(df_forecast_in_utc["departure"], format="%Y.%m.%d %H:%M:%S")
        df_forecast_in_utc["arrival"] = pd.to_datetime(df_forecast_in_utc["arrival"], format="%Y.%m.%d %H:%M:%S")
        df_forecast_in_utc.sort_values(by="departure", inplace=True)
        df_forecast_in_utc.reset_index(inplace=True, drop=True)
        return df_forecast_in_utc

    def get_forecast_df_in_time_of_departure(self, df_forecast_in_utc):
        df = df_forecast_in_utc.copy()
        delta = self.get_time_delta_airport_time_with_utc(self.departure_airport)
        df["departure"] += delta
        df["arrival"] += delta
        return df

    @staticmethod
    def get_average_and_var_of_delay(history_df):
        history = history_df[history_df["departure_date_time_real"] != "None"].copy()
        history["departure_date_time_real"] = pd.to_datetime(history["departure_date_time_real"],
                                                             format="%Y.%m.%d %H:%M:%S")
        history["departure_date_time_scheduled"] = pd.to_datetime(history["departure_date_time_scheduled"],
                                                                  format="%Y.%m.%d %H:%M:%S")
        history["delay"] = history["departure_date_time_real"] - history["departure_date_time_scheduled"]
        history["delay"] = history["delay"].astype("timedelta64[s]")

        delay_average = history["delay"].mean(skipna=True)
        delay_var = history["delay"].var(skipna=True)

        return delay_average, delay_var

    @staticmethod
    def get_predicted_time_of_arrival_in_utc(history_of_planned_flights, duration_average: int, delay_average: int):
        num_of_planned_flights = len(history_of_planned_flights)
        departure_in_utc_list = []
        arrival_in_utc_list = []
        for i in range(num_of_planned_flights):
            data = history_of_planned_flights.iloc[-1 - i, :]["departure_date_time_scheduled"]
            # to perform time in UTC -2 h
            # str to datetime
            departure_in_utc = datetime.strptime(data, "%Y.%m.%d %H:%M:%S") - timedelta(hours=2)
            utc_time = datetime.now(pytz.timezone("UTC")).replace(tzinfo=None)
            if departure_in_utc < utc_time:
                continue
            arrival_in_utc = departure_in_utc + timedelta(seconds=duration_average)
            arrival_in_utc += timedelta(seconds=delay_average)  # add delay for flight
            # datetime to str
            departure_in_utc = datetime.strftime(departure_in_utc, "%Y.%m.%d %H:%M:%S")
            arrival_in_utc = datetime.strftime(arrival_in_utc, "%Y.%m.%d %H:%M:%S")
            departure_in_utc_list.append(departure_in_utc)
            arrival_in_utc_list.append(arrival_in_utc)
        return [departure_in_utc_list, arrival_in_utc_list]

    def get_local_datetime_in_airport(self, airport_name: str):
        info = self.flight_data.get_airport_details(airport_name)["timezone"]["name"]
        local_time_in_airport = self.get_local_datetime_in_airport_by_timezone(info)
        return local_time_in_airport

    def get_time_delta_airport_time_with_utc(self, airport_name: str):
        info = self.flight_data.get_airport_details(airport_name)["timezone"]["name"]
        local_time_in_airport = self.get_local_datetime_in_airport_by_timezone(info)
        local_time_by_utc = datetime.now(pytz.timezone("UTC")).replace(tzinfo=None)

        return local_time_in_airport - local_time_by_utc

    @staticmethod
    def get_local_datetime_in_airport_by_timezone(time_zone: str):
        tz = pytz.timezone(time_zone)
        local_lime_in_airport = datetime.now(tz).replace(tzinfo=None)
        return local_lime_in_airport

    def get_flights_forecast(self, origin: str, destination: str,
                             preferred_date: str = None, preferred_time_of_day: str = None):

        self.departure_airport = origin
        self.arrival_airport = destination

        self.time_delta_departure_with_utc = self.get_time_delta_airport_time_with_utc(origin)
        self.time_delta_arrival_with_utc = self.get_time_delta_airport_time_with_utc(destination)

        forecast_in_utc_dict, data_info = self.get_dict_for_planned_flights()

        if not forecast_in_utc_dict:
            return pd.DataFrame(), data_info

        df_forecast_in_utc = self.get_forecast_df_in_utc(forecast_in_utc_dict)

        if preferred_date is not None and preferred_time_of_day is not None:
            preferred_date_time_from, preferred_date_time_to = self.get_preferred_time_period(preferred_date,
                                                                                              preferred_time_of_day)

            preferred_date_time_from = datetime.strptime(preferred_date_time_from, "%Y.%m.%d %H:%M:%S")
            preferred_date_time_to = datetime.strptime(preferred_date_time_to, "%Y.%m.%d %H:%M:%S")

            preferred_date_time_from -= self.time_delta_departure_with_utc
            preferred_date_time_to -= self.time_delta_departure_with_utc

            return df_forecast_in_utc[(df_forecast_in_utc["departure"] >= preferred_date_time_from) &
                                      (df_forecast_in_utc["departure"] <= preferred_date_time_to)], data_info

        return df_forecast_in_utc, data_info

    @staticmethod
    def get_df_with_str_instead_of_datetime(df):
        df["departure"] = df["departure"].dt.strftime("%Y.%m.%d %H:%M:%S")
        df["arrival"] = df["arrival"].dt.strftime("%Y.%m.%d %H:%M:%S")
        return df

    @staticmethod
    def get_preferred_time_period(preferred_date: str, preferred_time_of_day: str):
        preferred_time_of_day = preferred_time_of_day.lower()
        if preferred_time_of_day == "morning":  # 06:00 - 12:00
            return preferred_date + " 06:00:00", preferred_date + " 12:00:00"
        elif preferred_time_of_day == "afternoon":  # 12:00 - 18:00
            return preferred_date + " 12:00:00", preferred_date + " 18:00:00"
        elif preferred_time_of_day == "evening":  # 18:00 - 24:00
            return preferred_date + " 18:00:00", preferred_date + " 23:59:00"
        elif preferred_time_of_day == "night":  # 24:00 - 06:00
            return preferred_date + " 00:00:00", preferred_date + " 06:00:00"
        else:
            return None, None

    def get_list_of_airports(self, country):
        airports_list = []
        airports = self.flight_data.get_airports(country)
        for airport in airports:
            airports_list.append(airport["iata"])
        return airports_list
