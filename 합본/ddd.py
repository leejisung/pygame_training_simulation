import pygame as pg
import pandas as pd
import numpy as np


pg.init()
font =pg.font.Font('maple.ttf', 20)
dark = pg.image.load("dark_500_500.png")

status_button_img = pg.image.load("see_status.png")
talk_button_img = pg.image.load("talk.png")
plan_button_img = pg.image.load("make_plan.png")
base_window = pg.image.load("base_window.png")
close_button = pg.image.load("close_button.png")

board = pg.display.set_mode((500,500))
board.blit(dark,(0,0))
pg.display.update()

def update():
    pg.display.update()

class icon_making():
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
class window_making(icon_making):
    def blit(self):
        global buttons
        self.cxy = (self.x+240,self.y)
        board.blit(self.img, self.xy)
        close = icon_making(close_button, self.cxy)
        close.event = close_window
        buttons.append(close)
        close.blit()
class data_making():
    def __init__(self):
        self.hp = 10
        self.strength = 5
        self.tec = 5
        self.stress = 10
        self.dung = 50
        self.day = 1

def board_start():
    board.blit(dark,(0,0))
    status_button.blit()
    plan_button.blit()
    talk_button.blit()
def status_window_open():
    white_window.blit()
    name = font.render("상태창",True,(255,255,255))
    hp = font.render("HP: "+str(data.hp),True,(0,0,0))
    strength = font.render("힘: "+str(data.strength),True,(0,0,0))
    tec = font.render("기술: "+str(data.tec),True,(0,0,0))
    stress = font.render("스트레스: "+str(data.stress),True,(0,0,0))
    dung = font.render("분충도: "+str(data.dung),True,(0,0,0))
    board.blit(name,(20,20))
    board.blit(hp,(40,60))
    board.blit(strength,(40,80))
    board.blit(tec,(40,100))
    board.blit(stress,(40,120))
    board.blit(dung,(40,140))
def close_window():
    global buttons
    del buttons[-1]
    board_start()
data = data_making()
status_button= icon_making(status_button_img, (330,20))
plan_button= icon_making(plan_button_img, (330,70))
talk_button= icon_making(talk_button_img, (330,120))

status_button.event = status_window_open
white_window = window_making(base_window, (20,20))
  
################
board_start()
update()

buttons =[status_button, talk_button, plan_button]
            
while True:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse = pg.mouse.get_pos()
            for button in buttons:
                if button.col.collidepoint(mouse):
                    button.event()
                    update()
