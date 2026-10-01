def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def getDayOfTheWeek(year, month, day):
    yy = year % 100
    twelves = yy // 12
    remainder = yy - (twelves * 12)
    fours = remainder // 4

    total = twelves + remainder + fours + day

    month_codes = {
        1: 1, 2: 4, 3: 4, 4: 0, 5: 2, 6: 5,
        7: 0, 8: 3, 9: 6, 10: 1, 11: 4, 12: 6
    }

    total += month_codes[month]

    century = year // 100

    if century == 16:
        total += 6
    elif century == 17:
        total += 4
    elif century == 18:
        total += 2
    elif century == 20:
        total += 6
    elif century == 21:
        total += 4

    if (month == 1 or month == 2) and isLeapYear(year):
        total -= 1

    day_index = total % 7

    days = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday"
    }

    return days[day_index]


def makeCalendar():
    days_in_months = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    year = 2026

    for month in range(1, 13):
        max_days = days_in_months[month]

        for day in range(1, max_days + 1):
            day_name = getDayOfTheWeek(year, month, day)
            print(f"{month}-{day}-{year} is a {day_name.lower()}.")