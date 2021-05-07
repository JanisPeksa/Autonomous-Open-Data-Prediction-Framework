from os import listdir, rename
from os.path import isfile, join
import pandas as pd

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


def rename_station_files():
    path = "C:\\Users\\Modni\\Desktop\\py\\Forecasting_web_app_for_testing\\API\\Stations"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    print(files)

    for file in files:
        df = pd.read_excel(io=path + "\\" + file)
        name = df.columns[0].split(",")[0] + ".xls"
        rename(path + "\\" + file, path + "\\" + name)


def read_station_file():
    path = "C:\\...\\API\\Stations"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    print(files)

    columns = ["Datums \ Laiks", "00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00",
               "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00",
               "20:00", "21:00", "22:00", "23:00"]

    for file in files:
        df = pd.read_excel(io=path + "\\" + file)
        df = df.iloc[1:]
        df.columns = columns
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(df)
