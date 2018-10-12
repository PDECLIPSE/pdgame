import pygame
from pygame.locals import *
pygame.init()

FPS = 30
WINDOWWIDTH = 720  # 720
WINDOWHEIGHT = 460  # 460

#COLORS
BLACK = (  0,  0,  0)
WHITE = (255,255,255)
GREEN = (  0,255,  0)

#image objects    
doorImageSurf = pygame.load('doorimage')  #문 이미지 넣을 것
item1 = pygame.load('ddd')
item2 = pygame.load('ddds')

#mapData
mapDataList = ({'ground':[(0,0),(WINDOWWIDTH,WINDOWHEIGHT*0.2)]]
                ,'item' :[((0,0),---)]  #이미지 파일 넣을것
                ,'door' :[((0,0),1)]
                ,'spawn':[(0,0)]},
               {'ground':[((0,0),(WINDOWWIDTH,WINDOWHEIGHT))]
                ,'item' :[((0,0),---)]  #이미지 파일 넣을 것
                ,'door' :[((0,0),1)]
                ,'spawn':[(0,0)]})



def main():
    global FPSCLOCK, SCREEN
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('test')

    
    activeTitle()
    activeGame()

def activeTitle():
    pass

def activeGame():
    playerLocation = [0,0]
    mapCode = 0
    while True:


def drawAll(mapCode,surf):  #surf에 모든 이미지를 그려넣는다.
    for ground in mapDataList[mapCode]['ground']:
        Rect=pygame.rect(ground[0],ground[1])
        pygame.draw.rect(surf, (0,0,0,0), Rect)
    for item in mapDataList[mapCode]['item']:
        surf.blit(item[1],itme[0])
    for door in mapDataList[mapCode]['door']:
        surf.blit(doorImageSurf,door[0])








        

