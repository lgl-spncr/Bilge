from curses import *
import time

Colors = {
  'red':1,
  'green':2,
  'yellow':3,
  'blue':4,
  'magenta':5,
  'cyan':6,
}

class Timer:
  def __init__(self, win, pos, length):
    self.start_time = time.time()
    self.start_time -= 1
    self.win = win
    self.y = pos[0]
    self.x = pos[1]
    self.time = length
    self.update()
  def update(self):
    if time.time() - self.start_time > 1:
      self.start_time = time.time()
      self.time -= 1
      self.win.addstr(self.y, self.x, '   ')
      self.win.addstr(self.y, self.x, str(self.time))
      self.win.refresh()

class Meter:
  def __init__(self, win, pos):
    self.val = 0 
    self.win = win
    self.y = pos[0]
    self.x = pos[1]
  def update(self, val):
    if self.val != val:
      self.val = val
      self.win.addstr(self.y, self.x, '   ')
      self.win.addstr(self.y, self.x, str(self.val))

class Interface:
  def __init__(self):
    self.term = initscr()
    noecho()
    cbreak()
    height, width = self.term.getmaxyx() 
    self.game = newwin(18, 48, (height/2)-9, (width/2)-15)
    self.screen = newwin(14, 26, (height/2)-7, (width/2)-13)
    self.stats = newwin(14, 15, (height/2)-7, (width/2)+15)
    self.screen.box()
    self.stats.box()
    self.term.refresh()


    start_color()

    init_pair(1, COLOR_BLACK, COLOR_RED)
    init_pair(2, COLOR_BLACK, COLOR_GREEN)
    init_pair(3, COLOR_BLACK, COLOR_YELLOW)
    init_pair(4, COLOR_BLACK, COLOR_BLUE)
    init_pair(5, COLOR_BLACK, COLOR_MAGENTA)
    init_pair(6, COLOR_BLACK, COLOR_CYAN)
    init_pair(7, COLOR_WHITE, COLOR_RED)
    init_pair(8, COLOR_WHITE, COLOR_GREEN)
    init_pair(9, COLOR_WHITE, COLOR_YELLOW)
    init_pair(10, COLOR_WHITE, COLOR_BLUE)
    init_pair(11, COLOR_WHITE, COLOR_MAGENTA)
    init_pair(12, COLOR_WHITE, COLOR_CYAN)

    for row in range(17):
      for col in range(47):
        self.game.addch(row, col, ' ', color_pair(5))
    self.game.refresh()

    for row in range(1, 13):
      for col in range(1, 14):
        self.stats.addch(row, col, ' ', color_pair(5))
    self.screen.refresh()
    
    self.stats.addstr(2, 4, " Level ")
    self.level = Meter(self.stats, (3, 6))
    self.stats.addstr(5, 4, " Goal ")
    self.goal = Meter(self.stats, (6, 6))
    self.stats.addstr(8, 4, " Score ")
    self.score = Meter(self.stats, (9, 6))
    self.stats.addstr(11, 4, " Timer ")
    self.timer = Timer(self.stats, (12, 6), 150)
    self.stats.refresh()


  def draw_cell(self, cell, cursor=False):
    if cell.color == ' ':
      if cursor:
        self.screen.addstr(cell.y+1, (cell.x*4)+1, '[  ]')
      else:
        self.screen.addstr(cell.y+1, (cell.x*4)+1, '    ')
    else:
      if cursor:
        color = color_pair(Colors[cell.color] + 6)
      else:
        color = color_pair(Colors[cell.color])
      self.screen.addstr(cell.y+1, (cell.x*4)+1, '[  ]', color | A_BOLD)

  def getkey(self):
    return self.screen.getkey()

  def quit(self):
    endwin()
