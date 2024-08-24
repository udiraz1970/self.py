days_in_month = {
    0: 31,  # January
    1: 28,  # February (non-leap year)
    2: 31,  # March
    3: 30,  # April
    4: 31,  # May
    5: 30,  # June
    6: 31,  # July
    7: 31,  # August
    8: 30,  # September
    9: 31,  # October
    10: 30,  # November
    11: 31  # December
}

class time_stamp:
    def __init__(self, seconds = 0, minutes = 0, hours = 0, days = 0, months = 0, years = 2019) -> None:
        self._seconds = seconds
        self._minutes = minutes
        self._hours = hours
        self._days = days
        self._months = months
        self._years = years

    def collapse_time_table(self):
        
        # Collapse seconds to minutes
        self._minutes += self._seconds // 60
        self._seconds %= 60

        # Collapse minutes to hours
        self._hours += self._minutes // 60
        self._minutes %= 60

        # Collapse hours to days
        self._days += self._hours // 24
        self._hours %= 24

        #collapse days and months
        #can be nicer if you collapse days into years directly only collapsing months if there is less then a year left
        days_rollover = self.get_days_in_month()
        while self._days >= days_rollover:
            self._days -= days_rollover
            self._months += 1
            while self._months >= 12:
                self._months -= 12
                self._years += 1
            days_rollover = self.get_days_in_month()
        while self._months >= 12:
            self._months -= 12
            self._years += 1


    def is_leap_year(self):
        return (self._years % 4 == 0 and self._years % 100 != 0) or self._years % 400 == 0
    
    def get_days_in_month(self):
        if self.is_leap_year() and self._months == 1:
            return 29
        return days_in_month[self._months % 12]
    
    def add_seconds(self, seconds = 1):
        self._seconds += seconds
        self.collapse_time_table()

    def add_minutes(self, minutes = 1):
        self._minutes += minutes
        self.collapse_time_table()

    def add_hours(self, hours = 1):
        self._hours += hours
        self.collapse_time_table()

    def add_days(self, days = 1):
        self._days += days
        self.collapse_time_table()

    def add_months(self, months = 1):
        self._months += months
        self.collapse_time_table()

    def add_years(self, years = 1):
        self._years += years
        self.collapse_time_table()

    def __str__(self) -> str:
        return f"{self._days + 1:02d}/{self._months + 1:02d}/{self._years} {self._hours:02d}:{self._minutes:02d}:{self._seconds:02d}"

def inf_genorator_wrapper(func):
    state = time_stamp()
    def ret():
        while True:
            yield func(state)
    return ret

@inf_genorator_wrapper
def second_gen(state):
    return str(state)
    state.add_seconds()


@inf_genorator_wrapper
def hour_gen(state):
    return str(state)
    state.add_hours()


@inf_genorator_wrapper
def days_gen(state):
    return str(state)
    state.add_days()


def gen_years(start = 2019):
    state = time_stamp(years=start)
    while True:
        yield str(state)
        state.add_years()


for i in days_gen():
    print(i)