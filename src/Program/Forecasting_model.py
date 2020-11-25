import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error
from math import sqrt

import warnings

warnings.filterwarnings('ignore')


class Forecasting_model:

    def __init__(self, model_name, data_series, steps: int, optimize: bool,
                 max_p_value=6, max_q_value=6):
        self.model_name = model_name
        self.data_series = data_series
        self.steps = steps
        self.optimize = optimize

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
        else:
            self.model_name = "Not defined"

    def get_d_value_and_ADF_test(self):

        # ----- Augmented Dickey-Fuller test ----- #
        # ----- p-value > 0.05: the data has a unit root and is non-stationary ----- #
        # ----- p-value <= 0.05: the data does not have a unit root and is stationary ----- #
        # ----- The more negative is ADF Statistic, the more likely we have a stationary dataset ----- #

        d = 0
        try:
            adf_test_results = adfuller(self.data_series.values)
        except:
            return d

        data_series_diff = self.data_series
        while adf_test_results[1] > 0.05 or d == 0:
            if d > 2:
                return 0
            d += 1
            # ----- make data stationary and drop NA values ----- #
            data_series_diff = data_series_diff.diff().dropna()

            try:
                data_series_diff_values = data_series_diff.values
                adf_test_results = adfuller(data_series_diff_values)
            except:
                d -= 1
                return d

        return d

    def get_order_ARIMA(self, data_series):
        aic_dict = dict()

        if len(self.d_values) != 1:
            d = self.get_d_value_and_ADF_test()
        else:
            d = 0

        for p in self.p_values:
            for q in self.q_values:
                order = [p, d, q]

                try:
                    arma_model = ARIMA(data_series, order).fit(disp=False)
                    aic = arma_model.aic

                    if [p, d, q] == [0, 0, 0]:
                        continue

                    if aic not in aic_dict:
                        aic_dict[aic] = order
                        # print("Order: {}, AIC: {}".format(order, aic))
                except:
                    continue

        # if aic_dict is empty
        # it is impossible to create arima model for this data set
        if len(aic_dict) == 0:
            return None

        min_val = min(aic_dict.keys())

        return aic_dict[min_val]

    @staticmethod
    def make_forecast_ARIMA(order, data_series, steps):
        model = ARIMA(data_series, order=order).fit(disp=False)
        forecast_list = model.forecast(steps=steps)[0].tolist()

        return forecast_list

    @staticmethod
    def get_forecast_accuracy_with_real_data(forecast, actual):
        return sqrt(mean_squared_error(actual, forecast))

    @staticmethod
    def get_steps_and_points_of_min_rmse(rmse_dataframe):
        min_rmse = rmse_dataframe.min().min()
        results = rmse_dataframe.isin([min_rmse])
        series_obj = results.any()
        column_names = list(series_obj[series_obj == True].index)
        for col in column_names:
            rows = list(results[col][results[col] == True].index)
            for row in rows:
                return [row, col]

    def get_all_possible_models_with_data_points(self):
        if self.optimize:
            if len(self.data_series) <= 1000 + self.steps:
                data_optimize_points = len(self.data_series)
                point_range = int(data_optimize_points / 20)
            else:
                data_optimize_points = 1010
                point_range = 50
        else:
            data_optimize_points = len(self.data_series)
            point_range = int(data_optimize_points / 20)

        models_order_and_data_points_dict = dict()
        last_point = len(self.data_series) - self.steps - 1

        data_point_range = range(200, data_optimize_points, point_range)
        for data_points in data_point_range:
            first_point = last_point - data_points
            if first_point < 0:
                break
            data_series_copy = self.data_series[first_point:last_point].copy()

            order = self.get_order_ARIMA(data_series_copy)
            if order is None:
                continue
            else:
                models_order_and_data_points_dict[data_points] = order

        return models_order_and_data_points_dict

    def get_forecast(self):

        if self.model_name == "Not defined":
            return [None, None, None]

        models_order_and_data_points_dict = self.get_all_possible_models_with_data_points()

        if not bool(models_order_and_data_points_dict):
            return [None, None, None]

        # dataframe of data points, steps and RMSE
        rmse_df = pd.DataFrame()

        rmse_dict = dict()
        last_point = len(self.data_series) - 1 - self.steps

        for data_points, order in models_order_and_data_points_dict.items():
            first_point = last_point - data_points
            data_series_copy = self.data_series[first_point:last_point].copy()

            # ----- Make copy of real data for comparing with forecast ----- #
            data_copy_with_steps = self.data_series[last_point - 1:last_point - 1 + self.steps].copy()

            forecast_list = self.make_forecast_ARIMA(order, data_series_copy, self.steps)

            rmse = self.get_forecast_accuracy_with_real_data(forecast_list, data_copy_with_steps.values)
            rmse_dict[data_points] = rmse

        rmse_series = pd.Series(rmse_dict)
        rmse_df[str(self.steps)] = rmse_series

        rmse_df.reset_index(inplace=True)
        rmse_df['order'] = models_order_and_data_points_dict.values()
        rmse_df.rename(columns={'index': 'points'}, inplace=True)
        rmse_df.set_index(['points', 'order'], inplace=True)

        print(self.model_name)
        pd.set_option('display.max_rows', None)
        print(rmse_df)

        results = self.get_steps_and_points_of_min_rmse(rmse_df)

        data_points_for_forecast = results[0][0]

        data_series_copy = self.data_series[- data_points_for_forecast:].copy()

        model_order = self.get_order_ARIMA(data_series_copy)

        if model_order is None:
            return [None, None, None]

        forecast = self.make_forecast_ARIMA(model_order, data_series_copy, self.steps)

        return [data_points_for_forecast, model_order, forecast]
