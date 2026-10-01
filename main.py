import dow


def getDayOfTheWeekForUserDate():
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    year = int(input("Enter year: "))

    result_day = dow.getDayOfTheWeek(year, month, day)
    print(f"{month}-{day}-{year} is a {result_day.lower()}.")


if __name__ == "__main__":
    dow.makeCalendar()
    getDayOfTheWeekForUserDate()