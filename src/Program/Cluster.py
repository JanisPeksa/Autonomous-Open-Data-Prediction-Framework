from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
from Program.ClusterResults import ClusterResults
import math


class Cluster:

    def __init__(self, records, max_k_value=10, default_k_value=None, path_to_save=None):
        self.k_range = range(1, max_k_value)
        self.records_df = self.get_records_df(records)
        self.lat_and_lng_array = self.get_lat_and_lng_array()

        self.path_to_save = path_to_save
        if path_to_save is not None:
            self.save_results = True
        else:
            self.save_results = False

        self.default_k_value = default_k_value

        self.dist_points_from_cluster_center = None
        self.distance_of_points_from_line = None

        if default_k_value is None:
            self.optimal_k_value = self.get_optimal_k_value()
        else:
            self.optimal_k_value = default_k_value

    @staticmethod
    def get_records_df(records):
        records_df = pd.DataFrame.from_records(records, columns=["index", "code", "name", "lat", "lng"])
        records_df = records_df[["code", "lat", "lng"]]

        records_df["lat"] = records_df["lat"].astype(float)
        records_df["lng"] = records_df["lng"].astype(float)

        return records_df

    def get_lat_and_lng_array(self):
        lat_and_lng_array = np.column_stack((self.records_df["lng"], self.records_df["lat"]))
        return lat_and_lng_array

    def get_dist_points_from_cluster_center_using_k_range(self):
        dist_points_from_cluster_center = []
        k = range(1, 10)
        for num_of_clusters in k:
            k_model = KMeans(n_clusters=num_of_clusters)
            k_model.fit(self.lat_and_lng_array)
            dist_points_from_cluster_center.append(k_model.inertia_)
        return dist_points_from_cluster_center

    @staticmethod
    def calc_distance(x1, y1, a, b, c):
        d = abs((a * x1 + b * y1 + c)) / (math.sqrt(a * a + b * b))
        return d

    def cal_distance_of_points_from_line(self):
        a = self.dist_points_from_cluster_center[0] - self.dist_points_from_cluster_center[8]
        b = self.k_range[-1] - self.k_range[0]
        c1 = self.k_range[0] * self.dist_points_from_cluster_center[8]
        c2 = self.k_range[-1] * self.dist_points_from_cluster_center[0]
        c = c1 - c2

        distance_of_points_from_line = []
        for k in range(len(self.k_range)):
            distance_of_points_from_line.append(
                Cluster.calc_distance(self.k_range[k], self.dist_points_from_cluster_center[k], a, b, c))

        return distance_of_points_from_line

    def get_optimal_k_value(self):
        self.dist_points_from_cluster_center = self.get_dist_points_from_cluster_center_using_k_range()
        self.distance_of_points_from_line = self.cal_distance_of_points_from_line()

        opt_value = self.distance_of_points_from_line.index(max(
            self.distance_of_points_from_line)) + 1
        return opt_value

    def save_results_and_graphs(self):
        cluster_results = ClusterResults(self.records_df, self.k_range, self.optimal_k_value,
                                         path_to_save_results=self.path_to_save)

        if self.default_k_value is None:
            cluster_results.get_dist_points_from_cluster_center_plot(self.dist_points_from_cluster_center)
            cluster_results.get_distance_of_points_from_line_plot(self.distance_of_points_from_line)

        cluster_results.get_clustered_stations_plot()

    # x - lng
    # y - lat

    def make_clustering(self):
        km = KMeans(n_clusters=self.optimal_k_value)
        predicted = km.fit_predict(self.records_df[["lng", "lat"]])
        self.records_df["cluster"] = predicted

    def make_scaler(self):
        scaler = MinMaxScaler()

        scaler.fit(self.records_df[["lat"]])
        self.records_df["lat"] = scaler.transform(self.records_df[["lat"]])

        scaler.fit(self.records_df[["lng"]])
        self.records_df["lng"] = scaler.transform(self.records_df[["lng"]])

    def get_stations_clusters_df(self):
        self.make_scaler()
        self.make_clustering()

        if self.save_results:
            self.save_results_and_graphs()

        self.records_df.set_index("code", inplace=True)
        return self.records_df[["cluster"]]
