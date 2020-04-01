from openpyxl import Workbook


class XLSXExporter:
    def __init__(self):
        self.workbook = Workbook()
        self.worksheet = self.workbook.active
