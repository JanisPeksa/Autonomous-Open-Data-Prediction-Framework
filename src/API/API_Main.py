from Program.Test import Test
from flask import request
from flask_api import FlaskAPI
from Program.DataHandler import DataHandler
from Program.KF import KF_1D, KF_2D
from Program.MySQLClient import MySQLClient
from Program.Forecasting_Model import Forecasting_Model
from Program.Cluster import Cluster
from Program.DataFiller import DataFiller
from Program.TimeHandler import TimeHandler
from Program.Flights import Flights

app = FlaskAPI(__name__)


def data_still_has_none_values(station_code):
    results_dict = dict()
    response_json = dict()

    results_dict["Data overview: "] = "After data filling data still contains None values"
    response_json[station_code] = results_dict
    return response_json


def data_problems(station_code):
    results_dict = dict()
    response_json = dict()

    results_dict["Data overview: "] = "Data is fully empty or data indexes can not be found"
    response_json[station_code] = results_dict
    return response_json


def data_is_too_small(station_code):
    results_dict = dict()
    response_json = dict()

    results_dict["Data overview: "] = "Data must contain more than 100 values"
    response_json[station_code] = results_dict
    return response_json


@app.route("/use/1d_kalman_filter", methods=["GET"])
def get_filtered_values_using_1d_kalman_filter():
    sql_client = MySQLClient("xxx.xxx.xxx.xxx", "login", "pwd", "dbname")
    value = request.args["value"]
    station_code = request.args["station"]
    datetime_unit_of_measure = request.args["datetime_unit_of_measure"]
    period_value = int(request.args["period_value"])

    try:
        use_second_data_type = request.args["use_second_data_type"] in ["True", "true"]
    except:
        use_second_data_type = False

    try:
        # YYYY-MM-DD ---> YYYY-MM-DD HH:MM:SS
        date_from = request.args["date_from"].replace("_", " ")
        date_till = request.args["date_till"].replace("_", " ")
    except:
        date_from = None
        date_till = None

    records = sql_client.get_info_by_station(station_code)

    list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
    list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

    time_handler = TimeHandler(datetime_unit_of_measure, period_value, date_from=date_from, date_till=date_till)
    data_df = time_handler.get_datetime_and_measurements_dataframe(list_of_datetime, list_of_measurements)
    data_df = data_df[~data_df.index.duplicated(keep='first')]

    if data_df.empty:
        return data_problems(station_code)

    contains_none_values = False
    if data_df.isnull().values.any():
        contains_none_values = True
        station_locations_rec = sql_client.get_latitude_and_longitude()
        station_clusters_df = Cluster(station_locations_rec).get_stations_clusters_df()

        data_df = DataFiller(data_df, station_clusters_df, station_code, time_handler,
                             sql_client, station_locations_rec, use_second_data_type).fill_data_none_values(value)

    if data_df.isnull().values.any():
        return data_still_has_none_values(station_code)

    filtered_values_list = KF_1D(DataHandler.get_list_of_dataframe_values(data_df.values)).get_filtered_values()

    results_dict = dict()
    response_json = dict()

    if contains_none_values:
        results_dict["Data overview: "] = "In the selected data were found and filled None values"
    else:
        results_dict["Data overview: "] = "Data has no None values"

    results_dict["Filtered values using 1D Kalman Filter: "] = filtered_values_list

    response_json[station_code] = results_dict

    return response_json


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

    try:
        use_second_data_type = request.args["use_second_data_type"] in ["True", "true"]
    except:
        use_second_data_type = False

    try:
        # YYYY-MM-DD ---> YYYY-MM-DD HH:MM:SS
        date_from = request.args["date_from"].replace("_", " ")
        date_till = request.args["date_till"].replace("_", " ")
    except:
        date_from = None
        date_till = None

    records = sql_client.get_info_by_station(station_code)

    list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
    list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

    time_handler = TimeHandler(datetime_unit_of_measure, period_value, date_from=date_from, date_till=date_till)
    data_df = time_handler.get_datetime_and_measurements_dataframe(list_of_datetime, list_of_measurements)
    data_df = data_df[~data_df.index.duplicated(keep='first')]

    if data_df.empty:
        return data_problems(station_code)

    contains_none_values = False
    if data_df.isnull().values.any():
        contains_none_values = True
        station_locations_rec = sql_client.get_latitude_and_longitude()
        station_clusters_df = Cluster(station_locations_rec).get_stations_clusters_df()

        data_df = DataFiller(data_df, station_clusters_df, station_code, time_handler,
                             sql_client, station_locations_rec, use_second_data_type).fill_data_none_values(value)

    if data_df.isnull().values.any():
        return data_still_has_none_values(station_code)

    filtered_values = KF_2D(DataHandler.get_list_of_dataframe_values(data_df.values), position=position,
                            velocity=velocity, time_delta=time_delta).get_filtered_values()

    results_dict = dict()
    response_json = dict()

    if contains_none_values:
        results_dict["Data overview: "] = "In the selected data were found and filled None values"
    else:
        results_dict["Data overview: "] = "Data has no None values"

    results_dict["Filtered values using 2D Kalman Filter: "] = filtered_values

    response_json[station_code] = results_dict

    return response_json


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
        use_fk = request.args["use_Kalman_Filter"] in ["True", "true"]
    except:
        use_fk = False

    try:
        use_second_data_type = request.args["use_second_data_type"] in ["True", "true"]
    except:
        use_second_data_type = False

    try:
        optimize = request.args["optimize"] in ["True", "true"]
    except:
        optimize = True

    date_from = None
    date_till = None

    records = sql_client.get_info_by_station(station_code)

    list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
    list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

    # if optimize:
    #     if len(list_of_measurements) > 1000:
    #         list_of_measurements = list_of_measurements[-1000:]
    #         list_of_datetime = list_of_datetime[-1000:]
    #
    # if len(list_of_measurements) < 100:
    #     return data_is_too_small(station_code)

    time_handler = TimeHandler(datetime_unit_of_measure, period_value, date_from=date_from, date_till=date_till)
    data_df = time_handler.get_datetime_and_measurements_dataframe(list_of_datetime, list_of_measurements)
    data_df = data_df[~data_df.index.duplicated(keep='first')]

    if data_df.empty:
        return data_problems(station_code)

    if optimize and len(data_df) > 1100:
        data_df = data_df.iloc[-1100:]

    print(data_df)

    contains_none_values = False
    if data_df.isnull().values.any():
        contains_none_values = True
        station_locations_rec = sql_client.get_latitude_and_longitude()
        station_clusters_df = Cluster(station_locations_rec).get_stations_clusters_df()

        data_df = DataFiller(data_df, station_clusters_df, station_code, time_handler,
                             sql_client, station_locations_rec, use_second_data_type).fill_data_none_values(value)

    print(data_df)

    if data_df.isnull().values.any():
        return data_still_has_none_values(station_code)

    if use_fk:
        filtered_values_list = KF_1D(DataHandler.get_list_of_dataframe_values(data_df.values)).get_filtered_values()
        data_df["Measurements"] = filtered_values_list

    data_df.sort_index(inplace=True)

    model = Forecasting_Model(model_name, data_df, steps, station_code, optimize)

    forecast = model.get_forecast()
    data_points = model.data_points_to_use
    model_order = model.best_model_order

    results_dict = dict()
    response_json = dict()

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
        results_dict["Kalman Filter: "] = use_fk
        results_dict["Use second data type: "] = use_second_data_type
        forecast_dict = time_handler.get_forecast_dict_with_datetime(forecast, data_df.index[-1])
        results_dict["Forecast: "] = forecast_dict
    else:
        results_dict["{} results: ".format(model_name)] = "{} model was not created".format(model_name)

    response_json[station_code] = results_dict

    return response_json


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
        use_fk = request.args["use_Kalman_Filter"] in ["True", "true"]
    except:
        use_fk = False

    try:
        use_second_data_type = request.args["use_second_data_type"] in ["True", "true"]
    except:
        use_second_data_type = False

    try:
        optimize = request.args["optimize"] in ["True", "true"]
    except:
        optimize = True

    try:
        # YYYY-MM-DD ---> YYYY-MM-DD HH:MM:SS
        date_from = request.args["date_from"].replace("_", " ")
        date_till = request.args["date_till"].replace("_", " ")
    except:
        date_from = None
        date_till = None

    # if optimize:
    #     if len(list_of_measurements) > 1000:
    #         list_of_measurements = list_of_measurements[-1000:]
    #         list_of_datetime = list_of_datetime[-1000:]
    #
    # if len(list_of_measurements) < 100:
    #     return data_is_too_small(station_code)

    records = sql_client.get_info_by_station(station_code)

    list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
    list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

    time_handler = TimeHandler(datetime_unit_of_measure, period_value, date_from=date_from, date_till=date_till)
    data_df = time_handler.get_datetime_and_measurements_dataframe(list_of_datetime, list_of_measurements)
    data_df = data_df[~data_df.index.duplicated(keep='first')]

    if data_df.empty:
        return data_problems(station_code)

    if optimize and len(data_df) > 1100:
        data_df = data_df.iloc[-1100:]

    contains_none_values = False
    if data_df.isnull().values.any():
        contains_none_values = True
        station_locations_rec = sql_client.get_latitude_and_longitude()
        station_clusters_df = Cluster(station_locations_rec).get_stations_clusters_df()

        data_df = DataFiller(data_df, station_clusters_df, station_code, time_handler,
                             sql_client, station_locations_rec, use_second_data_type).fill_data_none_values(value)

    if data_df.isnull().values.any():
        return data_still_has_none_values(station_code)

    if use_fk:
        filtered_values_list = KF_1D(DataHandler.get_list_of_dataframe_values(data_df.values)).get_filtered_values()
        data_df["Measurements"] = filtered_values_list

    data_df.sort_index(inplace=True)

    model = Forecasting_Model(model_name, data_df, steps, station_code, optimize)

    forecast = model.get_forecast()
    data_points = model.data_points_to_use
    model_order = model.best_model_order

    results_dict = dict()
    response_json = dict()

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
        results_dict["Kalman Filter: "] = use_fk
        forecast_dict = time_handler.get_forecast_dict_with_datetime(forecast, data_df.index[-1])
        results_dict["Forecast: "] = forecast_dict
    else:
        results_dict["{} results: ".format(model_name)] = "{} model was not created".format(model_name)

    response_json[station_code] = results_dict

    return response_json


@app.route("/get/forecast/all_models", methods=["GET"])
def get_forecast_all_models():
    sql_client = MySQLClient("xxx.xxx.xxx.xxx", "login", "pwd", "dbname")
    value = request.args["value"]
    station_code = request.args["station"]
    steps = int(request.args["steps"])
    datetime_unit_of_measure = request.args["datetime_unit_of_measure"]
    period_value = int(request.args["period_value"])

    try:
        use_fk = request.args["use_Kalman_Filter"] in ["True", "true"]
    except:
        use_fk = False

    try:
        use_second_data_type = request.args["use_second_data_type"] in ["True", "true"]
    except:
        use_second_data_type = False

    try:
        optimize = request.args["optimize"] in ["True", "true"]
    except:
        optimize = True

    try:
        # YYYY-MM-DD ---> YYYY-MM-DD HH:MM:SS
        date_from = request.args["date_from"].replace("_", " ")
        date_till = request.args["date_till"].replace("_", " ")
    except:
        date_from = None
        date_till = None

    records = sql_client.get_info_by_station(station_code)

    list_of_measurements = DataHandler.get_filled_list_of_measurements(records, value)
    list_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

    # if optimize:
    #     if len(list_of_measurements) > 1000:
    #         list_of_measurements = list_of_measurements[-1000:]
    #         list_of_datetime = list_of_datetime[-1000:]
    #
    # if len(list_of_measurements) < 100:
    #     return data_is_too_small(station_code)

    time_handler = TimeHandler(datetime_unit_of_measure, period_value, date_from=date_from, date_till=date_till)
    data_df = time_handler.get_datetime_and_measurements_dataframe(list_of_datetime, list_of_measurements)
    data_df = data_df[~data_df.index.duplicated(keep='first')]

    if data_df.empty:
        return data_problems(station_code)

    if optimize and len(data_df) > 1100:
        data_df = data_df.iloc[-1100:]

    contains_none_values = False
    if data_df.isnull().values.any():
        contains_none_values = True
        station_locations_rec = sql_client.get_latitude_and_longitude()
        station_clusters_df = Cluster(station_locations_rec).get_stations_clusters_df()

        data_df = DataFiller(data_df, station_clusters_df, station_code, time_handler,
                             sql_client, station_locations_rec, use_second_data_type).fill_data_none_values(value)

    if data_df.isnull().values.any():
        return data_still_has_none_values(station_code)

    if use_fk:
        filtered_values_list = KF_1D(DataHandler.get_list_of_dataframe_values(data_df.values)).get_filtered_values()
        data_df["Measurements"] = filtered_values_list

    data_df.sort_index(inplace=True)

    arima_model = Forecasting_Model("ARIMA", data_df, steps, station_code, optimize)
    forecast_arima = arima_model.get_forecast()
    arima_data_points = arima_model.data_points_to_use
    arima_model_order = arima_model.best_model_order

    arma_model = Forecasting_Model("ARMA", data_df, steps, station_code, optimize)
    forecast_arma = arma_model.get_forecast()
    arma_data_points = arma_model.data_points_to_use
    arma_model_order = arma_model.best_model_order

    ar_model = Forecasting_Model("AR", data_df, steps, station_code, optimize)
    forecast_ar = ar_model.get_forecast()
    ar_data_points = ar_model.data_points_to_use
    ar_model_order = ar_model.best_model_order

    ma_model = Forecasting_Model("MA", data_df, steps, station_code, optimize)
    forecast_ma = ma_model.get_forecast()
    ma_data_points = ma_model.data_points_to_use
    ma_model_order = ma_model.best_model_order

    results_dict = dict()
    response_json = dict()

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

    response_json["Kalman Filter: "] = use_fk
    response_json[station_code] = results_dict

    return response_json


@app.route("/get/flights/by_airports", methods=["GET"])
def get_flights_forecast():
    login = request.args["login"]
    password = request.args["password"]
    departure = request.args["departure"]
    arrival = request.args["arrival"]

    try:
        preferred_date = request.args["preferred_date"]
        preferred_time_of_day = request.args["preferred_time_of_day"]
    except:
        preferred_date = None
        preferred_time_of_day = None

    flights_data = Flights(login, password)

    response_json = {"From: ": departure, "To: ": arrival}

    if preferred_date is not None:
        response_json["Preferred date"] = preferred_date
    if preferred_time_of_day is not None:
        response_json["Preferred time of day"] = preferred_time_of_day

    df_forecast_in_utc, data_info = flights_data.get_flights_forecast(departure, arrival, preferred_date,
                                                                      preferred_time_of_day)
    if not df_forecast_in_utc.empty:

        df_forecast_in_time_of_departure = flights_data.get_forecast_df_in_time_of_departure(df_forecast_in_utc)

        df_forecast_in_utc = flights_data.get_df_with_str_instead_of_datetime(df_forecast_in_utc)
        df_forecast_in_time_of_departure = flights_data.get_df_with_str_instead_of_datetime(
            df_forecast_in_time_of_departure)

        df_forecast_in_utc.reset_index(inplace=True, drop=True)
        df_forecast_in_time_of_departure.reset_index(inplace=True, drop=True)

        forecast_in_utc = df_forecast_in_utc.to_dict("index")
        forecast_in_time_of_departure = df_forecast_in_time_of_departure.to_dict("index")

        result_in_utc = {}
        result_in_time_of_departure = {}
        add_info = {}

        if len(forecast_in_utc) > 5:
            for index, flight_forecast in forecast_in_utc.items():
                if index == 5:
                    break
                flight_number = flight_forecast["flight_number"]
                dep = flight_forecast["departure"]
                arr = flight_forecast["arrival"]
                result_in_utc[index + 1] = flight_number + ":   " + dep + "  -  " + arr

                add_info[flight_number] = data_info[flight_number]

            for index, flight_forecast in forecast_in_time_of_departure.items():
                if index == 5:
                    break
                flight_number = flight_forecast["flight_number"]
                dep = flight_forecast["departure"]
                arr = flight_forecast["arrival"]
                result_in_time_of_departure[index + 1] = flight_number + ":   " + dep + "  -  " + arr
        elif 5 > len(forecast_in_utc) > 0:
            for index, flight_forecast in forecast_in_utc.items():
                flight_number = flight_forecast["flight_number"]
                dep = flight_forecast["departure"]
                arr = flight_forecast["arrival"]
                result_in_utc[index + 1] = flight_number + ":   " + dep + "  -  " + arr

                add_info[flight_number] = data_info[flight_number]

            for index, flight_forecast in forecast_in_time_of_departure.items():
                flight_number = flight_forecast["flight_number"]
                dep = flight_forecast["departure"]
                arr = flight_forecast["arrival"]
                result_in_time_of_departure[index + 1] = flight_number + ":   " + dep + "  -  " + arr

        response_json["Most recent flights in UTC: "] = result_in_utc
        response_json["Most recent flights in time of departure airport: "] = result_in_time_of_departure
        response_json["Additional information"] = add_info

        return response_json
    else:
        response_json["Error"] = "In the current moment there is no flights in this direction"

        return response_json


@app.route("/get/test", methods=["GET"])
def get_test():
    date_from = request.args["date_from"]
    date_till = request.args["date_till"]
    try:
        use_second_data_type = request.args["use_second_data_type"] in ["True", "true"]
    except:
        use_second_data_type = False
    test = Test(date_from, date_till, use_second_data_type)
    result = test.make_test()
    return result
