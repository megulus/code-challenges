def zerofy_rows_cols(two_d_array):
  if (len(two_d_array)) == 0:
    return two_d_array
  else:
    indeces = set()
    zerofy_row = False
    for i in range(len(two_d_array)):
      row = two_d_array[i]
      for j in range(len(row)):
        if row[j] == 0:
          indeces.add(j)
          zerofy_row = True
      if zerofy_row:
        two_d_array[i] = [0] * len(row)
        zerofy_row = False
    if (len(indeces)) > 0:
      for row in two_d_array:
        for index in indeces:
          row[index] = 0
  return two_d_array


def main():
  print(zerofy_rows_cols([[1, 0, 1, 0], [3, 5, 6, 7], [4, 2, 3, 4]]))

if __name__ == '__main__':
  main()
