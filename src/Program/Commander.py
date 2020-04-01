from Program.AutoDBFiller import AutoDBFiller
from Program.Asker import Asker
from os import system


class Commander:
    def __init__(self):
        self.filler = None
        self.collecting = False

    def wait_for_command(self):
        while True:
            command = input('Enter command, please\n>')
            self.execute_command(command)

    def execute_command(self, command: str):
        if command == 'create client':
            self.command_to_create_mongodb_client()
        elif command == 'enable realtime data collection':
            if self.filler is not None:
                update_frequency = Asker.ask_update_frequency()
                self.command_to_enable_realtime_data_collection(update_frequency)
                self.collecting = True
            else:
                print('You have to create mongoDB client first')
                return
        elif command == 'disable realtime data collection':
            if self.collecting is True:
                self.command_to_disable_realtime_data_collection()
            else:
                print('realtime data collection is already disabled')
                return
        elif command == 'delete database':
            if self.filler is not None:
                database_name = Asker.ask_string_answer('Enter database name you want to delete\n>')
                self.filler.delete_database(database_name)
            else:
                print('You have to create mongoDB client first')
                return
        elif command == 'exit':
            exit()
        elif command == 'clear':
            system('cls')
        else:
            print('Unknown command "{}"'.format(command))

    def command_to_create_mongodb_client(self):
        main_database_name = Asker.ask_string_answer('Enter main table name where information will be stored\n>')
        time_database_name = Asker.ask_string_answer(
            'Enter time table name where time of last insert will be stored\n>')

        self.filler = AutoDBFiller(main_database_name, time_database_name)

        print('client created successfully')

    def command_to_enable_realtime_data_collection(self, update_frequency_in_seconds: float = 10.0):
        self.filler.enable_realtime_data_collection(update_frequency_in_seconds)

    def command_to_disable_realtime_data_collection(self):
        self.filler.disable_realtime_data_collection()
