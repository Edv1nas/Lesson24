"""Write a function that returns dates of the 5 upcoming Friday 13ths, with Year, month and date"""

import datetime


def get_upcoming_friday_13ths():
    friday_13ths = []
    today = datetime.date.today()
    year = today.year

    while len(friday_13ths) < 5:
        for month in range(1, 13):
            date = datetime.date(year, month, 13)
            if date.weekday() == 4:
                friday_13ths.append(date.strftime("%Y-%m-%d"))

        year += 1

    return friday_13ths


print(get_upcoming_friday_13ths())
