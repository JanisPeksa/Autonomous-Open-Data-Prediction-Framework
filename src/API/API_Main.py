from flask import request
from flask_api import FlaskAPI
from Program.DataHandler import DataHandler
from Program.KF import KF_1D, KF_2D
from Program.MySQLClient import MySQLClient
from Program.ForecastingModel import ForecastingModel
from Program.Cluster import Cluster
from Program.DataFiller import DataFiller
from Program.TimeHandler import TimeHandler

app = FlaskAPI(__name__)


def data_still_has_none_values(station_code):
    results_dict = dict()
    json = dict()

    results_dict["Data overview: "] = "After data filling data still contains None values"
    json[station_code] = results_dict
    return json


def data_problems(station_code):
    results_dict = dict()
    json = dict()

    results_dict["Data overview: "] = "Data is fully empty or data indexes can not be found"
    json[station_code] = results_dict
    return json


@app.route("/use/1d_kalman_filter", methods=["GET"])
def get_filtered_values_using_1d_kalman_filter():
    sql_client = MySQLClient("xxx.xxx.xxx.xxx", "login", "pwd", "dbname")
    value = request.args["value"]
    station_code = request.args["station"]
    datetime_unit_of_measure = request.args["datetime_unit_of_measure"]
    period_value = int(request.args["period_value"])

    records = sql_client.get_info_by_station(station_code)

    list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
    list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

    time_handler = TimeHandler(datetime_unit_of_measure, period_value, list_of_datetime=list_of_datetime)
    series_of_measurements = time_handler.get_datetime_and_measurements_series(list_of_measurements, list_of_datetime)

    if series_of_measurements.empty:
        return data_problems(station_code)

    contains_none_values = False
    if series_of_measurements.isnull().values.any():
        contains_none_values = True
        station_locations_rec = sql_client.get_latitude_and_longitude()
        station_clusters_df = Cluster(station_locations_rec).get_stations_clusters_df()
        series_of_measurements = DataFiller(series_of_measurements, station_clusters_df, station_code,
                                            time_handler, sql_client).fill_the_data_none_values(value)

    if series_of_measurements.isnull().values.any():
        return data_still_has_none_values(station_code)

    filtered_values_list = KF_1D(series_of_measurements.values).get_filtered_values()

    results_dict = dict()
    json = dict()

    if contains_none_values:
        results_dict["Data overview: "] = "In the selected data were found and filled None values"
    else:
        results_dict["Data overview: "] = "Data has no None values"

    results_dict["Filtered values using 1D Kalman Filter: "] = filtered_values_list

    json[station_code] = results_dict

    return json


@app.route("/use/2d_kalman_filter", methods=["GET"])
def get_filtered_values_using_2d_kalman_filter():
    sql_client = MySQLClient("xxx.xxx.xxx.xxx", "login", "pwd", "dbname")
    value = request.args["value"]
    station_code = request.args["station"]
    datetime_unit_of_measure = request.args["datetime_unit_of_measure"]
    period_value = int(request.args["period_value"])
    try:
        position = float(request.args["position"])
    except KeyError:
        position = 0
    try:
        velocity = float(request.args["velocity"])
    except KeyError:
        velocity = 0
    try:
        time_delta = float(request.args["time_delta"])
    except KeyError:
        time_delta = 0.1

    records = sql_client.get_info_by_station(station_code)

    list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
    list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

    time_handler = TimeHandler(datetime_unit_of_measure, period_value, list_of_datetime=list_of_datetime)
    series_of_measurements = time_handler.get_datetime_and_measurements_series(list_of_measurements, list_of_datetime)

    if series_of_measurements.empty:
        return data_problems(station_code)

    contains_none_values = False
    if series_of_measurements.isnull().values.any():
        contains_none_values = True
        station_locations_rec = sql_client.get_latitude_and_longitude()
        station_clusters_df = Cluster(station_locations_rec).get_stations_clusters_df()
        series_of_measurements = DataFiller(series_of_measurements, station_clusters_df, station_code,
                                            time_handler, sql_client).fill_the_data_none_values(value)

    if series_of_measurements.isnull().values.any():
        return data_still_has_none_values(station_code)

    filtered_values = KF_2D(list_of_measurements, position=position, velocity=velocity,
                            time_delta=time_delta).get_filtered_values()

    results_dict = dict()
    json = dict()

    if contains_none_values:
        results_dict["Data overview: "] = "In the selected data were found and filled None values"
    else:
        results_dict["Data overview: "] = "Data has no None values"

    results_dict["Filtered values using 2D Kalman Filter: "] = filtered_values

    json[station_code] = results_dict

    return json


@app.route("/get/forecast", methods=["GET"])
def get_forecast():
    sql_client = MySQLClient("xxx.xxx.xxx.xxx", "login", "pwd", "dbname")
    model_name = request.args["model_name"]
    value = request.args["value"]
    station_code = request.args["station"]
    steps = int(request.args["steps"])
    datetime_unit_of_measure = request.args["datetime_unit_of_measure"]
    period_value = int(request.args["period_value"])
    try:
        using_Kalman_Filter = request.args["using_Kalman_Filter"] in ["True", "true"]
    except:
        using_Kalman_Filter = False

    records = sql_client.get_info_by_station(station_code)

    list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
    list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

    if len(list_of_measurements) > 1000:
        list_of_measurements = list_of_measurements[-1000:]
        list_of_datetime = list_of_datetime[-1000:]
    elif len(list_of_measurements) < 100:
        raise Exception("list of measurements must contain at least 100 values")

    time_handler = TimeHandler(datetime_unit_of_measure, period_value, list_of_datetime=list_of_datetime)
    series_of_measurements = time_handler.get_datetime_and_measurements_series(list_of_measurements, list_of_datetime)

    if series_of_measurements.empty:
        return data_problems(station_code)

    contains_none_values = False
    if series_of_measurements.isnull().values.any():
        contains_none_values = True
        station_locations_rec = sql_client.get_latitude_and_longitude()
        station_clusters_df = Cluster(station_locations_rec).get_stations_clusters_df()
        series_of_measurements = DataFiller(series_of_measurements, station_clusters_df, station_code,
                                            time_handler, sql_client).fill_the_data_none_values(value)

    if series_of_measurements.isnull().values.any():
        return data_still_has_none_values(station_code)

    if using_Kalman_Filter:
        filtered_values_list = KF_1D(series_of_measurements.values).get_filtered_values()
        series_of_measurements = time_handler.get_data_series(filtered_values_list, series_of_measurements.index)

    model = ForecastingModel(model_name, series_of_measurements, steps, station_code)
    forecast = model.get_forecast()
    data_points = model.data_points_to_use
    model_order = model.best_model_order

    results_dict = dict()
    json = dict()

    if contains_none_values:
        results_dict["Data overview: "] = "In the selected data were found and filled None values"
    else:
        results_dict["Data overview: "] = "Data has no None values"

    if forecast is not None:
        p, d, q = model_order

        if model_name == "ARIMA":
            model_order = {"p: ": p,
                           "d: ": d,
                           "q: ": q}
        elif model_name == "ARMA":
            model_order = {"p: ": p,
                           "q: ": q}
        elif model_name == "AR":
            model_order = {"p: ": p}
        elif model_name == "MA":
            model_order = {"q: ": q}

        results_dict["Data points: "] = data_points
        results_dict["{} model order: ".format(model_name)] = model_order
        results_dict["Steps: "] = steps
        results_dict["Kalman Filter: "] = using_Kalman_Filter
        forecast_dict = time_handler.get_forecast_dict_with_datetime(forecast, series_of_measurements.index[-1])
        results_dict["Forecast: "] = forecast_dict
    else:
        results_dict["{} results: ".format(model_name)] = "{} model was not created".format(model_name)

    json[station_code] = results_dict

    return json


@app.route("/get/forecast/time_period", methods=["GET"])
def get_forecast_by_time_period():
    sql_client = MySQLClient("xxx.xxx.xxx.xxx", "login", "pwd", "dbname")
    model_name = request.args["model_name"]
    value = request.args["value"]
    station_code = request.args["station"]
    steps = int(request.args["steps"])
    datetime_unit_of_measure = request.args["datetime_unit_of_measure"]
    period_value = int(request.args["period_value"])
    try:
        using_Kalman_Filter = request.args["using_Kalman_Filter"] in ["True", "true"]
    except:
        using_Kalman_Filter = False

    # YYYY-MM-DD ---> YYYY-MM-DD HH:MM:SS
    date_from = request.args["date_from"].replace("_", " ")
    date_till = request.args["date_till"].replace("_", " ")

    records = sql_client.get_info_by_station(station_code)

    list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
    list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

    time_handler = TimeHandler(datetime_unit_of_measure, period_value, date_from, date_till)
    series_of_measurements = time_handler.get_datetime_and_measurements_series(list_of_measurements, list_of_datetime)

    if series_of_measurements.empty:
        return data_problems(station_code)

    contains_none_values = False
    if series_of_measurements.isnull().values.any():
        contains_none_values = True
        station_locations_rec = sql_client.get_latitude_and_longitude()
        station_clusters_df = Cluster(station_locations_rec).get_stations_clusters_df()
        series_of_measurements = DataFiller(series_of_measurements, station_clusters_df, station_code,
                                            time_handler, sql_client).fill_the_data_none_values(value)

    if series_of_measurements.isnull().values.any():
        return data_still_has_none_values(station_code)

    if using_Kalman_Filter:
        filtered_values_list = KF_1D(series_of_measurements.values).get_filtered_values()
        series_of_measurements = time_handler.get_data_series(filtered_values_list, series_of_measurements.index)

    model = ForecastingModel(model_name, series_of_measurements, steps, station_code)
    forecast = model.get_forecast()
    data_points = model.data_points_to_use
    model_order = model.best_model_order

    results_dict = dict()
    json = dict()

    if contains_none_values:
        results_dict["Data overview: "] = "In the selected data were found and filled None values"
    else:
        results_dict["Data overview: "] = "Data has no None values"

    if forecast is not None:
        p, d, q = model_order

        if model_name == "ARIMA":
            model_order = {"p: ": p,
                           "d: ": d,
                           "q: ": q}
        elif model_name == "ARMA":
            model_order = {"p: ": p,
                           "q: ": q}
        elif model_name == "AR":
            model_order = {"p: ": p}
        elif model_name == "MA":
            model_order = {"q: ": q}

        results_dict["Date from: "] = date_from
        results_dict["Date till: "] = date_till
        results_dict["Data points: "] = data_points
        results_dict["{} model order: ".format(model_name)] = model_order
        results_dict["Steps: "] = steps
        results_dict["Kalman Filter: "] = using_Kalman_Filter
        forecast_dict = time_handler.get_forecast_dict_with_datetime(forecast, series_of_measurements.index[-1])
        results_dict["Forecast: "] = forecast_dict
    else:
        results_dict["{} results: ".format(model_name)] = "{} model was not created".format(model_name)

    json[station_code] = results_dict

    return json


@app.route("/get/forecast/all_models", methods=["GET"])
def get_forecast_all_models():
    sql_client = MySQLClient("xxx.xxx.xxx.xxx", "login", "pwd", "dbname")
    value = request.args["value"]
    station_code = request.args["station"]
    steps = int(request.args["steps"])
    datetime_unit_of_measure = request.args["datetime_unit_of_measure"]
    period_value = int(request.args["period_value"])
    try:
        using_Kalman_Filter = request.args["using_Kalman_Filter"] in ["True", "true"]
    except:
        using_Kalman_Filter = False

    records = sql_client.get_info_by_station(station_code)

    list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
    list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

    if len(list_of_measurements) > 1000:
        list_of_measurements = list_of_measurements[-1000:]
        list_of_datetime = list_of_datetime[-1000:]
    elif len(list_of_measurements) < 100:
        raise Exception("list of measurements must contain at least 100 values")

    time_handler = TimeHandler(datetime_unit_of_measure, period_value, list_of_datetime=list_of_datetime)
    series_of_measurements = time_handler.get_datetime_and_measurements_series(list_of_measurements, list_of_datetime)

    if series_of_measurements.empty:
        return data_problems(station_code)

    contains_none_values = False
    if series_of_measurements.isnull().values.any():
        contains_none_values = True
        station_locations_rec = sql_client.get_latitude_and_longitude()
        station_clusters_df = Cluster(station_locations_rec).get_stations_clusters_df()
        series_of_measurements = DataFiller(series_of_measurements, station_clusters_df, station_code,
                                            time_handler, sql_client).fill_the_data_none_values(value)

    if series_of_measurements.isnull().values.any():
        return data_still_has_none_values(station_code)

    if using_Kalman_Filter:
        filtered_values_list = KF_1D(series_of_measurements.values).get_filtered_values()
        series_of_measurements = time_handler.get_data_series(filtered_values_list, series_of_measurements.index)

    arima_model = ForecastingModel("ARIMA", series_of_measurements, steps, station_code)
    forecast_arima = arima_model.get_forecast()
    arima_data_points = arima_model.data_points_to_use
    arima_model_order = arima_model.best_model_order

    arma_model = ForecastingModel("ARMA", series_of_measurements, steps, station_code)
    forecast_arma = arma_model.get_forecast()
    arma_data_points = arma_model.data_points_to_use
    arma_model_order = arma_model.best_model_order

    ar_model = ForecastingModel("AR", series_of_measurements, steps, station_code)
    forecast_ar = ar_model.get_forecast()
    ar_data_points = ar_model.data_points_to_use
    ar_model_order = ar_model.best_model_order

    ma_model = ForecastingModel("MA", series_of_measurements, steps, station_code)
    forecast_ma = ma_model.get_forecast()
    ma_data_points = ma_model.data_points_to_use
    ma_model_order = ma_model.best_model_order

    results_dict = dict()
    json = dict()

    if contains_none_values:
        results_dict["Data overview: "] = "In the selected data were found and filled None values"
    else:
        results_dict["Data overview: "] = "Data has no None values"

    # ARIMA results
    if forecast_arima is not None:
        p, d, q = arima_model_order
        arima_model_order = {"p: ": p,
                             "d: ": d,
                             "q: ": q}

        results_dict["Data points for ARIMA: "] = arima_data_points
        results_dict["ARIMA model order: "] = arima_model_order
        results_dict["Steps: "] = steps
        results_dict["ARIMA forecast: "] = forecast_arima
    else:
        results_dict["ARIMA results: "] = "ARIMA model was not created"

    # ARMA results
    if forecast_arma is not None:
        p, d, q = arma_model_order
        arma_model_order = {"p: ": p,
                            "q: ": q}

        results_dict["Data points for ARMA: "] = arma_data_points
        results_dict["ARMA model order: "] = arma_model_order
        results_dict["Steps: "] = steps
        results_dict["ARMA forecast: "] = forecast_arma
    else:
        results_dict["ARMA results: "] = "ARMA model was not created"

    # AR results
    if forecast_ar is not None:
        p, d, q = ar_model_order
        ar_model_order = {"p: ": p}

        results_dict["Data points for AR: "] = ar_data_points
        results_dict["AR model order: "] = ar_model_order
        results_dict["Steps: "] = steps
        results_dict["AR forecast: "] = forecast_ar
    else:
        results_dict["AR results: "] = "AR model was not created"

    # MA results
    if forecast_ma is not None:
        p, d, q = ma_model_order
        ma_model_order = {"q: ": q}

        results_dict["Data points for MA: "] = ma_data_points
        results_dict["MA model order: "] = ma_model_order
        results_dict["Steps: "] = steps
        results_dict["MA forecast: "] = forecast_ma
    else:
        results_dict["MA results: "] = "MA model was not created"

    json["Kalman Filter: "] = using_Kalman_Filter
    json[station_code] = results_dict

    return json
