import json
from datetime import datetime


class FileHandler:

    @staticmethod
    def write_a_set_of_data_to_file(file_name: str, lists_of_measurements: list,
                                    lists_of_estimates: list,
                                    station_names: list, accuracies: dict, mode: str = 'a', encoding: str = 'utf-8'):
        with open(file_name, mode=mode, encoding=encoding) as file:
            file.write(str(datetime.now()) + '\n\n')
            for station_name, measurements, estimates in zip(station_names, lists_of_measurements,
                                                             lists_of_estimates):
                file.write('Station: {}'.format(str(station_name) + '\n'))

                file.write('Measurements: ')
                for measurement in measurements:
                    file.write(str(measurement) + ' , ')
                else:
                    file.write('\n')

                file.write('Estimates: ')
                for estimate in estimates:
                    file.write(str(estimate) + ' , ')
                else:
                    file.write('\n\n')

                file.write('Last estimate: {}\n'.format(estimates[-2]))
                file.write('True value: {}\n'.format(measurements[-1]))
                file.write('Accuracy(RMSE): {}\n\n\n'.format(accuracies[station_name]))
                file.write('<------------------------------------------->\n\n\n')
            else:
                file.write('\n\n\n')

    @staticmethod
    def write_estimations_to_json(value: str, lists_of_estimates: list, station_names: list):
        json_dict = {}

        file_name = value + ' estimations.json'

        for estimates, station_name in zip(lists_of_estimates, station_names):
            json_dict[station_name] = estimates
        else:
            with open(file_name, mode='w', encoding='utf-8') as file:
                json.dump(json_dict, file, indent=4)
