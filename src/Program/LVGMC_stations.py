import math
import pandas as pd
from math import sin, cos, sqrt, atan2, radians


locations = {"Rucava": (56.162, 21.1732),
             "Liepāja": (56.4754, 21.0206),
             "Pāvilosta": (56.8883, 21.1896),
             "Ventspils": (57.3956, 21.5373),
             "Kolka": (57.747003, 22.587788),
             "Stende": (57.1834, 22.5508),
             "Mērsrags": (57.3332, 23.1132),
             "Saldus": (56.71014, 22.426743),
             "Dobele": (56.6199, 23.3196),
             "Jelgava": (56.556932, 23.964077),
             "Rīga - Universitāte": (56.954797, 24.104686),
             "Bauska": (56.36667, 24.21667),
             "Skulte": (57.3006, 24.4122),
             "Ainaži": (57.8679, 24.366),
             "Skrīveri": (56.642474, 25.128349),
             "Priekuļi": (57.315602, 25.337983),
             "Zosēni": (57.1351, 25.9056),
             "Madona": (56.8483, 26.2375),
             "Zīlāni": (56.52, 25.9182),
             "Alūksne": (57.4396, 27.0354),
             "Daugavpils": (55.8698, 26.6174),
             "Rēzekne": (56.479862, 27.357136),
             "Dagda": (56.107, 27.56),
             "Gulbene": (57.1322, 26.7188),
             "Rūjiena": (57.8865, 25.3718)}

columns = ["Datums \ Laiks", "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00",
           "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00",
           "20:00", "21:00", "22:00", "23:00"]


class LVGMS_stations:
    def __init__(self, station: str, station_locations_rec: list):
        self.station_lat_long = tuple(self.get_proper_lan_and_long(station, station_locations_rec))
        self.nearest_station = None

        self.df_temperature = None
        self.df_humidity = None
        self.lvgms_station_indexes = None

    @staticmethod
    def get_proper_lan_and_long(station, station_locations_rec):
        for station_records in station_locations_rec:
            if station in station_records:
                return float(station_records[3]), float(station_records[4])

    def get_distance_between_stations(self):
        distances_dict = {}

        # approximate radius of earth in km
        R = 6373.0

        for lvgmc_station, lat_long in locations.items():
            lat1 = radians(lat_long[0])
            lon1 = radians(lat_long[1])

            lat2 = radians(self.station_lat_long[0])
            lon2 = radians(self.station_lat_long[1])

            d_lon = lon2 - lon1
            d_lat = lat2 - lat1

            a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            # distance = R * c
            distances_dict[lvgmc_station] = R * c

        return distances_dict

    def get_the_nearest_station(self):
        distances_dict = self.get_distance_between_stations()
        nearest_station = min(distances_dict.items(), key=lambda x: x[1])
        return nearest_station

    def get_lvgmc_station_data(self):
        nearest_station = self.get_the_nearest_station()
        self.nearest_station = nearest_station[0]
        file = "Stations\\{}.xls".format(nearest_station[0])
        df_temperature = pd.read_excel(io=file, sheet_name="1. tabula")
        df_humidity = pd.read_excel(io=file, sheet_name="2. tabula")
        df_temperature = df_temperature.iloc[1:]
        df_humidity = df_humidity.iloc[1:]
        df_temperature.columns = columns
        df_humidity.columns = columns

        df_temperature.set_index("Datums \ Laiks", inplace=True)
        df_humidity.set_index("Datums \ Laiks", inplace=True)

        self.df_temperature = df_temperature
        self.df_humidity = df_humidity
        self.lvgms_station_indexes = df_temperature.index

    def get_second_data_type_value(self, datetime):
        i = datetime.strftime("%Y-%m-%d %S:%M:%H")
        date, time = i.split(" ")
        year, month, day = date.split("-")
        hours = time.split(":")[0]
        d = "{}.{}.{}".format(day, month, year)
        t = "{}:00".format(hours)
        if d not in self.lvgms_station_indexes:
            return None
        else:
            if math.isnan(self.df_temperature.loc[d, t]) or math.isnan(self.df_humidity.loc[d, t]):
                return None
            else:
                return self.df_temperature.loc[d, t] - (100 - self.df_humidity.loc[d, t]) / 5
