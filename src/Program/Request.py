from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

from Program.Request_data import headers, login_data
from Program.TimeStamps import TimeStamps


class Request:

    @staticmethod
    def get_data_lists_from_table(table) -> list:
        tmp_list = []
        data_list = []

        for row in table.find_all('tr'):
            for cell in row.find_all('td'):
                tmp_list.append(cell.text)

            while len(tmp_list) < 19:
                tmp_list.append('-')

            data_list.append(tmp_list)
            tmp_list = []

        data_list.pop(0)

        return data_list

    @staticmethod
    def get_table(url='http://www.lvceli.lv/cms/'):
        with requests.session() as s:
            r = s.post(url, data=login_data, headers=headers)

        soup = BeautifulSoup(r.content, 'html5lib')
        return soup.find("table", attrs={"class": "norm", "id": "table-1"})

    @staticmethod
    def get_old_tables(modified_urls: list) -> list:
        old_tables = []

        with requests.session() as s:
            r = s.post('http://www.lvceli.lv/cms/', data=login_data, headers=headers)

            for url in modified_urls:
                r = s.get(url)
                soup = BeautifulSoup(r.content, 'html5lib')
                old_tables.append(soup.find("table", attrs={"class": "norm", "id": "table-1"}))

        return old_tables

    @staticmethod
    def get_time_stamps() -> dict:
        time_stamps = TimeStamps()
        return time_stamps.get()

    @staticmethod
    def get_valid_dates(time_stamps) -> list:
        valid_dates = []

        year_start = time_stamps['Year Start']
        year_stop = time_stamps['Year Stop']

        month_start = time_stamps['Month Start']
        month_stop = time_stamps['Month Stop']

        day_start = time_stamps['Day Start']
        day_step = time_stamps['Day Step']
        day_stop = time_stamps['Day Stop']

        hour_start = time_stamps['Hour Start']
        hour_step = time_stamps['Hour Step']
        hour_stop = time_stamps['Hour Stop']

        date_start = datetime(year_start, month_start, day_start, hour_start, 0, 0)
        date_stop = datetime(year_stop, month_stop, day_stop, hour_stop, 0, 0)
        date_step = timedelta(days=day_step, hours=hour_step)
        date_next = date_start + date_step

        while date_next <= date_stop:
            valid_dates.append(date_next)
            date_next += date_step

        return valid_dates

    @staticmethod
    def transform_date_into_url_modifier(date) -> str:
        return '{}{:02d}{:02d}{:02d}'.format(date.year, date.month, date.day, date.hour)

    def get_url_modifiers(self) -> list:
        url_modifiers = []

        valid_dates = self.get_valid_dates(self.get_time_stamps())

        for date in valid_dates:
            url_modifiers.append(self.transform_date_into_url_modifier(date))

        return url_modifiers

    def get_modified_urls(self):
        modified_urls = []

        for modifier in self.get_url_modifiers():
            modified_urls.append('http://www.lvceli.lv/cms/index.php?h=' + modifier)

        return modified_urls

    @staticmethod
    def get_data_from_old_tables(old_tables) -> list:
        data = []
        rows = []
        cells = []

        for table in old_tables:
            for row in table.find_all('tr'):
                for cell in row.find_all('td'):
                    cells.append(cell.text)
                rows.append(cells)
                cells = []
            rows.pop(0)
            data.append(rows)
            rows = []

        return data

    @staticmethod
    def get_data_doc_from_data(data: list) -> list:
        data_doc = []
        for table in data:
            for row in table:
                if len(row) < 19:
                    continue
                else:
                    data_doc.append({'Station': row[0], 'Time': row[1], 'Dew Point': row[5]})

        return data_doc
