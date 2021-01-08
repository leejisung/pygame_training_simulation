import pygame as pg
import pandas as pd
import numpy as np
import random


pg.init()
font =pg.font.Font('maple.ttf', 20)
talk_data = pd.read_csv('대사집.csv', encoding='CP949')
talk_data= talk_data.replace(np.nan, 0) 


dark = pg.image.load("dark_500_500.png")
status_button_img = pg.image.load("see_status.png")
talk_button_img = pg.image.load("talk.png")
plan_button_img = pg.image.load("make_plan.png")
save_button_img = pg.image.load("save.png")
base_window = pg.image.load("base_window.png")
close_button = pg.image.load("close_button.png")
text_window = pg.image.load("white_460_110.png")

hp_training_icon_img=pg.image.load("hp_training_icon.png")
strength_training_icon_img=pg.image.load("strength_training_icon.png")
tec_training_icon_img=pg.image.load("tec_training_icon.png")
hit_icon_img=pg.image.load("hit_icon.png")
hp_training_icon_check_img=pg.image.load("hp_training_icon_check.png")
strength_training_icon_check_img=pg.image.load("strength_training_icon_check.png")
tec_training_icon_check_img=pg.image.load("tec_training_icon_check.png")
hit_icon_check_img=pg.image.load("hit_icon_check.png")

hp_training_icon_img = pg.transform.scale(hp_training_icon_img,(50,50))
strength_training_icon_img = pg.transform.scale(strength_training_icon_img,(50,50))
tec_training_icon_img = pg.transform.scale(tec_training_icon_img,(50,50))
hit_icon_img = pg.transform.scale(hit_icon_img,(50,50))
hp_training_icon_check_img = pg.transform.scale(hp_training_icon_check_img,(50,50))
strength_training_icon_check_img = pg.transform.scale(strength_training_icon_check_img,(50,50))
tec_training_icon_check_img = pg.transform.scale(tec_training_icon_check_img,(50,50))
hit_icon_check_img = pg.transform.scale(hit_icon_check_img,(50,50))




board = pg.display.set_mode((500,500))
board.blit(dark,(0,0))
pg.display.update()

def update():
    pg.display.update()

def list_talk(name): 
    talk= list(talk_data[name]) 
    while(talk[-1] ==0): 
        del talk[-1] 
    return talk

def blit_text(surface, text, font):
    color=pg.Color('black')
    surface.blit(text_window, (20, 370))
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = (450, 450)
    x, y = (30, 380)
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = 30
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = 30
        y += word_height  # Start on new row.

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
        
class plan_icon_making():
    global plan
    def __init__(self, img, img2, xy, plan_num, plan_me):
        self.img = img
        self.img2 = img2
        self.xy = xy
        self.x = xy[0]
        self.y = xy[1]
        self.col = img.get_rect(topleft= xy)
        self.plan_num = plan_num
        self.plan_me = plan_me
    def blit(self):
        if self.plan_num== plan[self.plan_me]:
            board.blit(self.img2, self.xy)
        else:
            board.blit(self.img, self.xy)
    def click(self):
        global plan
        if plan[self.plan_me]!=self.plan_num:
            plan[self.plan_me]=self.plan_num
            print(0)
        else:
            plan[self.plan_me]=0
        print(self.blit)
        self.blit()
        update()
    



class data_making():
    def __init__(self):
        self.day = 1
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
    save_button.blit()
    dd = pg.font.Font('maple.ttf', 40)
    day = dd.render("DAY "+str(data.day),True,(255,255,255))
    board.blit(day,(330,240))

    
def status_window_open():
    board_start()
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

def make_plan():
    white_window.blit()
    blit_text(board, "3개 일정을 전부 체크하여 일정을 짜자.", font)
    name = font.render("일정표",True,(255,255,255))
    up_text = font.render("아침일정",True,(0,0,0))
    down_text = font.render("저녁일정",True,(0,0,0))
    board.blit(up_text,(50,50))
    board.blit(down_text,(50,150))
    m_hp_training_icon.blit()
    m_strength_training_icon.blit()
    m_tec_training_icon.blit()
    m_hit_icon.blit()
    e_hp_training_icon.blit()
    e_strength_training_icon.blit()
    e_tec_training_icon.blit()
    e_hit_icon.blit()
def save_window():
    white_window.blit()

def talk_with_wiki():
    global talk
    if data.dung<30:
        xx= list_talk("30under")
    elif data.dung>79:
        xx = list_talk("80over")
    else:
        xx = list_talk("30_80")
    xx= random.choice(xx)
    board_start()
    blit_text(board, xx, font)
    talk = True
    
def close_window():
    global buttons
    del buttons[-1]
    board_start()
data = data_making()

status_button= icon_making(status_button_img, (330,20))
plan_button= icon_making(plan_button_img, (330,70))
talk_button= icon_making(talk_button_img, (330,120))
save_button= icon_making(save_button_img, (330,170))

status_button.event = status_window_open
plan_button.event = make_plan
talk_button.event = talk_with_wiki
save_button.event = save_window

white_window = window_making(base_window, (20,20))
  
################
board_start()
update()
text = []
talk = False
buttons =[status_button, talk_button, plan_button, save_button]

plan = [0,0]
m_hp_training_icon = plan_icon_making(hp_training_icon_img, hp_training_icon_check_img, (50,70),1,0)
m_strength_training_icon = plan_icon_making(strength_training_icon_img, strength_training_icon_check_img, (100,70),2,0)
m_tec_training_icon = plan_icon_making(tec_training_icon_img, tec_training_icon_check_img, (150,70),3,0)
m_hit_icon = plan_icon_making(hit_icon_img, hit_icon_check_img, (200,70),4,0)

e_hp_training_icon = plan_icon_making(hp_training_icon_img, hp_training_icon_check_img, (50,170),1,1)
e_strength_training_icon = plan_icon_making(strength_training_icon_img, strength_training_icon_check_img, (100,170),2,1)
e_tec_training_icon = plan_icon_making(tec_training_icon_img, tec_training_icon_check_img, (150,170),3,1)
e_hit_icon = plan_icon_making(hit_icon_img, hit_icon_check_img, (200,170),4,1)


plan_list = []

plan_list.append(m_hp_training_icon)
plan_list.append(m_strength_training_icon)
plan_list.append(m_tec_training_icon)
plan_list.append(m_hit_icon)

print(plan_list)


update()
            
while True:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:

            if talk == True:
                if text==[]:
                    board_start()
                    update()
                    talk = False
                else:
                    blit_text(board, text[0], font)
                
            mouse = pg.mouse.get_pos()
            for button in buttons:
                if button.col.collidepoint(mouse):
                    button.event()
                    update()
