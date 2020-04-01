from threading import Thread
from time import sleep
from os import remove
from os.path import isfile

from Program.MongoDBClient import MongoDBClient
from Program.Request import Request


class AutoDBFiller(MongoDBClient):
    def __init__(self, login: str, password: str, main_database_name: str, time_database_name: str):
        super().__init__(login, password, main_database_name, time_database_name)
        self.thread = Thread()
        self.thread_is_running = False
        self.data = []
        self.requester = Request()

    def __del__(self):
        if isfile('first_filling.txt'):
            remove('first_filling.txt')

    def enable_realtime_data_collection(self, update_frequency_in_seconds: float = 10):
        self.thread_is_running = True
        self.thread = Thread(target=self.collect_data_in_realtime(update_frequency_in_seconds))
        print('starting thread')
        self.thread.start()
        return

    def collect_data_in_realtime(self, update_frequency_in_seconds):
        print('creating session')
        while self.thread_is_running:
            sleep(update_frequency_in_seconds)
            self.requester = Request()
            print(' collecting')
            table = self.requester.get_table()
            fill_data_doc = self.requester.get_fill_data_doc(table)

            if self.is_it_first_filling:
                self.fill_time_database(fill_data_doc)
                self.fill_main_database(fill_data_doc)
                self.is_it_first_filling = self.mark_first_filling(False)
                print('  First filling completed')
            else:
                fill_data_doc = self.get_relevant_fill_data_doc(fill_data_doc)
                self.update_time_database(fill_data_doc)
                self.fill_main_database(fill_data_doc)
                print('  Another filling completed')

            print(' collecting finished')

    def disable_realtime_data_collection(self):
        self.thread_is_running = False
        self.thread.join()

    @staticmethod
    def mark_first_filling(param: bool) -> bool:
        file_name = 'first_filling.txt'
        with open(file_name, 'w') as file:
            if not param:
                print('marked first filling with false')
                file.write('0')
                return False
            else:
                print('marked first filling with true')
                file.write('1')
                return True
