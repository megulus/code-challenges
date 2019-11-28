"""
CTCI Problem 1.6
Implement a method to perform basic string compression using the
counts of repeated characters. For example, the string 'abbcccccaaa'
would become 'a1b2c5a3.' If the compressed string would not be
shorter than the original, return the original string.
"""

import sys

def compress(my_string): # this is O(n^2) b/c of all of the copies of the string this creates
  if (len(my_string)) == 0:
    return my_string
  new_str = ''
  prev = my_string[0]
  new_str += prev
  my_string = my_string[1:]
  count = 1
  while len(my_string) > 0:
    curr = my_string[0]
    my_string = my_string[1:]
    if curr == prev:
      count += 1
    else:
      new_str += str(count)
      count = 1
      new_str += curr
    prev = curr
  new_str += count
  if len(new_str) >= len(my_string):
    return my_string
  return new_str

def better_compress(my_string):
  if (len(my_string)) == 0:
    return my_string
  new_str = ''
  prev = my_string[0]
  count = 0
  for char in my_string:
    if char == prev:
      count += 1
    else:
      new_str += (prev + str(count))
      count = 1
    prev = char
  new_str += (prev + str(count))
  if len(new_str) >= len(my_string):
    return my_string
  return new_str


def main():
  print('compressed string ' + better_compress(sys.argv[1]))

if __name__ == '__main__':
  main()

