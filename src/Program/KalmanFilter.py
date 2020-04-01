class KalmanFilter:

    def __init__(self, initial_error_in_estimate, __initial_estimate, __error_in_measurement, __measurements):
        self.__measurements = __measurements
        self.__estimate = __initial_estimate
        self.__error_in_estimate = initial_error_in_estimate
        self.__error_in_measurement = __error_in_measurement
        self.__measurement = None
        self.__kalman_gain = None

    def __calculate_kalman_gain(self) -> float:
        return self.__error_in_estimate / (self.__error_in_estimate + self.__error_in_measurement)

    def __calculate_estimate(self) -> float:
        return self.__estimate + self.__kalman_gain * (self.__measurement - self.__estimate)

    def __calculate_error_in_estimate(self) -> float:
        return (1 - self.__kalman_gain) * self.__error_in_estimate

    def make_basic_calculations(self):
        self.__kalman_gain = self.__calculate_kalman_gain()
        self.__estimate = self.__calculate_estimate()
        self.__error_in_estimate = self.__calculate_error_in_estimate()

    def get_estimates(self) -> list:
        list_of_estimates = []

        for measurement in self.__measurements:
            self.__measurement = measurement
            self.make_basic_calculations()
            list_of_estimates.append(self.__estimate)

        return list_of_estimates

    @staticmethod
    def __get_initial_estimate(measurements: list) -> float:
        return measurements[-1] + (
                measurements[-1] - measurements[-2])

    @staticmethod
    def get_lists_of_estimates(lists_of_measurements: list, error_in_estimate: float,
                               error_in_measurement: float) -> list:
        lists_of_estimates = []

        for measurements in lists_of_measurements:
            initial_estimate = KalmanFilter.__get_initial_estimate(measurements)
            kf = KalmanFilter(error_in_estimate, initial_estimate, error_in_measurement, measurements)
            lists_of_estimates.append(kf.get_estimates())

        return lists_of_estimates
