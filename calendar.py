STARTYEAR = 1753
STARTDAY = 1
STARTMONTH = 1
MONTHS = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}
DAYS = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def translateDayNumber(dayNumber):
  return DAYS[dayNumber]

def translateMonthNumber(monthNumber):
  return MONTHS[monthNumber]

def isLeapYear(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  return False

def countDaysInElapsedYears(elapsedYears):
  count = 0
  for i in range(elapsedYears):
    year = STARTYEAR + i
    if isLeapYear(year):
      count += 366
    else:
      count += 365
  return count

def countDaysInElapsedMonths(elapsedMonths, year):
  count = 0
  for i in range(elapsedMonths):
    if i == 1:
      if isLeapYear(year):
        count += 29
      else:
        count += 28
    elif i in [3, 5, 8, 10]:
      count += 30
    else:
      count += 31
  return count

def countDaysElapsed(month, day, year):
  yearsElapsed = year - STARTYEAR
  monthsElapsed = month - STARTMONTH
  daysElapsed = day - STARTDAY
  daysInElapsedYears = countDaysInElapsedYears(yearsElapsed)
  daysInElapsedMonths = countDaysInElapsedMonths(monthsElapsed, year)
  return daysInElapsedYears + daysInElapsedMonths + daysElapsed

def whatDayOfTheWeekWas(month, day, year):
  numberOfDaysElapsed = countDaysElapsed(month, day, year)
  return translateDayNumber(numberOfDaysElapsed % 7)

def main():
  month = 3
  day = 24
  year = 1977
  print("{0} {1}, {2} is/was/will be a {3}.".format(translateMonthNumber(month), day, year, whatDayOfTheWeekWas(month, day, year)))

if __name__ == "__main__":
  main()
