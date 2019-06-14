STARTYEAR = 1753
STARTDAY = 1
STARTMONTH = 1

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
  print('years elapsed ', yearsElapsed)
  monthsElapsed = month - STARTMONTH
  print('months elapsed ', monthsElapsed)
  daysElapsed = day - STARTDAY
  print('days elapsed ', daysElapsed)
  daysInElapsedYears = countDaysInElapsedYears(yearsElapsed)
  daysInElapsedMonths = countDaysInElapsedMonths(monthsElapsed, year)
  return daysInElapsedYears + daysInElapsedMonths + daysElapsed


def main():
  month = 6
  day = 14
  year = 2019
  print("{0} days elapsded since January 1, 1753.".format(countDaysElapsed(month, day, year)))

if __name__ == "__main__":
  main()
