import pygame as pg
import pandas as pd
import numpy as np

d = pd.read_csv('시험용 대사집.csv', encoding='CP949') 
d = d.replace(np.nan, 0) 

pg.init()
font =pg.font.Font('maple.ttf', 20)
TEXT_WINDOW = pg.image.load("white_460_110.png")
dark = pg.image.load("dark_500_500.png")
board = pg.display.set_mode((500,500))
board.blit(dark,(0,0))
pg.display.update()

def update():
    pg.display.update()


def list_talk(name): 
    talk= list(d[name]) 
    while(talk[-1] ==0): 
        del talk[-1] 
    return talk

def blit_text(surface, text, font):
    color=pg.Color('black')
    surface.blit(TEXT_WINDOW, (20, 370))
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
TALK = False
TEXT = []

#시범
TEXT = list_talk("디지몬")
TALK = True
        
while True:
    if TEXT == []:
        TALK = False
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN and TALK == True:
            blit_text(board, TEXT[0], font)
            del TEXT[0]
        if event.type == pg.MOUSEBUTTONDOWN and TALK == False:
            board.blit(dark,(0,0))
        update()

            
            
