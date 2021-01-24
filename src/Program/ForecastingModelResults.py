from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


class ForecastingModelResults:

    def __init__(self, path_to_save_results):
        self.path_to_save_results = path_to_save_results

    def save_adf_test_results(self, d, adf_test_results, data_points):
        adf_test_results_str = "Augmented Dickey-Fuller test for {} data points\n".format(data_points)
        adf_test_results_str += "d = {}\n".format(d)
        adf_test_results_str += "ADF Statistic: %f \n" % adf_test_results[0]
        adf_test_results_str += "p-value: %f\n" % adf_test_results[1]
        adf_test_results_str += "Critical Values:"
        for key, value in adf_test_results[4].items():
            adf_test_results_str += "\n%s: %.3f" % (key, value)

        file = open(self.path_to_save_results + "/adf_test_results_for_{}_data_points.txt".format(data_points), "w+")
        file.write(adf_test_results_str)
        file.close()

    def save_plot_pacf_and_plot_acf(self, data_df_diff, d, data_points):
        # Draw Plot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=80)
        plot_acf(data_df_diff, ax=ax1, lags=50)
        plot_pacf(data_df_diff, ax=ax2, lags=30)

        # Decorate
        # lighten the borders
        ax1.spines["top"].set_alpha(.3)
        ax2.spines["top"].set_alpha(.3)
        ax1.spines["bottom"].set_alpha(.3)
        ax2.spines["bottom"].set_alpha(.3)
        ax1.spines["right"].set_alpha(.3)
        ax2.spines["right"].set_alpha(.3)
        ax1.spines["left"].set_alpha(.3)
        ax2.spines["left"].set_alpha(.3)

        # font size of tick labels
        ax1.tick_params(axis='both', labelsize=12)
        ax2.tick_params(axis='both', labelsize=12)
        name = "ACF_and_PACF_d={}_for_{}_data_points".format(d, data_points)
        plt.savefig(self.path_to_save_results + name)
        plt.close()

    def save_data_difference_plot(self, data_df_diff, d):
        bx = plt.gca()
        data_df_diff.plot(color="green", ax=bx)
        plt.title('Data difference d={} for {} data points'.format(d, len(data_df_diff) + 1))
        plt.xlabel('Date and time')
        plt.ylabel('Dew point')
        name = "Data_difference_d={}_for_{}_data_points.png".format(d, len(data_df_diff) + 1)
        plt.savefig(self.path_to_save_results + name)
        plt.close()

    def save_forecasting_model_summary(self, mode_summary: str, model_name: str):
        file = open(self.path_to_save_results + "/{}_model_summary.txt".format(model_name), "w+")
        file.write(mode_summary)
        file.close()
