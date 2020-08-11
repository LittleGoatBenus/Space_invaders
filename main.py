import pygame
import random
import math
import time
import os




(width, height) = (800, 600) # delcaring window dimensions

screen = pygame.display.set_mode((width, height)) #calling dimensions and creating screen

#title and icon
pygame.display.set_caption('GAME') #name of window
icon = pygame.image.load(os.path.join('assets','crow.png')) #to set an icon
pygame.display.set_icon(icon) #displaying an icon

#score

score = 0

#Background
#background = pygame.image.load(os.path.join('assets', 'BG.png') #if you want a background in the while loop add a backrgound image of 800 by 600 then type the command





#boss alien
bossimg = pygame.image.load(os.path.join('assets','boss.png'))  #loading the alien image in
bossx = 750 #the coordinates
bossy = 50

def boss(x, y):
    screen.blit(bossimg, (bossx, bossy)) #drawing an image blit class

#alien bullets

alienbullet = pygame.image.load(os.path.join('assets', 'alienbullet.png'))

#alien 1


alienimg = pygame.image.load(os.path.join('assets','alien.png'))
alienx = random.randint(0,800)
alieny = random.randint(50,150)
alienchangex = 0.15 #the movement of enemy in x direction left to right
alienchangey = 20 # the movement in y direction , down if a boundry is hit, game over if enemy touches player


def alien(x,y):
    screen.blit(alienimg, (x, y)) #blit is the command to draw images

#alien2
alien2img = pygame.image.load(os.path.join('assets', 'alien2.png'))

#alien3

alien3img = pygame.image.load(os.path.join('assets', 'alien3.png'))

#bullet
bulletimg = pygame.image.load(os.path.join('assets','bullet.png'))
bulletx = 0
bullety = 550
bulletx = 0 # this will be needed to save x value of where bullet is fired
bulletchangey = 3 #bullet velocity
bulletload = "load" # bulletload is at load



def bulletfire(x,y):
    global bulletload #allows variable to be called oitside functions
    bulletload = "shoot" # if space is pressed function is called, and ulletload changes to shoot, which triggers an if statement
    screen.blit(bulletimg, (x, y+10)) #the point of where the bullet is fired




#ship
shipimg = pygame.image.load(os.path.join('assets','ship.png'))
shipx = 370
shipy = 550
shipchangex = 0



def ship(x,y):
    screen.blit(shipimg, (x, y))




pygame.display.flip()

running = True # to create an infinite loop

while running: # ininite loop so window doesnt close

    screen.fill((0,0,0))#screen colour, this is r , g, b

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if statement for if (x) is pressed closes window
          running = False #breaks infinite loop


    #movements on keyboard
        #if the arrow key is pressed the ship will move according to the if staement
        if event.type == pygame.KEYDOWN: #if a key is pressed

            if event.key == pygame.K_SPACE:
                if bulletload is "load": #this prevents bullets to be spammed
                    bulletx = shipx
                    bulletfire(bulletx, bullety)
                    print("FIRE")

            if event.key == pygame.K_LEFT: #if left arrow is pressed
                shipchangex = -0.4 #the pixle moves -0.1 on x axis
                print("LEFT")
            if event.key == pygame.K_RIGHT: # the >K_RIGHT stands for keyright
                shipchangex = 0.4
                print("RIGHT")




        if event.type == pygame.KEYUP: #If a key was released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #if left or right released no movement
                shipchangex = 0 #if key is released no movement is made




#bullet movements
    #this allows multiple bullets to be fired

    if bullety <= 0: #if the bullet reaches 0 on an axis
        bullety = 550 #the bullet image goes back to original point of 550
        bulletload = "load" #the state of the bullet is reseet



    if  bulletload == "shoot":#if the function is called then shoot is bulletload which triggers this if statement
        bulletfire(bulletx, bullety) #bullet is called and the values are sent to the function
        bullety -= bulletchangey

 # colision
    if (bulletx, bullety) is (alienx, alieny):
        score += 1
        bullety = 550
        bulletload = "load"
        print(score)


#ship movement
    shipx += shipchangex # if the arrow is pressed the ships x axis will change by 0.1

    if shipx <= 0: # boundries so ship doesnt go out the srcreen window
        shipx = 0
    elif shipx >= 736: #image is 64 pixel
        shipx = 736



        #alien 1 movement
    alienx += alienchangex

    if alienx <= 0: # makeing sure enemy doesnt go out the boundry
        alienchangex = 0.15 # the alien moves at 0.15 pixels
        alieny +=alienchangey


    elif alienx >= 736:
        alienchangex = -0.15
        alieny += alienchangey




# the sprites
    alien(alienx, alieny)#calling all the characters in the game
    ship(shipx, shipy)
    boss(bossx, bossy)

    pygame.display.update() #updates the display/window to colour
