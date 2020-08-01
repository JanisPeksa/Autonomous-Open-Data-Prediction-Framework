from flask import request
from flask_api import FlaskAPI
import pandas as pd

from Program.DataHandler import DataHandler
from Program.KalmanFilter import KalmanFilter
from Program.MySQLClient import MySQLClient
from Program.Arima_Main import Arima_Main

app = FlaskAPI(__name__)


@app.route('/get/', methods=['GET'])
def get_basic():
    sql_client = MySQLClient('xxx.xxx.xxx.xxx', 'xxx', 'xxx', 'xxx')
    for x in request.args.keys():
        if x == 'value' and request.args['value'] != 'Station':
            return DataHandler.get_json_of_chosen_values(
                //DataHandler.get_lists_of_chosen_values(db_client.get_all_info_from_main_database(),
                DataHandler.get_lists_of_chosen_values_with_station_names(sql_client.get_all_info_from_database(),
                                                       request.args['value']))
        elif x == 'list' and request.args['list'] == 'all':
            return DataHandler.get_json_of_existing_values()
        elif (x == 'value' and request.args['value'] == 'Station') or (
                x == 'list' and request.args['list'] == 'Station'):
            return DataHandler.get_json_of_station_names()
        elif x == 'measment':
            pass


@app.route('/get/accuracies', methods=['GET'])
def get_accuracies():
    sql_client = MySQLClient('XX.XX.XX.XX', 'xxx', 'xxx', 'xxx')
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
    sql_client = MySQLClient('XX.XX.XX.XX', 'xxx', 'xxx', 'xxx')
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
    sql_client = MySQLClient('XX.XX.XX.XX', 'xxx', 'xxx', 'xxx')
    value = request.args['value']

    print(value)

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


@app.route('/get/forecast/arima', methods=['GET'])
def get_forecast_arima():
    sql_client = MySQLClient('XX.XX.XX.XX', 'xxx', 'xxx', 'xxx')
    value = request.args['value']
    station_code = request.args['station']
    steps = int(request.args['steps'])
    optimize = request.args['optimize'] in ('true', 'True')

    records = sql_client.get_info_by_station(station_code)

    index = DataHandler.get_index_of_value(value)

    list_of_measurements = DataHandler.get_exact_value_from_my_sql_records(records, index)
    list_of_measurements = DataHandler.get_list_of_floats(list_of_measurements)

    list_of_measurements = DataHandler.replace_in_list_none_with_dash(list_of_measurements)
    list_of_measurements = DataHandler.fill_missing_data_in_lists([list_of_measurements])[0]

    series_of_measurements = pd.Series(list_of_measurements)

    data_points_for_forecast, arima_model_order, steps, forecast = Arima_Main(series_of_measurements,
                                                                              steps, optimize).get_arima_forecast()

    results_dict = dict()
    json = dict()

    p, d, q = arima_model_order

    arima_model_order = {'p: ': p,
                         'd: ': d,
                         'q: ': q}

    results_dict['Data points: '] = data_points_for_forecast
    results_dict['ARIMA model order: '] = arima_model_order
    results_dict['Steps: '] = steps
    results_dict['Forecast: '] = forecast

    json[station_code] = results_dict

    return json

@app.route('/get/forecast/arima/time_period', methods=['GET'])
def get_forecast_arima_by_time_period():
    sql_client = MySQLClient('XX.XX.XX.XX', 'xxx', 'xxx', 'xxx')
    value = request.args['value']
    station_code = request.args['station']
    steps = int(request.args['steps'])
    optimize = request.args['optimize'] in ('true', 'True')

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

    data_points_for_forecast, arima_model_order, steps, forecast_list = Arima_Main(data_df, steps, optimize).get_arima_forecast()

    results_dict = dict()
    json = dict()

    p, d, q = arima_model_order

    arima_model_order = {'p: ': p,
                         'd: ': d,
                         'q: ': q}

    results_dict['Data points: '] = data_points_for_forecast
    results_dict['Date from: '] = date_from
    results_dict['Date till: '] = date_till
    results_dict['ARIMA model order: '] = arima_model_order
    results_dict['Steps: '] = steps
    results_dict['Forecast: '] = forecast_list

    json[station_code] = results_dict

    return json
