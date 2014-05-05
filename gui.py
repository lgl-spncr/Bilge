import sys
import pygame
from pygame.locals import *
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 51) 
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

Colors = {
  'black':BLACK,
  'red':RED,
  'green':GREEN,
  'yellow':YELLOW,
  'blue':BLUE,
  'magenta':MAGENTA,
  'cyan':CYAN,
}

class Timer:
  def __init__(self, font, screen, pos, length):
    self.start_time = time.time()
    self.start_time -= 1
    self.font = font
    self.screen = screen
    self.x = pos[0]
    self.y = pos[1]
    self.time = length

  def update(self):
    if time.time() - self.start_time > 1:
      self.start_time = time.time()
      self.time -= 1
      timerSurf = self.font.render(str(self.time), True, (255, 255, 255), (0, 0, 0))
      timerRect = timerSurf.get_rect()
      timerRect.topleft = (self.x, self.y)
      pygame.draw.rect(self.screen, BLACK, (self.x, self.y, 220, 40))
      self.screen.blit(timerSurf, timerRect)
      pygame.display.update()

class Meter:
  def __init__(self, font, screen, pos):
    self.val = 0
    self.font = font
    self.screen = screen
    self.x = pos[0]
    self.y = pos[1]
  def update(self, val):
    if self.val != val or self.val == 0:
      self.val = val
      meterSurf = self.font.render(str(self.val), True, (255, 255, 255), (0, 0, 0))
      meterRect = meterSurf.get_rect()
      meterRect.topleft = (self.x, self.y)
      pygame.draw.rect(self.screen, BLACK, (self.x, self.y, 220, 40))
      self.screen.blit(meterSurf, meterRect)
      pygame.display.update()

class Interface:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((500, 560), 0, 32)
    freesans = pygame.font.Font('freesansbold.ttf', 32)
    self.screen.fill((255, 0, 255)) 
    pygame.draw.rect(self.screen, (0, 0, 0), (20, 20, 280, 510))

    #Each rect object comes to 40 pixels tall
    self.level = Meter(freesans, self.screen, (320, 20))
    self.goal = Meter(freesans, self.screen, (320, 60)) 
    self.score = Meter(freesans, self.screen, (320, 100)) 
    self.timer = Timer(freesans, self.screen, (320, 140), 150)
    pygame.display.update()

    self.current_cursor = (0, 0)

  def draw_cell(self, cell, cursor=False):
    color = Colors[cell.color]
    col = cell.col
    row = cell.row
    #Draw a white box around the cell if cursor, a black box if not
    if cursor:
      pygame.draw.rect(self.screen, (255, 255, 255), (col*46+20, row*42+20, 51, 47))
      pygame.draw.rect(self.screen, color, (col*46+25, row*42+25, 41, 37))

    else:
      pygame.draw.rect(self.screen, (0, 0, 0), (col*46+20, row*42+20, 51, 47))
      pygame.draw.rect(self.screen, color, (col*46+25, row*42+25, 41, 37))
    pygame.display.update()

  def getkey(self):

    keys = {
      K_UP:'w',
      K_DOWN:'s',
      K_LEFT:'a',
      K_RIGHT:'d',
      K_w:'w',
      K_s:'s',
      K_a:'a',
      K_d:'d',
      K_k:'w',
      K_j:'s',
      K_h:'a',
      K_l:'d',
      K_SPACE:' ',
      K_RETURN:' ',
      K_q:'q',
    }

    while True:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        elif event.type == KEYDOWN:
          if event.key in keys:
            return keys[event.key]
        elif event.type == MOUSEMOTION:
          mouse_x, mouse_y = event.pos 
          if mouse_x < 300 and mouse_y < 530:
            mouse_x -= 20
            mouse_y -= 20
            mouse_x /= 46
            mouse_y /= 42
            if mouse_y >= 0 and mouse_x >= 0 and \
              list((mouse_x, mouse_y)) != self.current_cursor:
              self.current_cursor = list((mouse_x, mouse_y))
              return list((mouse_x+1, mouse_y+1))
        elif event.type == MOUSEBUTTONDOWN:
          return ' '

  def quit(self):
    pygame.quit()
