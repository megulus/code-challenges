"""
Given an image represented by an NxN matrix, where each pixel is 
represented by 4 bytes, write a method to rotate the image by 90 
degrees. Can you do this in place?
1 byte = 8 bits
4 bytes = 32 bits
i.e., 64x64 bit matrix = 8x8 byte matrix = 2x2 pixel matrix
assuming clockwise rotation
"""


def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(((n - 1) // 2) + 1):
        flip(matrix, i)


def flip(matrix, ring_index):
  row = ring_index
  n = len(matrix)
  for col in range(ring_index, len(matrix) - 1 - ring_index):
    cell1 = (row, col)
    cell2 = (col, n - 1 - ring_index)
    cell3 = (n - 1 - ring_index, n - 1 - col)
    cell4 = (n - 1 - col, row)
    swap(matrix, cell1, cell2, cell3, cell4)


def swap(matrix, cell1, cell2, cell3, cell4):
    a = matrix[cell1[0]][cell1[1]]
    b = matrix[cell2[0]][cell2[1]]
    c = matrix[cell3[0]][cell3[1]]
    d = matrix[cell4[0]][cell4[1]]
    matrix[cell1[0]][cell1[1]] = d
    matrix[cell2[0]][cell2[1]] = a
    matrix[cell3[0]][cell3[1]] = b
    matrix[cell4[0]][cell4[1]] = c


def print_matrix(matrix):
    for row in matrix:
        row_str = ''
        for col in row:
            row_str += str(col) + '  '
        print(row_str)
    print('\n')


def main():
    # matrix = [['a1', 'b1', 'c1', 'a2'], ['c4', 'd1', 'd2', 'b2'],
    #           ['b4', 'd4', 'd3', 'c2'], ['a4', 'c3', 'b3', 'a3']]
    matrix = [['a1', 'b1', 'c1', 'd1', 'a2'], ['d4', 'e1', 'f1', 'e2', 'b2'],
              ['c4', 'f4', 'g1', 'f2', 'c2'], ['b4', 'e4', 'f3', 'e3', 'd2'], ['a4', 'd3', 'c3', 'b3', 'a3']]
    print_matrix(matrix)
    # print('\n')
    rotate_matrix(matrix)
    print_matrix(matrix)


if __name__ == "__main__":
    main()
