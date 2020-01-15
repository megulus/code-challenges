"""
There are three allowable string edits:
- remove a character
- add a character
- replace a character
Given two strings, write a function to determine whether they are one edit
(or zero edits) away
"""

def is_one_away(str1, str2):
  if str1 == str2:
    return True
  if abs(len(str1) - len(str2)) > 1:
    return False
  else:
    same_length = (len(str1) == len(str2))
    diff = 0
    counter1 = 0 # counter for longer string
    counter2 = 0 # counter for shorter string
    stop = len(str2) # start by assuming str2 is shorter
    longer = str1
    shorter = str2
    if not same_length:
      if len(str1) < len(str2):
        stop = len(str1)
        longer = str2
        shorter = str1
    while counter2 < stop:
      if not longer[counter1] == shorter[counter2]:
        diff += 1
        if not same_length:
          counter1 += 1
          if not longer[counter1] == shorter[counter2]: # more than one difference now
            return False
      counter1 += 1
      counter2 += 1
    if not same_length and diff == 0:
      diff += 1
    if diff > 1:
      return False
    return True


def main():
  print(is_one_away('pale', 'ple'))

if __name__ == "__main__":
  main()
