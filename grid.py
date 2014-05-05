from cell import *

class Grid:
  #Grid is represented as a list of cells
  grid = []

  def __init__(self, length, height):
    self.height = height
    self.length = length
    for row in range(height):
      for col in range(length):
        self.grid.append(Cell(col, row))

    while self.check_matches():
      self.fill()

  #Return cell based on (col X row) position
  def cell(self, col, row):
    col -= 1
    row = (row-1) * self.length

    return self.grid[row + col]

  #Change the value of a cell
  def change(self, col, row, val):
    col -= 1
    row = (row-1) * self.length
    self.grid[row + col].color = val
    return val

  #Switch values of two cells
  #cell1 and cell2 are lists of col and row
  def switch(self, cell1, cell2):
    cell1 = self.cell(cell1[0], cell1[1])
    cell2 = self.cell(cell2[0], cell2[1])
    color1 = cell1.color
    color2 = cell2.color
    self.change(cell1.col+1, cell1.row+1, color2)
    self.change(cell2.col+1, cell2.row+1, color1)

  def check_matches(self):
    matches = False
    #Check for horizontal matches
    for row in range(1, self.height+1):
      for col in range(1, self.length-1):
        cell1 = self.cell(col, row)
        cell2 = self.cell(col+1, row)
        cell3 = self.cell(col+2, row)
        if cell1.color == cell2.color == cell3.color:
          matches = True
          self.change(cell1.col+1, cell1.row+1, ' ')
          self.change(cell2.col+1, cell2.row+1, ' ')
          self.change(cell3.col+1, cell3.row+1, ' ')
    for col in range(1, self.length+1):
      for row in range(1, self.height-1):
        cell1 = self.cell(col, row)
        cell2 = self.cell(col, row+1)
        cell3 = self.cell(col, row+2)
        if cell1.color == cell2.color == cell3.color:
          matches = True
          self.change(cell1.col+1, cell1.row+1, ' ')
          self.change(cell2.col+1, cell2.row+1, ' ')
          self.change(cell3.col+1, cell3.row+1, ' ')
    return matches

  def fill(self):
    empty=True
    while empty:
      empty=False
      for row in range(self.height):
        for col in range(self.length):
          if self.cell(col, row).color == ' ':
            empty = True 
            if row != self.height-1:
              self.change(col, row, self.cell(col, row+1).color)
              self.change(col, row+1, ' ')
            else:
              self.change(col, row, self.cell(col, row+1).color)
              self.change(col, row+1, colors[randint(0, len(colors)-1)])

  def update(self, cursor):
    for cell in self.grid:
      cell.draw()
    self.cell(cursor[0], cursor[1]).draw(True)
    self.cell(cursor[0]+1, cursor[1]).draw(True)
