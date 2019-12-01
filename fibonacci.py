import sys

# recursive fibonacci
def fib(n):
  if n == 0:
    return 0
  elif n == 1: 
    return 1
  else:
    return fib(n - 1) + fib(n -2)

# iterative fibonacci
def iterative_fib(n):
  if n == 0:
    return 0
  # if n == 1:
  #   return 1
  else:
    two_previous = 0
    one_previous = 1
    fib_num = 1
    fib_result = 0
    while fib_num < n:
      fib_result = two_previous + one_previous
      two_previous = one_previous
      one_previous = fib_result
      fib_num += 1
    return fib_result


def main():
  # print(fib(int(sys.argv[1])))
  print(iterative_fib(int(sys.argv[1])))

if __name__ == '__main__':
  main()
