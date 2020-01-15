import sys

"""
CTCI Problem 1.2 Check Permutation:
Given two strings, write a method to decide if one is a permutation of the other.
"""

def is_permutation(str1, str2):
  if len(str1) != len(str2):
    return False
  l1 = [a.lower() for a in str1]
  l2 = [b.lower() for b in str2]
  l1.sort()
  l2.sort()
  for i in range(len(l2)):
    if l1[i] != l2[i]:
      return False
  return True

def main():
  print(is_permutation(sys.argv[1], sys.argv[2]))


if __name__ == '__main__':
  main()
