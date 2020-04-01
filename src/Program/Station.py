from Program.MongoDBClient import MongoDBClient


class Station:
    def __init__(self, name):
        self.name = name

    def get_data_for_station(self, db_client: MongoDBClient) -> list:
        return db_client.get_data_from_collection(self.name)

    def get_value_from_data(self, db_client: MongoDBClient, value: str) -> list:
        list_of_info = []

        for row in self.get_data_for_station(db_client):
            list_of_info.append(row[value])
        else:
            return list_of_info
