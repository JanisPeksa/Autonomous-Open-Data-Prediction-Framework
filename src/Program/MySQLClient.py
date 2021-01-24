import mysql.connector


class MySQLClient:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.database_connection = self.connect_to_database()
        self.cursor = self.database_connection.cursor()

    def connect_to_database(self):
        database_connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            passwd=self.password,
            database=self.database
        )
        return database_connection

    def get_all_info_from_database(self):
        command = 'SELECT * FROM data_records'
        self.cursor.execute(command)
        records = self.cursor.fetchall()
        return records

    def get_all_info_by_stations(self):
        all_info_by_stations = []

        for index in range(1, 55):
            station_code = 'LV{:02d}'.format(index)
            all_info_by_stations.append(self.get_info_by_station(station_code))

        return all_info_by_stations

    def get_info_by_station(self, station_code: str = 'LV01'):
        command = 'SELECT * FROM data_records WHERE stacijas_kods = %s'
        self.cursor.execute(command, (station_code,))
        records = self.cursor.fetchall()
        return records

    def get_info_by_distance(self):
        command = 'SELECT * FROM distance'
        self.cursor.execute(command)
        records = self.cursor.fetchall()
        return records

    def get_latitude_and_longitude(self):
        command = 'SELECT * FROM stations'
        self.cursor.execute(command)
        records = self.cursor.fetchall()
        return records

    def get_info_by_stations(self, station_codes: list) -> list:
        info = []
        for station_code in station_codes:
            command = 'SELECT * FROM data_records WHERE stacijas_kods = %s'
            self.cursor.execute(command, (station_code,))
            records = self.cursor.fetchall()
            info.append(records)
        else:
            return info
