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

ok_img=pg.image.load("ok.png")
end_img=pg.image.load("end.png")

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
    global plan_click
    pg.display.update()
    plan_click=0


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
    global plan_click
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
    def event(self):
        global plan
        if plan[self.plan_me]!=self.plan_num:
            plan[self.plan_me]=self.plan_num
        else:
            plan[self.plan_me]=0
        make_plan()

    



class data_making():
    def __init__(self):
        self.day = 1
        self.hp = 10
        self.strength = 5
        self.tec = 5
        self.stress = 10
        self.dung = 50


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
    global plan_click
    white_window.blit()
    blit_text(board, "아침저녁 일정을 전부 체크하여 일정을 짜자.", font)
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
    ok_button.blit()

def ok_click():
    global plan
    global text
    global talk
    global data
    if plan[0] ==0 or plan[1]==0:
        blit_text(board, "전부 채크해야 한다", font)
        print("전부 채크해야 한다")
    else:
        data.day+=1
        blit_text(board, "훈련을 시작했다", font)

        if data.dung<30:
            weight = 0.5
        elif data.dung>79:
            weight = 0.1
        else:
            weight = 1
        if plan[0]==4:
            data.dung = 0
            text = text +["아침에는 먼지나게 팼다. 분충도가 0이 되었다."]
        elif plan[0]==3:
            print("w",weight)
            tec_up = int(20*weight)
            data.dung +=30
            data.tec+=tec_up
            text = text +["아침 스파링 결과 기술이" +str(tec_up)+ "올랐고,  분충도가 30 올랐다."]
        elif plan[0]==2:
            strength_up = int(20*weight)
            data.dung +=10
            data.strength+=strength_up
            text = text +["아침 근력훈련 결과 힘이" +str(strength_up)+ "올랐고,  분충도가 30 올랐다."]
        elif plan[0]==1:
            hp_up = int(20*weight)
            data.dung +=10
            data.hp+=hp_up
            text = text +["아침 체력훈련 결과 HP가" +str(hp_up)+ "올랐고,  분충도가 30 올랐다."]
        if data.dung<30:
            weight = 0.5
        elif data.dung>79:
            weight = 0.1
        else:
            weight = 1
        if plan[1]==4:
            data.dung = 0
            text = text +["저녁에는 먼지나게 팼다. 분충도가 0이 되었다."]
        elif plan[1]==3:
            print("w",weight)
            tec_up = int(20*weight)
            data.dung +=30
            data.tec+=tec_up
            text = text +["저녁 스파링 결과 기술이" +str(tec_up)+ "올랐고,  분충도가 30 올랐다."]
        elif plan[1]==2:
            strength_up = int(20*weight)
            data.dung +=10
            data.strength+=strength_up
            text = text +["저녁 근력훈련 결과 힘이" +str(strength_up)+ "올랐고,  분충도가 10 올랐다."]
        elif plan[1]==1:
            hp_up = int(20*weight)
            data.dung +=10
            data.hp+=hp_up
            text = text +["저녁 체력훈련 결과 HP가" +str(hp_up)+ "올랐고,  분충도가 10 올랐다."]
    talk = True

def ending():
    global end
    global text
    ed_text = ["드디어 그 날이 왔다.", "후타바 공원 배 실장 격투기 대회. 위키세계어는 이 날을 위해 훈련해 왔다."]
    if data.strength+data.hp+data.tec >250 and data.strength>70 and data.hp>70 and data.tec>70:
        ed_text+=["위키세계어는 탈실장적 싸움실력으로 정상에 섰다.", "위키세계어의 우승을 확인한 우리들은 위키세계어를 기절시켰다.", "원래 우승한 실장석은 전골로 끓여먹는게 이 대회의 전통이었기 때문이다.", "그렇게 위키세계어는 나의 피가 되고 살이 되었다.", "고마워 위키세계어."]
    else:
        ed_text+=["위키세계어는 결국 지고 말았다. 팔 다리가 잘린 체로 나를 향해 무언가를 원하는 듯한 눈빛을 보냈다.", "살려주기라도 원하는 건가?", "빠직!", "나는 그 자리에서 위키세계어를 신발로 뭉개버렸다.", "쓸모없는 녀석"]
    text+=ed_text
    end = 1
    
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

ok_button = icon_making(ok_img, (150,250))
ok_button.event = ok_click

plan_list = []

plan_click = 0

plan_list.append(m_hp_training_icon)
plan_list.append(m_strength_training_icon)
plan_list.append(m_tec_training_icon)
plan_list.append(m_hit_icon)
plan_list.append(e_hp_training_icon)
plan_list.append(e_strength_training_icon)
plan_list.append(e_tec_training_icon)
plan_list.append(e_hit_icon)
plan_list.append(ok_button)




end = 0
update()
            
while True:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if text==[] and end ==1:
                board.blit(end_img,(0,0))
                pg.display.update()
            if data.day == 10 and end == 0:
                ending()
            if talk == True:
                if text==[]:
                    board_start()
                    update()
                    talk = False
                else:
                    blit_text(board, text[0], font)
                    update()
                    del text[0]
                
            mouse = pg.mouse.get_pos()
            for button in buttons:
                if button.col.collidepoint(mouse):
                    button.event()
                    update()
                    if button == plan_button:
                        plan_click=1
            if plan_click==1:
                for button in plan_list:
                    if button.col.collidepoint(mouse):
                        button.event()
                        update()
                        plan_click=1
