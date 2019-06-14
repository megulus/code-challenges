
def translateDayNumber(dayNumber):
  days = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
  }
  return days[dayNumber]

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

def countDaysElapsed(month, day, year):
  startMonth = 1
  startDay = 1
  startYear = 1753
  yearsElapsed = year - startYear
  monthsElapsed = year - startMonth
  daysElapsed = year - startDay

def main():
  year = 2020
  print("{0} is a leap year: {1}".format(year, isLeapYear(year)))

if __name__ == "__main__":
  main()
