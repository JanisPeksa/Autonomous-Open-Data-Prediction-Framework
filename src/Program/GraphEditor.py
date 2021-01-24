from matplotlib import pyplot as plt


class GraphEditor:
    index = 0

    def __init__(self, estimates: list, measurements: list, value: str, station_name: str, period: str, accuracy=None):
        self.estimates = estimates
        self.measurements = measurements
        self.value = value
        self.station_name = station_name
        self.period = period
        self.accuracy = accuracy
        self.plt = None

    def create_est_and_meas_plot(self):
        plt.plot(self.estimates, label='estimates', color='blue')
        plt.plot(self.measurements, label='measurements', color='orange')
        plt.title(self.station_name + ', Period: ' + self.period)
        plt.ylabel(self.value)
        plt.xlabel('Observations')
        plt.legend()
        self.plt = plt

    def create_est_plot(self):
        plt.plot(self.estimates, color='blue')
        plt.title('Estimates: ' + self.station_name + ', Period: ' + self.period)
        plt.ylabel(self.value)
        plt.xlabel('Observations')
        self.plt = plt

    def create_meas_plot(self):
        plt.plot(self.measurements, color='orange')
        plt.title('Measurements: ' + self.station_name + ', Period: ' + self.period)
        plt.ylabel(self.value)
        plt.xlabel('Observations')
        self.plt = plt

    def show_plot(self):
        self.plt.show()

    def save_plot(self):
        self.plt.savefig('Plot{}.png'.format(GraphEditor.index), dpi=300)
        GraphEditor.index += 1

    def create_accuracy_bar_plot(self):
        plt.bar(self.accuracy, label='accuracy', color='blue')
        plt.xlabel('Observations')
        plt.ylabel('Accuracy %')
        plt.title(self.value + ' Accuracy, ' + 'Period: ' + self.period)
        plt.legend()
        self.plt = plt

    @staticmethod
    def create_twolined_plot(lists_of_estimates: list, lists_of_measurements: list, value: str):
        __list_of_estimates = []
        __list_of_measurements = []

        for estimates, measurements in zip(lists_of_estimates, lists_of_measurements):
            for estimate in estimates:
                __list_of_estimates.append(estimate)

            for measurement in measurements:
                __list_of_measurements.append(measurement)
        else:
            plt.plot(__list_of_measurements, label='measurements', color='red')
            plt.plot(__list_of_estimates, label='estimates', color='green')
            plt.title('Twolined plot, ' + value)
            plt.legend()
            plt.show()

    @staticmethod
    def create_multilined_plot(lists_of_estimates: list, lists_of_measurements: list, value: str):
        for estimates, measurements in zip(lists_of_estimates, lists_of_measurements):
            plt.plot(estimates, color='green')
            plt.plot(measurements, color='red')
        else:
            plt.title('Multilined plot, ' + value)
            plt.show()

    @staticmethod
    def save_created_plots(lists_of_estimates: list, lists_of_measurements: list, station_names: list,
                           value: str):
        # TODO
        pass
