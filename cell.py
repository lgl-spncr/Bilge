from random import *
from gui import *

interface = Interface()

colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan')
class Cell:
  def __init__(self, col, row):
    self.color = colors[randint(0, len(colors)-1)]
    self.col = col
    self.row = row
    self.x = col
    self.y = row

  def draw(self, cursor=False):
    interface.draw_cell(self, cursor)
