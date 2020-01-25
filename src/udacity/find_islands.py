'''
Given a 2D (n x m) matrix M consisting only of 0s and 1s, find the 
number of islands it contains. An island is defined as 1 or more
adjacent 1s 

1. Clarifying the Question
    Q: What constitutes an island? Just vertically/horizontally adjacent 1s, or also
       diagonally?
    A. In this case, just horizontally/vertically connected - but this is a popular
       interview question with many variants. Some interviewers might consider diagonally
       connected 1s to be an island

       [[1, 0],    OR     [[1, 1],      but NOT   [[1, 0], 
       [1, 0]]            [0, 0]]                 [0, 1]]

2. Confirming Inputs/Outputs
    Confirm that we're taking in a 2D matrix containing only 0s and 1s, and returning
    an integer representing the number of islands in the matrix.
    

    example input: [[1, 0, 1], 
                    [1, 1, 1]]
            output: 1

    This also helps to clarify the method signature for the code we'll write later on.

3. Test Cases
    Think about edge cases. Can we take a None object? Empty 2D array? Can I assume that
    any other 2D array input will only contain 0s and 1s, and nothing else?

    Edge cases: None object, [[]]

4. Brainstorming
    None input => 0
    [[]] input => 0
    [1, 0, 1], 
    [1, 1, 1]] => When we encounter the first 1 (M[0][0]), we'll want to initialize some 
                  island counter to 1. Then we'll get to the 0. We don't have to do anything
                  because it's not part of an island. When we get to the third island (M[0][2]),
                  we'll need to check whether it's part of an island. So we need some way of 
                  keeping track of which 1s are part of the same island.
                  --> So, each time we encounter a 1, we want to look around it and see if it
                  is part of an island. 
                  --> Matrix could be represented as a graph (typically, this is used the other
                  way around -- i.e., an adjacency matrix used to represent a graph)
                  --> ** This should call to mind a BREADTH FIRST SEARCH **
    

5. Runtime Analysis
    We're looking at each element of the n x m array at least once. Runtime will be at least
    n x m, where n == # of rows, m == # of columns


6. Coding
    Primary function island_counter(M)
      -- handle the None, [[]] cases first
      -- then we'll need a double for loop to go through the 2D array
      -- if an element is a 1, we know it's an island or part of one - define a helper method
         to find the island that it's part of ** this is our BFS   


7. Debugging
'''

from collections import deque

def find_islands(M):
    if (M == None or M == [[]]):
        return 0
    else:
        islands = 0
        rows = len(M)
        cols = len(M[0])
        for i in range(rows):
            for j in range(cols):
                if M[i][j] == 1:
                    islands += 1
                    find_island_parts(M, i, j, rows, cols)
        return islands

'''
The helper method below is our Breadth First Search method. The general
BFS algorithm is: (here, a 'vertex' is an element of the 2D array)
- put source onto queue
- while queue is not empty:
  - remove the next vertex v from the queue
  - put onto queue all unmarked vertices adjacent to v and mark them
'''
def find_island_parts(M, i, j, rows, cols):
    q = deque()
    q.append([i, j])
    while len(q) != 0:
        el = q.pop()
        r = el[0]
        c = el[1]
        if M[r][c] == 1:
            M[r][c] = 2
            check_adjacent_indices(q, r + 1, c, rows, cols)
            check_adjacent_indices(q, r - 1, c, rows, cols)
            check_adjacent_indices(q, r, c + 1, rows, cols)
            check_adjacent_indices(q, r, c - 1, rows, cols)


'''
Another helper method that simply checks whether indices are in range
'''
def check_adjacent_indices(q, r, c, rows, cols):
    if (r >= 0 and r < rows and c >= 0 and c < cols):
        q.append([r, c])




def main():
    print('find_islands(): ' + str(find_islands(None)))
    print('find_islands([[]]): ' + str(find_islands([[]])))
    print('find_islands([[1, 0, 1], [1, 1, 1]]): ' +
          str(find_islands([[1, 0, 1], [1, 1, 1]])))
    print('find_islands([[1, 0, 0, 1], [0, 1, 1, 1], [0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 1, 0]]): ' +
          str(find_islands([[1, 0, 0, 1], [0, 1, 1, 1], [0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 1, 0]])))
    



if __name__ == '__main__':
    main()

