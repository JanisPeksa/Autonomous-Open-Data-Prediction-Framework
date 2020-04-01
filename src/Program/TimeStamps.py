class TimeStamps:
    def __init__(self):
        self.year_start = 2020
        self.year_step = 0
        self.year_stop = 2020

        self.month_start = 1
        self.month_step = 0
        self.month_stop = 1

        self.day_start = 10
        self.dat_step = 1
        self.day_stop = 17

        self.hour_start = 12
        self.hour_step = 0
        self.hour_stop = 12

    def get(self):
        return {
            'Year Start': self.year_start,
            'Year Stop': self.year_stop,

            'Month Start': self.month_start,
            'Month Stop': self.month_stop,

            'Day Start': self.day_start,
            'Day Step': self.dat_step,
            'Day Stop': self.day_stop,

            'Hour Start': self.hour_start,
            'Hour Step': self.hour_step,
            'Hour Stop': self.hour_stop
        }
