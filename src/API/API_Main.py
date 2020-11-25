from flask import request
from flask_api import FlaskAPI
import pandas as pd

from Program.DataHandler import DataHandler
from Program.KalmanFilter import KalmanFilter
from Program.KF import KF_1D, KF_2D
from Program.MySQLClient import MySQLClient
from Program.Forecasting_model import Forecasting_model

app = FlaskAPI(__name__)


@app.route('/get/', methods=['GET'])
def get_basic():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    for x in request.args.keys():
        if x == 'value' and request.args['value'] != 'Station':
            return DataHandler.get_json_of_chosen_values(
                DataHandler.get_lists_of_chosen_values_with_station_names(sql_client.get_all_info_from_database(),
                                                                          request.args['value']))
        elif x == 'list' and request.args['list'] == 'all':
            return DataHandler.get_json_of_existing_values()
        elif (x == 'value' and request.args['value'] == 'Station') or \
                (x == 'list' and request.args['list'] == 'Station'):
            return DataHandler.get_json_of_station_names()
        elif x == 'measment':
            pass


@app.route('/get/accuracies', methods=['GET'])
def get_accuracies():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    value = request.args['value']
    station_codes = request.args['stations'].split(',')

    records = sql_client.get_info_by_stations(station_codes)

    index = DataHandler.get_index_of_value(value)

    lists_of_measurements = DataHandler.get_exact_value_from_many_my_sql_records(records, index)
    lists_of_measurements = DataHandler.get_lists_of_floats(lists_of_measurements)

    error_in_estimate = 1.0
    error_in_measurement = 1.0

    lists_of_measurements = DataHandler.replace_none_with_dash(lists_of_measurements)
    lists_of_measurements = DataHandler.fill_missing_data_in_lists(lists_of_measurements)

    lists_of_estimates = KalmanFilter.get_lists_of_estimates(lists_of_measurements, error_in_estimate,
                                                             error_in_measurement)

    accuracies = DataHandler.get_accuracies(lists_of_measurements, lists_of_estimates)
    json = {}

    for station_code, accuracy in zip(station_codes, accuracies):
        json[station_code] = 'Accuracy: ' + str(accuracy)

    return json


@app.route('/get/estimates', methods=['GET'])
def get_estimates():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    value = request.args['value']
    station_codes = request.args['stations'].split(',')

    records = sql_client.get_info_by_stations(station_codes)

    index = DataHandler.get_index_of_value(value)

    lists_of_measurements = DataHandler.get_exact_value_from_many_my_sql_records(records, index)
    lists_of_measurements = DataHandler.get_lists_of_floats(lists_of_measurements)

    error_in_estimate = 1.0
    error_in_measurement = 1.0

    lists_of_measurements = DataHandler.replace_none_with_dash(lists_of_measurements)
    lists_of_measurements = DataHandler.fill_missing_data_in_lists(lists_of_measurements)

    lists_of_estimates = KalmanFilter.get_lists_of_estimates(lists_of_measurements, error_in_estimate,
                                                             error_in_measurement)

    data_dict = {}
    json = {}

    for station_code, measurements, estimates in zip(station_codes, lists_of_measurements, lists_of_estimates):
        try:
            if request.args['measurements'] == 'true':
                data_dict['Measurements: '] = measurements
        except KeyError:
            pass

        data_dict['Estimates: '] = estimates

        json[station_code] = data_dict
        data_dict = {}

    return json


# overload for taking all estimates
@app.route('/get/estimates/all', methods=['GET'])
def get_all_estimations():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    value = request.args['value']

    records = sql_client.get_all_info_by_stations()
    index = DataHandler.get_index_of_value(value)

    lists_of_measurements = DataHandler.get_exact_value_from_many_my_sql_records(records, index)
    lists_of_measurements = DataHandler.get_lists_of_floats(lists_of_measurements)

    error_in_estimate = 1.0
    error_in_measurement = 1.0

    lists_of_measurements = DataHandler.replace_none_with_dash(lists_of_measurements)
    lists_of_measurements = DataHandler.fill_missing_data_in_lists(lists_of_measurements)

    station_codes = DataHandler.get_station_codes()

    station_codes, lists_of_measurements = DataHandler.zip_codes_and_measurements(station_codes, lists_of_measurements)

    lists_of_estimates = KalmanFilter.get_lists_of_estimates(lists_of_measurements, error_in_estimate,
                                                             error_in_measurement)
    data_dict = {}
    json = {}

    for station_code, measurements, estimates in zip(station_codes, lists_of_measurements, lists_of_estimates):
        try:
            if request.args['measurements'] == 'true':
                data_dict['Measurements: '] = measurements
        except KeyError:
            pass

        data_dict['Estimates: '] = estimates

        json[station_code] = data_dict
        data_dict = {}

    return json


@app.route('/use/1d_kalman_filter', methods=['GET'])
def get_filtered_values_using_1d_kalman_filter():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    value = request.args['value']
    station_code = request.args['station']

    records = sql_client.get_info_by_station(station_code)

    index = DataHandler.get_index_of_value(value)

    list_of_measurements = DataHandler.get_exact_value_from_my_sql_records(records, index)
    list_of_measurements = DataHandler.get_list_of_floats(list_of_measurements)

    list_of_measurements = DataHandler.replace_in_list_none_with_dash(list_of_measurements)
    list_of_measurements = DataHandler.fill_missing_data_in_lists([list_of_measurements])[0]

    filtered_values = KF_1D(list_of_measurements).get_filtered_values()

    results_dict = dict()
    json = dict()

    results_dict['Filtered values using 1D Kalman Filter: '] = filtered_values

    json[station_code] = results_dict

    return json


@app.route('/use/2d_kalman_filter', methods=['GET'])
def get_filtered_values_using_2d_kalman_filter():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    value = request.args['value']
    station_code = request.args['station']
    try:
        position = float(request.args['position'])
    except KeyError:
        position = 0
    try:
        velocity = float(request.args['velocity'])
    except KeyError:
        velocity = 0
    try:
        time_delta = float(request.args['time_delta'])
    except KeyError:
        time_delta = 0.1

    records = sql_client.get_info_by_station(station_code)

    index = DataHandler.get_index_of_value(value)

    list_of_measurements = DataHandler.get_exact_value_from_my_sql_records(records, index)
    list_of_measurements = DataHandler.get_list_of_floats(list_of_measurements)

    list_of_measurements = DataHandler.replace_in_list_none_with_dash(list_of_measurements)
    list_of_measurements = DataHandler.fill_missing_data_in_lists([list_of_measurements])[0]

    filtered_values = KF_2D(list_of_measurements, position=position, velocity=velocity,
                            time_delta=time_delta).get_filtered_values()

    results_dict = dict()
    json = dict()

    results_dict['Filtered values using 2D Kalman Filter: '] = filtered_values

    json[station_code] = results_dict

    return json


@app.route('/get/forecast/arima', methods=['GET'])
def get_forecast_arima():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    value = request.args['value']
    station_code = request.args['station']
    steps = int(request.args['steps'])
    try:
        optimize = request.args['optimize'] in ('true', 'True')
    except KeyError:
        optimize = True

    records = sql_client.get_info_by_station(station_code)

    index = DataHandler.get_index_of_value(value)

    list_of_measurements = DataHandler.get_exact_value_from_my_sql_records(records, index)
    list_of_measurements = DataHandler.get_list_of_floats(list_of_measurements)

    list_of_measurements = DataHandler.replace_in_list_none_with_dash(list_of_measurements)
    list_of_measurements = DataHandler.fill_missing_data_in_lists([list_of_measurements])[0]

    series_of_measurements = pd.Series(list_of_measurements)

    arima_data_points, arima_model_order, forecast_arima = Forecasting_model("ARIMA", series_of_measurements, steps,
                                                                             optimize).get_forecast()

    results_dict = dict()
    json = dict()

    if forecast_arima is not None:
        p, d, q = arima_model_order

        arima_model_order = {'p: ': p,
                             'd: ': d,
                             'q: ': q}

        results_dict['Data points: '] = arima_data_points
        results_dict['ARIMA model order: '] = arima_model_order
        results_dict['Steps: '] = steps
        results_dict['Forecast: '] = forecast_arima
    else:
        results_dict['ARIMA results: '] = 'ARIMA model was not created'

    json[station_code] = results_dict

    return json


@app.route('/get/forecast/arima/time_period', methods=['GET'])
def get_forecast_arima_by_time_period():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    value = request.args['value']
    station_code = request.args['station']
    steps = int(request.args['steps'])
    try:
        optimize = request.args['optimize'] in ('true', 'True')
    except KeyError:
        optimize = True

    # YYYY-MM-DD ---> YYYY-MM-DD HH:MM:SS
    date_from = request.args['date_from'].replace('_', ' ')
    date_till = request.args['date_till'].replace('_', ' ')

    if len(date_from) == 10:
        date_from += ' 00:00:00'
    else:
        date_from += ':00'

    if len(date_till) == 10:
        date_till += ' 00:00:00'
    else:
        date_till += ':00'

    date_from = DataHandler.get_datetime_format(date_from)
    date_till = DataHandler.get_datetime_format(date_till)

    records = sql_client.get_info_by_station(station_code)

    index = DataHandler.get_index_of_value(value)

    list_of_measurements = DataHandler.get_exact_value_from_my_sql_records(records, index)
    list_of_measurements = DataHandler.get_list_of_floats(list_of_measurements)

    list_of_measurements = DataHandler.replace_in_list_none_with_dash(list_of_measurements)
    list_of_measurements = DataHandler.fill_missing_data_in_lists([list_of_measurements])[0]

    lists_of_datetime = DataHandler.get_exact_value_from_many_my_sql_records([records], 2)[0]

    data_df = DataHandler.get_datetime_and_measurements_dataframe(lists_of_datetime, list_of_measurements,
                                                                  date_from, date_till)

    arima_data_points, arima_model_order, forecast_arima = Forecasting_model("ARIMA", data_df, steps,
                                                                             optimize).get_forecast()

    results_dict = dict()
    json = dict()
    if forecast_arima is not None:
        p, d, q = arima_model_order

        arima_model_order = {'p: ': p,
                             'd: ': d,
                             'q: ': q}

        results_dict['Data points: '] = arima_data_points
        results_dict['Date from: '] = date_from
        results_dict['Date till: '] = date_till
        results_dict['ARIMA model order: '] = arima_model_order
        results_dict['Steps: '] = steps
        results_dict['Forecast: '] = forecast_arima
    else:
        results_dict['ARIMA results: '] = 'ARIMA model was not created'

    json[station_code] = results_dict

    return json


@app.route('/get/forecast/ar', methods=['GET'])
def get_forecast_ar():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    value = request.args['value']
    station_code = request.args['station']
    steps = int(request.args['steps'])
    try:
        optimize = request.args['optimize'] in ('true', 'True')
    except KeyError:
        optimize = True

    records = sql_client.get_info_by_station(station_code)

    index = DataHandler.get_index_of_value(value)

    list_of_measurements = DataHandler.get_exact_value_from_my_sql_records(records, index)
    list_of_measurements = DataHandler.get_list_of_floats(list_of_measurements)

    list_of_measurements = DataHandler.replace_in_list_none_with_dash(list_of_measurements)
    list_of_measurements = DataHandler.fill_missing_data_in_lists([list_of_measurements])[0]

    series_of_measurements = pd.Series(list_of_measurements)

    ar_data_points, ar_model_order, forecast_ar = Forecasting_model("AR", series_of_measurements, steps,
                                                                    optimize).get_forecast()

    results_dict = dict()
    json = dict()

    if forecast_ar is not None:
        p, d, q = ar_model_order

        ar_model_order = {'p: ': p}

        results_dict['Data points: '] = ar_data_points
        results_dict['AR model order: '] = ar_model_order
        results_dict['Steps: '] = steps
        results_dict['Forecast: '] = forecast_ar
    else:
        results_dict['AR results: '] = 'AR model was not created'

    json[station_code] = results_dict

    return json


@app.route('/get/forecast/ma', methods=['GET'])
def get_forecast_ma():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    value = request.args['value']
    station_code = request.args['station']
    steps = int(request.args['steps'])
    try:
        optimize = request.args['optimize'] in ('true', 'True')
    except KeyError:
        optimize = True

    records = sql_client.get_info_by_station(station_code)

    index = DataHandler.get_index_of_value(value)

    list_of_measurements = DataHandler.get_exact_value_from_my_sql_records(records, index)
    list_of_measurements = DataHandler.get_list_of_floats(list_of_measurements)

    list_of_measurements = DataHandler.replace_in_list_none_with_dash(list_of_measurements)
    list_of_measurements = DataHandler.fill_missing_data_in_lists([list_of_measurements])[0]

    series_of_measurements = pd.Series(list_of_measurements)

    ma_data_points, ma_model_order, forecast_ma = Forecasting_model("MA", series_of_measurements, steps,
                                                                    optimize).get_forecast()

    results_dict = dict()
    json = dict()

    if forecast_ma is not None:
        p, d, q = ma_model_order

        ma_model_order = {'q: ': q}

        results_dict['Data points: '] = ma_data_points
        results_dict['MA model order: '] = ma_model_order
        results_dict['Steps: '] = steps
        results_dict['Forecast: '] = forecast_ma
    else:
        results_dict['MA results: '] = 'MA model was not created'

    json[station_code] = results_dict

    return json


@app.route('/get/forecast/arma', methods=['GET'])
def get_forecast_arma():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    value = request.args['value']
    station_code = request.args['station']
    steps = int(request.args['steps'])
    try:
        optimize = request.args['optimize'] in ('true', 'True')
    except KeyError:
        optimize = True

    records = sql_client.get_info_by_station(station_code)

    index = DataHandler.get_index_of_value(value)

    list_of_measurements = DataHandler.get_exact_value_from_my_sql_records(records, index)
    list_of_measurements = DataHandler.get_list_of_floats(list_of_measurements)

    list_of_measurements = DataHandler.replace_in_list_none_with_dash(list_of_measurements)
    list_of_measurements = DataHandler.fill_missing_data_in_lists([list_of_measurements])[0]

    series_of_measurements = pd.Series(list_of_measurements)

    arma_data_points, arma_model_order, forecast_arma = Forecasting_model("ARMA", series_of_measurements, steps,
                                                                          optimize).get_forecast()

    results_dict = dict()
    json = dict()

    if forecast_arma is not None:
        p, d, q = arma_model_order

        arma_model_order = {'p: ': p,
                            'q: ': q}

        results_dict['Data points: '] = arma_data_points
        results_dict['ARMA model order: '] = arma_model_order
        results_dict['Steps: '] = steps
        results_dict['Forecast: '] = forecast_arma
    else:
        results_dict['ARMA results: '] = 'ARMA model was not created'

    json[station_code] = results_dict

    return json


@app.route('/get/forecast/all_models', methods=['GET'])
def get_forecast_all_models():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    value = request.args['value']
    station_code = request.args['station']
    steps = int(request.args['steps'])
    try:
        optimize = request.args['optimize'] in ('true', 'True')
    except KeyError:
        optimize = True

    records = sql_client.get_info_by_station(station_code)

    index = DataHandler.get_index_of_value(value)

    list_of_measurements = DataHandler.get_exact_value_from_my_sql_records(records, index)
    list_of_measurements = DataHandler.get_list_of_floats(list_of_measurements)

    list_of_measurements = DataHandler.replace_in_list_none_with_dash(list_of_measurements)
    list_of_measurements = DataHandler.fill_missing_data_in_lists([list_of_measurements])[0]

    series_of_measurements = pd.Series(list_of_measurements)

    arima_data_points, arima_model_order, forecast_arima = Forecasting_model("ARIMA", series_of_measurements, steps,
                                                                             optimize).get_forecast()

    arma_data_points, arma_model_order, forecast_arma = Forecasting_model("ARMA", series_of_measurements, steps,
                                                                          optimize).get_forecast()

    ar_data_points, ar_model_order, forecast_ar = Forecasting_model("AR", series_of_measurements, steps,
                                                                    optimize).get_forecast()

    ma_data_points, ma_model_order, forecast_ma = Forecasting_model("MA", series_of_measurements, steps,
                                                                    optimize).get_forecast()

    results_dict = dict()
    json = dict()

    # ARIMA results
    if forecast_arima is not None:
        p, d, q = arima_model_order
        arima_model_order = {'p: ': p,
                             'd: ': d,
                             'q: ': q}

        results_dict['Data points for ARIMA: '] = arima_data_points
        results_dict['ARIMA model order: '] = arima_model_order
        results_dict['Steps: '] = steps
        results_dict['ARIMA forecast: '] = forecast_arima
    else:
        results_dict['ARIMA results: '] = 'ARIMA model was not created'

    # ARMA results
    if forecast_arma is not None:
        p, d, q = arma_model_order
        arma_model_order = {'p: ': p,
                            'q: ': q}

        results_dict['Data points for ARMA: '] = arma_data_points
        results_dict['ARMA model order: '] = arma_model_order
        results_dict['Steps: '] = steps
        results_dict['ARMA forecast: '] = forecast_arma
    else:
        results_dict['ARMA results: '] = 'ARMA model was not created'

    # AR results
    if forecast_ar is not None:
        p, d, q = ar_model_order
        ar_model_order = {'p: ': p}

        results_dict['Data points for AR: '] = ar_data_points
        results_dict['AR model order: '] = ar_model_order
        results_dict['Steps: '] = steps
        results_dict['AR forecast: '] = forecast_ar
    else:
        results_dict['AR results: '] = 'AR model was not created'

    # MA results
    if forecast_ma is not None:
        p, d, q = ma_model_order
        ma_model_order = {'q: ': q}

        results_dict['Data points for MA: '] = ma_data_points
        results_dict['MA model order: '] = ma_model_order
        results_dict['Steps: '] = steps
        results_dict['MA forecast: '] = forecast_ma
    else:
        results_dict['MA results: '] = 'MA model was not created'

    json[station_code] = results_dict

    return json


@app.route('/get/forecast/all_models/with/1d_kalman_filter', methods=['GET'])
def get_forecast_all_models_with_1d_kalman_filter():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxxxx', 'xxxxx', 'xxxxxx')
    value = request.args['value']
    station_code = request.args['station']
    steps = int(request.args['steps'])
    try:
        optimize = request.args['optimize'] in ('true', 'True')
    except KeyError:
        optimize = True

    records = sql_client.get_info_by_station(station_code)

    index = DataHandler.get_index_of_value(value)

    list_of_measurements = DataHandler.get_exact_value_from_my_sql_records(records, index)
    list_of_measurements = DataHandler.get_list_of_floats(list_of_measurements)

    list_of_measurements = DataHandler.replace_in_list_none_with_dash(list_of_measurements)
    list_of_measurements = DataHandler.fill_missing_data_in_lists([list_of_measurements])[0]

    filtered_values = KF_1D(list_of_measurements).get_filtered_values()

    series_of_measurements = pd.Series(filtered_values)

    arima_data_points, arima_model_order, forecast_arima = Forecasting_model("ARIMA", series_of_measurements, steps,
                                                                             optimize).get_forecast()

    arma_data_points, arma_model_order, forecast_arma = Forecasting_model("ARMA", series_of_measurements, steps,
                                                                          optimize).get_forecast()

    ar_data_points, ar_model_order, forecast_ar = Forecasting_model("AR", series_of_measurements, steps,
                                                                    optimize).get_forecast()

    ma_data_points, ma_model_order, forecast_ma = Forecasting_model("MA", series_of_measurements, steps,
                                                                    optimize).get_forecast()

    results_dict = dict()
    json = dict()

    # ARIMA results
    if forecast_arima is not None:
        p, d, q = arima_model_order
        arima_model_order = {'p: ': p,
                             'd: ': d,
                             'q: ': q}

        results_dict['Data points for ARIMA: '] = arima_data_points
        results_dict['ARIMA model order: '] = arima_model_order
        results_dict['Steps: '] = steps
        results_dict['ARIMA forecast: '] = forecast_arima
    else:
        results_dict['ARIMA results: '] = 'ARIMA model was not created'

    # ARMA results
    if forecast_arma is not None:
        p, d, q = arma_model_order
        arma_model_order = {'p: ': p,
                            'q: ': q}

        results_dict['Data points for ARMA: '] = arma_model_order
        results_dict['ARMA model order: '] = arma_model_order
        results_dict['Steps: '] = steps
        results_dict['ARMA forecast: '] = forecast_arma
    else:
        results_dict['ARMA results: '] = 'ARMA model was not created'

    # AR results
    if forecast_ar is not None:
        p, d, q = ar_model_order
        ar_model_order = {'p: ': p}

        results_dict['Data points for AR: '] = ar_model_order
        results_dict['AR model order: '] = ar_model_order
        results_dict['Steps: '] = steps
        results_dict['AR forecast: '] = forecast_ar
    else:
        results_dict['AR results: '] = 'AR model was not created'

    # MA results
    if forecast_ma is not None:
        p, d, q = ma_model_order
        ma_model_order = {'q: ': q}

        results_dict['Data points for MA: '] = ma_model_order
        results_dict['MA model order: '] = ma_model_order
        results_dict['Steps: '] = steps
        results_dict['MA forecast: '] = forecast_ma
    else:
        results_dict['MA results: '] = 'MA model was not created'

    json[station_code] = results_dict

    return json
