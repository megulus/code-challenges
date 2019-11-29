"""
CTCI Problem 1.3
Write a method to replace all spaces in a string with '%20'
- Assume sufficient space to hold additional characters
- Assume we are given the true length of the string
example:
  Input: 'Mr John Smith    ', 13
 Output: 'Mr%20John%20Smith'
Additional Assumptions (my own):
- If input == '', 0: return ''
- If input == ' ', 1: return '%20'
** do this in place w/a character array
"""

def urlify(input, length):
  space_count = 0
  for i in range(length):
    if input[i] == ' ':
      space_count += 1
  last_empty = (length - 1) + (space_count * 2)
  for i in range(length - 1, -1, -1):
    if input[i] != ' ':
      input[last_empty] = input[i]
      last_empty -= 1
    else:
      input[last_empty] = '0'
      input[last_empty - 1] = '2'
      input[last_empty - 2] = '%'
      last_empty -= 3
  return input

def main():
  print(urlify(['M', 'r', ' ', 'J', 'o', 'h', 'n', ' ', 'S', 'm', 'i', 't', 'h', ' ', ' ', ' ', ' '], 13))

if __name__ == "__main__":
  main()

