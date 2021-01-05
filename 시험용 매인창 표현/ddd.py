import pygame as pg
import pandas as pd
import numpy as np


pg.init()
font =pg.font.Font('maple.ttf', 20)
dark = pg.image.load("dark_500_500.png")

status_button_img = pg.image.load("see_status.png")
base_window = pg.image.load("base_window.png")
close_button = pg.image.load("close_button.png")

board = pg.display.set_mode((500,500))
board.blit(dark,(0,0))
pg.display.update()

def update():
    pg.display.update()

class icon():
    def __init__(self, img, xy):
        self.img = img
        self.xy = xy
        self.x = xy[0]
        self.y = xy[1]
        self.col = img.get_rect(topleft= xy)
    def blit(self):
        board.blit(self.img, self.xy)
    def click_event(self, event):
        self.event = event
class window(icon):
    def blit(self):
        global buttons
        self.cxy = (self.x+240,self.y)
        board.blit(self.img, self.xy)
        close = icon(close_button, self.cxy)
        close.event = close_window
        buttons.append(close)
        close.blit()
        

def board_start():
    board.blit(dark,(0,0))
    status_button.blit()
def status_window_open():
    status_window.blit()
def close_window():
    global buttons
    del buttons[-1]
    board_start()

status_button= icon(status_button_img, (330,20))
status_button.event = status_window_open
status_window = window(base_window, (20,20))
  
################
board_start()
#status_window_open()
update()

buttons =[status_button]
            
while True:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse = pg.mouse.get_pos()
            for button in buttons:
                if button.col.collidepoint(mouse):
                    button.event()
                    update()
