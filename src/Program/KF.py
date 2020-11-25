# https://pypi.org/project/pykalman/

from pykalman import KalmanFilter

# position is 1-dimensional
# (x,v) is 2-dimensional

class KF_1D:

    def __init__(self, data_values_list: list):
        self.data_values_list = data_values_list

    def get_filtered_values(self):

        kf = KalmanFilter(transition_matrices=[1],
                          observation_matrices=[1],
                          initial_state_mean=0,
                          initial_state_covariance=1,
                          observation_covariance=1,
                          transition_covariance=0.05)

        state_means, state_covariances = kf.smooth(self.data_values_list)

        state_means_list = [state_mean[0] for state_mean in state_means]

        return state_means_list


class KF_2D:

    def __init__(self, data_values_list, position, velocity, time_delta):
        self.data_values_list = data_values_list
        self.position = position
        self.velocity = velocity
        self.time_delta = time_delta

    def get_filtered_values(self):

        kf = KalmanFilter(n_dim_obs=1, n_dim_state=2,
                          initial_state_mean=[self.position, self.velocity],
                          transition_matrices=[[1, self.time_delta], [0, 1]],                       # F
                          observation_matrices=[[1, 0]],                                            # H
                          transition_offsets=[0.5 * self.time_delta ** 2, self.time_delta])         # G

        state_means, state_covariances = kf.smooth(self.data_values_list)

        state_means_list = [state_mean[0] for state_mean in state_means]

        return state_means_list
