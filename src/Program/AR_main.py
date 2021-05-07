import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA


class AR_main:

    def __init__(self, data_series, steps: int, optimize: bool):
        self.data_series = data_series
        self.steps = steps
        self.optimize = optimize

    @staticmethod
    def get_ar_order(data_series):

        d = 0
        q = 0
        p_values = range(0, 10)

        aic_dict = dict()

        for p in p_values:
            order = (p, d, q)

            try:
                ar_model = ARIMA(data_series, order).fit(disp=0)
                aic = ar_model.aic

                if [p, d, q] == [0, 0, 0]:
                    continue

                if aic not in aic_dict:
                    aic_dict[aic] = order

            except:
                # print('ARIMA%s aic not defined' % (order,))
                continue

        # if aic_dict is empty
        # it is impossible to create arima model for this data set
        if len(aic_dict) == 0:
            return None

        min_val = min(aic_dict.keys())

        p = aic_dict[min_val][0]

        return [p, d, q]

    @staticmethod
    def make_ar_forecast(ar_model, data_series, steps):
        ar_model = ARIMA(data_series, order=ar_model).fit(disp=False)

        forecast_list = ar_model.forecast(steps=steps)[0].tolist()

        return forecast_list

    @staticmethod
    def get_forecast_accuracy_with_real_data(forecast, actual):
        rmse = np.mean((forecast - actual) ** 2) ** .5
        return rmse

    @staticmethod
    def get_steps_and_points_of_min_rmse(dataframe):
        min_rmse = dataframe.min().min()
        results = dataframe.isin([min_rmse])
        series_obj = results.any()
        column_names = list(series_obj[series_obj == True].index)
        for col in column_names:
            rows = list(results[col][results[col] == True].index)
            for row in rows:
                return [row, col]

    def get_all_possible_ar_models_with_data_points(self):
        if self.optimize:
            if len(self.data_series) <= 1000 + self.steps:
                optimize_point = len(self.data_series)
            else:
                optimize_point = 1010
        else:
            optimize_point = len(self.data_series)

        ar_models_order_and_data_points_dict = dict()
        last_point = len(self.data_series) - 1 - self.steps
        process = 0
        data_point_range = range(200, optimize_point, 50)
        for data_points in data_point_range:
            process += 1
            first_point = last_point - data_points
            if first_point < 0:
                break
            data_series_copy = self.data_series[first_point:last_point].copy()
            order = self.get_ar_order(data_series_copy)
            if order is None:
                continue
            else:
                ar_models_order_and_data_points_dict[data_points] = order

        return ar_models_order_and_data_points_dict

    def get_ar_forecast(self):

        ar_models_order_and_data_points_dict = self.get_all_possible_ar_models_with_data_points()

        # dataframe of data points, steps and RMSE
        rmse_df = pd.DataFrame()

        rmse_dict = dict()
        last_point = len(self.data_series) - 1 - self.steps

        for data_points, order in ar_models_order_and_data_points_dict.items():

            first_point = last_point - data_points
            data_series_copy = self.data_series[first_point:last_point].copy()

            # ----- Make copy of real data for comparing with forecast ----- #
            data_copy_with_steps = self.data_series[last_point - 1:last_point - 1 + self.steps].copy()

            forecast_list = self.make_ar_forecast(order, data_series_copy, self.steps)

            rmse = self.get_forecast_accuracy_with_real_data(forecast_list, data_copy_with_steps.values)
            rmse_dict[data_points] = rmse

        rmse_series = pd.Series(rmse_dict)
        rmse_df[str(self.steps)] = rmse_series

        rmse_df.reset_index(inplace=True)
        rmse_df['order'] = ar_models_order_and_data_points_dict.values()
        rmse_df.rename(columns={'index': 'points'}, inplace=True)
        rmse_df.set_index(['points', 'order'], inplace=True)

        print("AR model")
        pd.set_option('display.max_rows', None)
        print(rmse_df)

        results = self.get_steps_and_points_of_min_rmse(rmse_df)

        data_points_for_forecast = results[0][0]

        steps = int(results[1])

        data_series_copy = self.data_series[- data_points_for_forecast:].copy()

        ar_model_order = self.get_ar_order(data_series_copy)

        if ar_model_order is None:
            return [None, None, None, None]

        forecast = self.make_ar_forecast(ar_model_order, data_series_copy, steps)

        return [data_points_for_forecast, ar_model_order, steps, forecast]
