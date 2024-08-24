def gen_secs():
    sec = 0
    while True:
        sec += 1
        if sec == 60:
            sec = 0
        yield sec


def gen_minutes():
    min = 0
    while True:
        min += 1
        if min == 60:
            min = 0
        yield min


def gen_hours():
    hour = 0
    while True:
        hour += 1
        if hour == 24:
            hour = 0
        yield hour


def gen_time():
    second = 0
    minute = 0
    hour = 0
    secs = gen_secs()
    minutes = gen_minutes()
    hours = gen_hours()
    while True:
        for second in secs:
            if second == 0:
                minute = next(minutes)
                if minute == 0:
                    hour = next(hours)
            #yield f'{hour:02d}:{minute:02d}:{second:02d}'
            yield hour, minute, second


def gen_years(start=2019):
    current_year = start
    while True:
        current_year += 1
        yield current_year


def gen_months():
    month = 0
    while month != 12:
        month += 1
        yield month


def gen_days(month, leap_year=True):
    while True:
        match month:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                yield 31
            case 4 | 6 | 9 | 11:
                yield 30
            case 2:
                if leap_year:
                    yield 29
                else:
                    yield 28

def gen_date():
    day = 1
    month = 1
    year = 2024
    time = gen_time()
    months = gen_months()
    years = gen_years()
    days = gen_days(1)

    while True:
        for hour, minute, second in time:
            if hour == 0 and minute == 0 and second == 0:
                day += 1
                if day > next(days(month, leap_year(year))):
                    day = 1
                    prev_month = month
                    month = next(months)
                    if month != prev_month and month == 1:
                        year = next(years)
        yield f'{day:02d}/{month:02d}/{year} {hour:02d}:{minute:02d}:{second:02d}'




def leap_year(year):
    # Python program to check if year is a leap year or not

    # To get year (integer input) from the user
    # year = int(input("Enter a year: "))

    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        return True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        return True

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        return False



gen = gen_date()
count = 0
for date in gen:
    if count % 100000 == True:
        print(date)


