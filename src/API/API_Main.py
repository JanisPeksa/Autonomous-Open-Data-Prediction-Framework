from flask import request
from flask_api import FlaskAPI
from Program.DataHandler import DataHandler
from Program.KalmanFilter import KalmanFilter
from Program.MySQLClient import MySQLClient

app = FlaskAPI(__name__)


@app.route('/get/', methods=['GET'])
def get_basic():
    for x in request.args.keys():
        if x == 'value' and request.args['value'] != 'Station':
            return DataHandler.get_json_of_chosen_values(
                DataHandler.get_lists_of_chosen_values(db_client.get_all_info_from_main_database(),
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
