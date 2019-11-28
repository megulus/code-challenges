"""
CTCI Problem 1.4
Given a string, check whether it is a permutation of a palindrome.
Palindrome does not have to be limited to dictionary words
Example:
  Input: "Tact Coa"
  Output: True ("taco cat", "atco cta", etc.)
"""

def is_palindrome_permutation(my_string):
  if len(my_string) == 0:
    return False # my assumption - could also be true by definition, but problem is ambiguous on this
  else:
    my_string = my_string.replace(' ', '')
    counts = {}
    for c in my_string:
      char = c.lower()
      if char in counts:
        counts[char] += 1
      else:
        counts[char] = 1
    count_odds = 0
    for d in my_string:
      char = d.lower()
      if counts[char] % 2 != 0:
        if len(my_string) % 2 == 0:
          return False
        else:
          if count_odds == 1:
            return False
          else:
            count_odds += 1
    return True

def main():
  print(is_palindrome_permutation("Tact oa"))


if __name__ == "__main__":
  main()