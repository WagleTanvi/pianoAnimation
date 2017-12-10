__author__ = 'Tanvi'

import pygame# pygame is a gaming module with things built in to make game coding easier
import time
pygame.init()  # init is short for initialize... it initializes the game and all the modules available for you to use

gameDisplay = pygame.display.set_mode((800,600)) # creates a display and returns a surface object
gameDisplay.fill((255,255,255))
gameExit = False
black = (0,0,0)
lightblack = (48,48,48)
white = (255,255,255)
gray = (218,218,218)
lightgray = (235,235,235)
colors = {'keyOne': gray, 'keyTwo': gray, 'keyThree': gray, 'keyFour': gray,'keyFive': black, 'keySix': black, 'keySeven': black}

def writeScreen(message,color,xLoc,yLoc,size):
    myfont = pygame.font.SysFont( "comicsansms", size)
    text = myfont.render(message,True, color)
    gameDisplay.blit(text, [xLoc,yLoc])

def drawBoard () :
    #gameDisplay.fill(white)
    writeScreen("My Piano",black,350,80,30)
    pygame.draw.rect(gameDisplay,colors['keyOne'], (200,150,100,300),0)
    pygame.draw.rect(gameDisplay,black, (200,150,100,300),1)
    pygame.draw.rect(gameDisplay,colors['keyTwo'], (300,150,100,300),0)
    pygame.draw.rect(gameDisplay,black, (300,150,100,300),1)
    pygame.draw.rect(gameDisplay,colors['keyThree'], (400,150,100,300),0)
    pygame.draw.rect(gameDisplay,black, (400,150,100,300),1)
    pygame.draw.rect(gameDisplay,colors['keyFour'], (500,150,100,300),0)
    pygame.draw.rect(gameDisplay,black, (500,150,100,300),1)
    pygame.draw.rect(gameDisplay,colors['keyFive'], (275,150,50,150),0)
    pygame.draw.rect(gameDisplay,colors['keySix'], (375,150,50,150),0)
    pygame.draw.rect(gameDisplay,colors['keySeven'], (475,150,50,150),0)

def playSound(name):
    effect = pygame.mixer.Sound(name)
    effect.play()

# Example of flashing key
def flashKeyOne():
    colors['keyOne'] = lightgray
    time.sleep(0.5)
    drawBoard()
    playSound("Jump.wav")
    pygame.display.update()
    time.sleep(0.5)
    colors['keyOne'] = gray
    drawBoard()
    pygame.display.update()
def flashKeyTwo():
    colors['keyTwo'] = lightgray
    time.sleep(0.5)
    drawBoard()
    playSound("LowBeep.wav")
    pygame.display.update()
    time.sleep(0.5)
    colors['keyTwo'] = gray
    drawBoard()
    pygame.display.update()
def flashKeyThree():
    colors['keyThree'] = lightgray
    time.sleep(0.5)
    drawBoard()
    playSound("MediumBeep.wav")
    pygame.display.update()
    time.sleep(0.5)
    colors['keyThree'] = gray
    drawBoard()
    pygame.display.update()
def flashKeyFour():
    colors['keyFour'] = lightgray
    time.sleep(0.5)
    drawBoard()
    playSound("Beep.wav")
    pygame.display.update()
    time.sleep(0.5)
    colors['keyFour'] = gray
    drawBoard()
    pygame.display.update()
def flashKeyFive():
    colors['keyFive'] = lightblack
    time.sleep(0.5)
    drawBoard()
    playSound("Chime.wav")
    pygame.display.update()
    time.sleep(0.5)
    colors['keyFive'] = black
    drawBoard()
    pygame.display.update()
def flashKeySix():
    colors['keySix'] = lightblack
    time.sleep(0.5)
    drawBoard()
    playSound("Mario.wav")
    pygame.display.update()
    time.sleep(0.5)
    colors['keySix'] = black
    drawBoard()
    pygame.display.update()
def flashKeySeven():
    colors['keySeven'] = lightblack
    time.sleep(0.5)
    drawBoard()
    playSound("ping.wav")
    pygame.display.update()
    time.sleep(0.5)
    colors['keySeven'] = black
    drawBoard()
    pygame.display.update()

while gameExit == False:
    drawBoard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit= True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()
            if (mx > 200 and mx < 275 and my< 450 and my> 150) or (mx > 200 and mx < 300 and my< 450 and my> 300):
                flashKeyOne()
            if (mx > 325 and mx < 375 and my< 450 and my> 150) or (mx > 300 and mx < 400 and my< 450 and my> 300):
                flashKeyTwo()
            if (mx > 425 and mx < 475 and my< 450 and my> 150) or (mx > 400 and mx < 500 and my< 450 and my> 300):
                flashKeyThree()
            if (mx > 525 and mx < 500 and my< 450 and my> 150) or (mx > 500 and mx < 600 and my< 450 and my> 300):
                flashKeyFour()
            if (mx > 275 and mx < 325 and my< 300 and my> 150):
                flashKeyFive()
            if (mx > 375 and mx < 425 and my< 300 and my> 150):
                flashKeySix()
            if (mx > 475 and mx < 525 and my< 300 and my> 150):
                flashKeySeven()

    pygame.display.update()
pygame.quit()  # de-initializes the pygame module
quit()  # quits the window

