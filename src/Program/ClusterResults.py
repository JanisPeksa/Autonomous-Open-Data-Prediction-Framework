import matplotlib.pyplot as plt
from itertools import cycle

# x - lng
# y - lat


class ClusterResults:

    def __init__(self, records_df, k_range, optimal_k_value, path_to_save_results):
        self.records_df = records_df
        self.k_range = k_range
        self.path_to_save_results = path_to_save_results
        self.num_of_clusters = optimal_k_value

    def get_stations_location_plot(self):
        for index, row in self.records_df.iterrows():
            plt.annotate(row["code"], (row["lng"], row["lat"]))
        plt.scatter(self.records_df["lng"], self.records_df["lat"], c="g")
        plt.savefig(self.path_to_save_results + "/stations_location")
        plt.close()

    def get_dist_points_from_cluster_center_plot(self, dist_points_from_cluster_center):
        plt.plot(self.k_range, dist_points_from_cluster_center)
        plt.savefig(self.path_to_save_results + "/dist_points_from_cluster_center")
        plt.close()

    def get_distance_of_points_from_line_plot(self, distance_of_points_from_line):
        plt.plot(self.k_range, distance_of_points_from_line)
        plt.savefig(self.path_to_save_results + "/distance_of_points_from_line")
        plt.close()

    def get_clustered_stations_plot(self):
        cycol = cycle("bgrcmk")
        for k in range(self.num_of_clusters):
            df = self.records_df[self.records_df.cluster == k]
            plt.scatter(df.lng, df["lat"], c=next(cycol))
        plt.xlabel("lng")
        plt.ylabel("lat")
        plt.savefig(self.path_to_save_results + "/clustered_stations_location")
        plt.close()
