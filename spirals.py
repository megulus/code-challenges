from itertools import cycle

class ArraySpiral(object):
  def __init__(self, matrix):
    self.matrix = matrix
    self.rows = len(matrix)
    self.columns = len(matrix[0])
    self.currentRow = 0
    self.currentCol = 0
    self.destinationRow = 0
    self.destinationCol = self.columns - 1
    self.incompleteRows = set([i for i in range(self.rows)])
    self.incompleteCols = set([j for j in range(self.columns)])
    self.path = ['topRight', 'bottomRight', 'bottomLeft', 'topLeft']
    self.nextIndex = 0
    self.next = self.path[self.nextIndex % 4]



  def goToNextCorner(self):
    while ((self.currentRow, self.currentCol) != (self.destinationRow, self.destinationCol)):
      self.printContents()
      self.increment()
    self.completeTraversal()
    if (self.incompleteRows != set() and self.incompleteCols != set()):
      self.setNewDestination()
    else:
      self.printContents()

  def printContents(self):
    print(self.matrix[self.currentRow][self.currentCol])


  def increment(self):
    if self.next == 'topRight':
      self.currentCol += 1
    if self.next == 'bottomRight':
      self.currentRow += 1
    if self.next == 'bottomLeft':
      self.currentCol -= 1
    if self.next == 'topLeft':
      self.currentRow -= 1

  def completeTraversal(self):
    if self.next == 'topRight':
      self.incompleteRows.remove(self.currentRow)
    if self.next == 'bottomRight':
      self.incompleteCols.remove(self.currentCol)
    if self.next == 'bottomLeft':
      self.incompleteRows.remove(self.currentRow)
    if self.next == 'topLeft':
      self.incompleteCols.remove(self.currentCol)

  def setNewDestination(self):
    if self.next == 'topRight':
      self.destinationRow = max(self.incompleteRows)
      self.destinationCol = self.currentCol
    if self.next == 'bottomRight':
      self.destinationRow = self.currentRow
      self.destinationCol = min(self.incompleteCols)
    if self.next == 'bottomLeft':
      self.destinationRow = min(self.incompleteRows)
      self.destinationCol = self.currentCol
    if self.next == 'topLeft':
      self.destinationRow = self.currentRow
      self.destinationCol = max(self.incompleteCols)
    self.nextIndex += 1
    self.next = self.path[self.nextIndex % 4]

  def traverse(self):
    while (self.incompleteRows != set() and self.incompleteCols != set()):
      self.goToNextCorner()


def main():
  matrix = [
    ['a', 'b', 'c', 'd', 'e'],
    ['p', 'q', 'r', 's', 'f'],
    ['o', 'x', 'y', 't', 'g'],
    ['n', 'w', 'v', 'u', 'h'],
    ['m', 'l', 'k', 'j', 'i']
  ]
  arrayspiral = ArraySpiral(matrix)
  arrayspiral.traverse()

if __name__ == "__main__":
  main()
