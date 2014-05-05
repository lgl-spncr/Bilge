import sys
from gui import *
import time

from grid import *

interface = Interface()

class Bilge:
  cursor = [1, 1]
  level = 1
  goal = 80
  def __init__(self):
    self.original_goal = 80
    self.start_time = time.time()
    self.score = 0
    interface.score.update(self.score)
    interface.level.update(self.level)
    interface.goal.update(self.goal)
    self.timer = 150 #2 and a half minutes of game play
    self.grid = Grid(6, 12)

    self.grid.update(self.cursor)

  def main(self):
    def up(): 
      if self.cursor[1] > 1:
        self.cursor[1] -= 1
    def down():
      if self.cursor[1] < self.grid.height:
        self.cursor[1] += 1
    def left():
      if self.cursor[0] > 1:
        self.cursor[0] -= 1
    def right():
      if self.cursor[0] < self.grid.length - 1:
        self.cursor[0] += 1
    def switch():
      cursor2 = (self.cursor[0]+1, self.cursor[1])
      self.grid.switch(self.cursor, cursor2)
    def quit():
      interface.quit()
      print "Score: %d" % self.score
      sys.exit()

    keys = {
      'w':up,
      's':down,
      'a':left,
      'd':right,
      'k':up,
      'j':down,
      'h':left,
      'l':right,
      '\n':switch,
      ' ':switch,
      'q':quit,
    }

    ## GAME LOOP
    while True:
      while self.grid.check_matches(): 
        self.score += 1
        self.goal -= 1
        interface.score.update(self.score)
        interface.goal.update(self.goal)
        self.grid.fill()
      self.grid.update(self.cursor)
      interface.timer.update()

      if interface.timer.time == 0 or self.goal <= 0:

        if not self.goal <= 0:
          quit()
        else:
          interface.timer.time = 150
          self.level += 1
          self.original_goal += 5
          self.goal = self.original_goal
          interface.level.update(self.level)
          interface.goal.update(self.goal)

      key = interface.getkey()
      if type(key) == list:
        if key[0] <= self.grid.length-1 and key[0] != 0 \
		  and key[1] <= self.grid.height:
          self.cursor = key
      elif key in keys:
        keys[key]()

if __name__ == "__main__":
  puzzle = Bilge()
  puzzle.main()
