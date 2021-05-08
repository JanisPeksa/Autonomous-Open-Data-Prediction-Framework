from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error
from math import sqrt

import warnings

warnings.filterwarnings('ignore')


class Forecasting_Model:

    def __init__(self, model_name, data_df, steps: int, station_code: str, max_p_value=6, max_q_value=6,
                 optimize: bool = True):

        self.model_name = model_name
        self.data_df = data_df
        self.steps = steps
        self.optimize = optimize

        if len(self.data_df) <= 100:
            raise Exception("Data must contains more than 200 measurements")

        self.station_code = station_code

        self.min_aic_value = None
        self.data_points_to_use = None
        self.best_model_order = None

        # range (0, 3) == [ 0, 1, 2 ]
        if model_name == "ARIMA":
            self.d_values = range(0, 3)
            self.p_values = range(0, max_p_value)
            self.q_values = range(0, max_q_value)
        elif model_name == "ARMA":
            self.d_values = range(0, 1)
            self.p_values = range(0, max_p_value)
            self.q_values = range(0, max_q_value)
        elif model_name == "AR":
            self.d_values = range(0, 1)
            self.q_values = range(0, 1)
            self.p_values = range(0, max_p_value)
        elif model_name == "MA":
            self.d_values = range(0, 1)
            self.p_values = range(0, 1)
            self.q_values = range(0, max_q_value)
        elif model_name == "SARIMA":
            self.D_values = range(0, 3)
            self.P_values = range(0, 4)
            self.Q_values = range(0, 4)
            self.d_values = range(0, 3)
            self.p_values = range(0, 4)
            self.q_values = range(0, 4)
        else:
            raise Exception("The model name {} is incorrect".format(model_name))

    def get_d_value_and_ADF_test(self, data_df):

        # ----- Augmented Dickey-Fuller test ----- #
        # ----- p-value > 0.05: the data has a unit root and is non-stationary ----- #
        # ----- p-value <= 0.05: the data does not have a unit root and is stationary ----- #
        # ----- The more negative is ADF Statistic, the more likely we have a stationary dataset ----- #

        d = 0
        try:
            adf_test_results = adfuller(data_df.values)
        except:
            return d

        data_df_diff = data_df
        while adf_test_results[1] > 0.05 or d == 0:
            if d > 2:
                return 0
            # ----- make data stationary and drop NA values ----- #
            data_df_diff = data_df_diff.diff().dropna()
            d += 1

            try:
                data_df_diff_values = data_df_diff.values
                adf_test_results = adfuller(data_df_diff_values)
            except:
                d -= 1
                return d

        return d

    def get_order_and_min_aic_value(self, data_df):
        aic_dict = dict()

        if len(self.d_values) != 1:
            d = self.get_d_value_and_ADF_test(data_df)
        else:
            d = 0

        for p in self.p_values:
            for q in self.q_values:
                order = (p, d, q)

                if order == (0, 0, 0):
                    continue

                try:
                    arima_model = ARIMA(data_df, order).fit(disp=False)
                    aic = arima_model.aic
                    aic_dict[order] = aic
                    # print("Data Points: {}, Order: {}, AIC: {}".format(len(data_df), order, aic))
                except:
                    continue

        # if aic_dict is empty
        # it is impossible to create arima model for this data set
        if len(aic_dict) == 0:
            return None
        else:

            min_aic_val = min(aic_dict.values())

            for key, value in aic_dict.items():
                if value == min_aic_val:
                    result_dict = {key: value}
                    # order = (p, d, q)
                    # {order: aic_value }
                    return result_dict

    def make_forecast(self, data_df):

        model = ARIMA(data_df, order=self.best_model_order).fit(disp=False)
        forecast_list = model.forecast(steps=self.steps)[0].tolist()

        return forecast_list

    @staticmethod
    def get_forecast_accuracy_with_real_data(forecast, actual):
        return sqrt(mean_squared_error(actual, forecast))

    def get_possible_models_for_all_data_points_dict(self) -> dict:
        if self.optimize:
            if len(self.data_df) <= 1000:
                data_optimize_points = len(self.data_df)
                point_range = int(data_optimize_points / 10)
            else:
                data_optimize_points = 1010
                point_range = 100
        else:
            data_optimize_points = len(self.data_df)
            point_range = int(data_optimize_points / 20)

        models_order_and_data_points_dict = dict()
        last_point = len(self.data_df)

        data_point_range = range(200, data_optimize_points, point_range)
        for data_points in data_point_range:
            first_point = last_point - data_points
            if first_point < 0:
                break
            data_df_copy = self.data_df[first_point:last_point].copy()

            order_and_min_aic_value = self.get_order_and_min_aic_value(data_df_copy)
            if order_and_min_aic_value is None:
                continue
            else:
                models_order_and_data_points_dict[data_points] = order_and_min_aic_value

        return models_order_and_data_points_dict

    def get_lowest_aic_value_and_data_points_from_dict(self, models_for_all_data_points_dict: dict):
        for data_points, aic_dict in models_for_all_data_points_dict.items():
            for order, aic in aic_dict.items():
                if self.min_aic_value is None:
                    self.min_aic_value = aic
                    self.data_points_to_use = data_points
                    self.best_model_order = order
                elif aic < self.min_aic_value:
                    self.min_aic_value = aic
                    self.data_points_to_use = data_points
                    self.best_model_order = order
                else:
                    continue

    def get_forecast(self):
        models_for_all_data_points_dict = self.get_possible_models_for_all_data_points_dict()

        self.get_lowest_aic_value_and_data_points_from_dict(models_for_all_data_points_dict)

        if self.data_points_to_use is None:
            return None

        data_df_copy = self.data_df[-self.data_points_to_use:].copy()

        forecast = self.make_forecast(data_df_copy)

        return forecast
