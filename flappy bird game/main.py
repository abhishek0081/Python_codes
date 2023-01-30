from math import trunc
import random  # for generating random numbers
import sys  # we will use sys.exit() to exit the program
import pygame
from pygame.locals import *
# basic pygame imports 
# Global variables for the game
FPS = 10
SCREENWIDTH = 288
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT*0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER     = "gallery/sprites/bird.png"
BACKGROUND = "gallery/sprites/background.png"
PIPE       = "gallery/sprites/pipe.png"

def welcomeScreen():
    """
    Shows Welcome Screen to the user
    """
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT-GAME_SPRITES["player"].get_height())/2)
    messagex = int((SCREENHEIGHT-GAME_SPRITES["message"].get_height())/3.7)
    messagey = int(SCREENHEIGHT*0.25)
    basex = 0
    while True:
        for event in pygame.event.get():
            #  if user clicks cross button cross the game
            if event.type  ==  QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
                #  if the user presses spacr or up kay ,start the game
            elif event.type == KEYDOWN and(event.key == K_SPACE or event.key == K_UP):
                return
            else:

                SCREEN.blit(GAME_SPRITES["background"],(0,0))
                SCREEN.blit(GAME_SPRITES["player"],(playerx,playery))
                SCREEN.blit(GAME_SPRITES["message"],(messagex,messagey))
                SCREEN.blit(GAME_SPRITES["base"],(basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score =0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0
    #  create 2 pipes to blitting on screen
    newPipe11 = getRandomPipe()
    newPipe12 = getRandomPipe()
    # list of upper pipe
    upperPipes =[
        {"x":SCREENWIDTH+200,"y":newPipe11[0]["y"]},
        {"x":SCREENWIDTH+200+(SCREENWIDTH/2),"y":newPipe12[0]["y"]}
    ]
    # my list of lower pipes
    lowerPipes =[
        {"x":SCREENWIDTH+200,"y":newPipe11[1]["y"]},
        {"x":SCREENWIDTH+200+(SCREENWIDTH/2),"y":newPipe12[1]["y"]}
    ]
    pipeVelX = -4
    playerVelY = -9
    PlayerMaxVelY = 10
    PlayerMixVelY = -8
    playerAccY =1
    playerFlapACcv = -8 # valocity while Flapping
    playerFlapped = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or(event.type== KEYDOWN and event.key==K_ESCAPE):
                pygame.exit()
                sys.exit()
            if event.type == KEYDOWN and(event.key ==K_SPACE or event.key == K_UP):
                if playery>0:
                    playerVelY = playerFlapACcv
                    playerFlapped= True
                    GAME_SOUNDS["wing"].play()

        crashTest = isCollide(playerx,playery,upperPipes,lowerPipes)
        if crashTest:
            return
        # check for score
        playerMidPos = playerx + GAME_SPRITES["player"].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe["x"] +GAME_SPRITES["pipe"][0].get_width()/2
            if pipeMidPos<=playerMidPos<pipeMidPos+4:
                score+=1
                print(f"Your score is{score}")
                GAME_SOUNDS["point"].play()
        
        if playerVelY < PlayerMaxVelY and not playerFlapped:
            playerVelY += playerAccY
        if playerFlapped:
            playerFlapped  = False
        playerHeight = GAME_SPRITES["player"].get_height()
        playery += min(playerVelY,GROUNDY-playery-playerHeight)

        # move pipes to the left
        for upperPipe,lowerPipe in zip(upperPipes,lowerPipes):
            upperPipe["x"]+=pipeVelX
            lowerPipe["x"]+=pipeVelX
        # ADD a new pipe when the first is about to cross the leftmiost of the screen
        if  0<upperPipes[0]["x"]<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])
            # if pipe is out of screen remove it
        if upperPipes[0]["x"] < -GAME_SPRITES["pipe"][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        for upperPipe,lowerPipe in zip(upperPipes,lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],(upperPipe["x"],upperPipe["y"]))
            SCREEN.blit(GAME_SPRITES['pipe'][1],(lowerPipe["x"],lowerPipe["y"]))
            
        SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))

        myDigits =[int(x) for x in list(str(score))]
        width =0
        for digit in myDigits:
            width += GAME_SPRITES["numbers"][digit].get_width()
        Xoffset =(SCREENWIDTH - width)/2
        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES["numbers"][digit],(Xoffset,SCREENHEIGHT*0.12))
            # SCREEN.blit(GAME_SPRITES["numbers"][digit],(Xoffset,SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES["numbers"][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx,playery,upperPipes,lowerPipes):
    if playery >( GROUNDY -25 or playery < 0):
        GAME_SOUNDS["hit"].play()
        return True
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES["pipe"][0].get_height()
        if((playery < pipeHeight + pipe["y"] and  abs(playerx - pipe["x"]) < GAME_SPRITES["pipe"][0].get_width())):
            GAME_SOUNDS["hit"].play()
            return True
    for pipe in lowerPipes:
        if (playery + GAME_SPRITES["player"].get_height() > pipe["y"]) and abs(playerx - pipe["x"]) < GAME_SPRITES["pipe"][0].get_width():
            GAME_SOUNDS["hit"].play()
            return True           
    return False



def getRandomPipe():
    """
    Generate positions of two pipes(on bottom straight and one top rotated) for blitting on the screen
    """
    pipeHeight = GAME_SPRITES["pipe"][0].get_height()
    offset =  SCREENHEIGHT/3
    y2 = offset+random.randrange(0,int(SCREENHEIGHT - GAME_SPRITES["base"].get_height()-1.2*offset))
    pipeX = SCREENWIDTH+10
    y1 =  pipeHeight-y2+offset
    pipe =[
        {"x":pipeX,"y":-y1},
        {"x":pipeX,"y":y2}
    ]
    return pipe
if __name__ == "__main__":
    # THIS WILL BE THE MAIN POINT FROM WHERE OUR GAME WILL START
    pygame.init() # INITIALIZE ALL PYGAMES MODULES
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("FLAPPY BIRD BY ABHISHEK")
    GAME_SPRITES["numbers"]=(
        pygame.image.load("gallery/sprites/0.png").convert_alpha(),
        pygame.image.load("gallery/sprites/1.png").convert_alpha(),
        pygame.image.load("gallery/sprites/2.png").convert_alpha(),
        pygame.image.load("gallery/sprites/3.png").convert_alpha(),
        pygame.image.load("gallery/sprites/4.png").convert_alpha(),
        pygame.image.load("gallery/sprites/5.png").convert_alpha(),
        pygame.image.load("gallery/sprites/6.png").convert_alpha(),
        pygame.image.load("gallery/sprites/7.png").convert_alpha(),
        pygame.image.load("gallery/sprites/8.png").convert_alpha(),
        pygame.image.load("gallery/sprites/9.png").convert_alpha()
    )

    GAME_SPRITES["message"] = pygame.image.load("gallery/sprites/message.png").convert_alpha()
    GAME_SPRITES["base"]    = pygame.image.load("gallery/sprites/base.png").convert_alpha()
    GAME_SPRITES["pipe"] = (
        pygame.transform.rotate(pygame.image.load("gallery/sprites/pipe.png").convert_alpha(),180),
        pygame.image.load("gallery/sprites/pipe.png").convert_alpha()
    )
# GAME SOUNDS
    GAME_SOUNDS["die"]    = pygame.mixer.Sound("gallery/audio/die.wav")
    GAME_SOUNDS["hit"]    = pygame.mixer.Sound("gallery/audio/hit.wav")
    GAME_SOUNDS["point"]  = pygame.mixer.Sound("gallery/audio/point.wav")
    GAME_SOUNDS["swoosh"] = pygame.mixer.Sound("gallery/audio/swoosh.wav")
    GAME_SOUNDS["wing"]   = pygame.mixer.Sound("gallery/audio/wing.wav")
    GAME_SPRITES["background"] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES["player"] = pygame.image.load(PLAYER).convert_alpha()



    while True:
        welcomeScreen() # shows welcome screen to the user until user press any button
        mainGame()# This is main game error


