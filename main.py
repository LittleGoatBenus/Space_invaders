import pygame
import os
import random
import pygame.freetype

#initialising pygame
pygame.init()
pygame.font.init()
#screen
(width, height) = (800, 600)

#scree
screen = pygame.display.set_mode((width, height))


#title and icon
pygame.display.set_caption('invaders') #name of window
icon = pygame.image.load(os.path.join('assets','crow.png')) #to set an icon
pygame.display.set_icon(icon) #displaying an icon

#colours
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# text



# lives



#classes

#spaceship

vel = 4 #speed of ship
velr = 4 #velocity to right

class SpaceShip(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets','ship.png')) #calling the spaceship image in assets folder
        self.rect = self.image.get_rect()
        self.health = 3 # the amount of lives the spaceship has

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y)) # the x and y coordinates of the spaceship

class Lives(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets','ship.png')) #calling the spaceship image in assets folder
        self.rect = self.image.get_rect()
        self.health = 3 # the amount of lives the spaceship has

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y)) # the x and y coordinates of the spaceship


#alien
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets','alien.png'))
        self.rect = self.image.get_rect()
        self.group_rect = pygame.Rect(130, 75, 100,100) # first coordinate where first enemy on left starts, second covers all aliens in the area
        self.direction = 1 # speed
    def update(self):
        self.rect.x += self.direction
        self.group_rect.x += self.direction
        if self.group_rect.x + 500 >= 775: # if grouprectangle passes coordinate 775
            self.direction = -self.direction # change direction to negative
            self.rect.y += 10 # moves down 5 pixles in y direction
        if self.group_rect.x <= 25:
            self.direction = -self.direction
            self.rect.y += 10 # moves down 5 pixles in y direction


#alien 2

class Alien2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets','alien2.png'))
        self.rect = self.image.get_rect()
        self.group_rect = pygame.Rect(130, 75, 100,100) # first coordinate where first enemy on left starts, second covers all aliens in the area
        self.direction = 1 # speed
    def update(self):
        self.rect.x += self.direction
        self.group_rect.x += self.direction
        if self.group_rect.x + 500 >= 775: # if grouprectangle passes coordinate 775
            self.direction = -self.direction # change direction to negative
            self.rect.y += 10 # moves down 5 pixles in y direction
        if self.group_rect.x <= 25:
            self.direction = -self.direction
            self.rect.y += 10 # moves down 5 pixles in y direction


#alien 3

class Alien3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets','alien3.png'))
        self.rect = self.image.get_rect()
        self.group_rect = pygame.Rect(130, 75, 100,100) # first coordinate where first enemy on left starts, second covers all aliens in the area
        self.direction = 1 # speed
    def update(self):
        self.rect.x += self.direction
        self.group_rect.x += self.direction
        if self.group_rect.x + 500 >= 775: # if grouprectangle passes coordinate 775
            self.direction = -self.direction # change direction to negative
            self.rect.y += 10 # moves down 5 pixles in y direction
        if self.group_rect.x <= 25:
            self.direction = -self.direction
            self.rect.y += 10 # moves down 5 pixles in y direction
#bonus ships
#class Bonus(pygame.sprite.Sprite):
#    def __init__(self):
#        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.image.load(os.path.join('assets','boss.png'))
#        self.rect = self.image.get_rect()
#        self.group_rect = pygame.Rect(130, 75, 100,100) # first coordinate where first enemy on left starts, second covers all aliens in the area
#        self.direction = 1 # speed
#    def update(self):
#        self.rect.x += self.direction
##        self.group_rect.x += self.direction
#        if self.group_rect.x + 500 >= 775: # if grouprectangle passes coordinate 775
#            self.direction = -self.direction # change direction to negative
##            self.rect.y += 10 # moves down 5 pixles in y direction
#        if self.group_rect.x <= 25:
#            self.direction = -self.direction
#            self.rect.y += 10 # moves down 5 pixles in y direction




# bunker
class Bunker(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8, 8])
        self.image.fill(green)
        self.rect = self.image.get_rect()


#spaceship laser
class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 7])
        self.image.fill(green)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += -10

#alien laser 1

class AlienLaser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 7])
        self.image.fill(red)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1


lives = Lives()
lives.rect.x = 650
lives.rect.y = 780
ship = SpaceShip()
ship.rect.x = 370 # setting x and y coordinates of space ship
ship.rect.y = 550

alien2_list = pygame.sprite.Group()
alien_list = pygame.sprite.Group()
alien3_list = pygame.sprite.Group()
bunker_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
alienlaser_list = pygame.sprite.Group()




#alien 1 list
for row in range(3, 5): # spawns 2 rows from row 4 and 5
    for column in range(0, 12): #spawns 10 enemies
        alien = Alien() # the 80 is settimng them in the middle, the 50 is spacing between each alien
        alien.rect.x = 80 + (50 * column) #spacing on x axis
        alien.rect.y = 50 + (50 * row) #spacing on y axis
        alien_list.add(alien)

#alien2 list
for row in range(5, 7): # spawns 2 rows from row 4 and 5
    for column in range(0, 12): #spawns 10 enemies
        alien2 = Alien2() # the 80 is settimng them in the middle, the 50 is spacing between each alien
        alien2.rect.x = 80 + (50 * column) #spacing on x axis
        alien2.rect.y = 50 + (50 * row) #spacing on y axis
        alien2_list.add(alien2)

#alien3 list

for row in range(1, 3): # spawns 2 rows from row 4 and 5
    for column in range(0, 12): #spawns 10 enemies
        alien3 = Alien3() # the 80 is settimng them in the middle, the 50 is spacing between each alien
        alien3.rect.x = 80 + (50 * column) #spacing on x axis
        alien3.rect.y = 50 + (50 * row) #spacing on y axis
        alien3_list.add(alien3)

#bunker list
for bunk in range(4): # spawns 4 bunkers
    for row in range(7): # splits the bunkers into smaller squares from 5 on x
        for column in range(15): # 15 on y
            bunker = Bunker() # calling bunker class
            bunker.rect.x = (50 + (200 * bunk)) + (5 * column) # start bunker at 50 pixels, each bunker spaced 215 pixels, spacing by 10
            bunker.rect.y = 500 + (5 * row)
            bunker_list.add(bunker)



def update():

    screen.fill(black)
    #lives
    lives.draw()
    #sprites
    ship.draw()
    alien_list.draw(screen)
    alien_list.update()
    alien2_list.draw(screen)
    alien2_list.update()
    alien3_list.draw(screen)
    alien3_list.update()
    bunker_list.draw(screen)
    laser_list.update()
    laser_list.draw(screen)
    alienlaser_list.update()
    alienlaser_list.draw(screen)
    pygame.display.update()


running = True # set running to true
aliensy = alien.rect.y, alien2.rect.y, alien3.rect.y

while running: # infinite loop

    pygame.time.delay(10)





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    key = pygame.key.get_pressed()# calling the pressed function

    if key[pygame.K_LEFT]: # if the left arrow is pressed
        ship.rect.x += -vel # cange the ships position by vel pixels
    if key[pygame.K_RIGHT]: # if the right arrow is pressed
        ship.rect.x += velr # change the ships position by velr pixels
    if key[pygame.K_SPACE]: # if the space bar is pressed
        if len(laser_list) < 1: # and there are less than  lasers on screen
            laser = Laser() #call the laser class
            laser.rect.x = ship.rect.x + 32 # shoot the laser from position x + 32
            laser.rect.y = ship.rect.y  # shoot the laser from position y
            laser_list.add(laser)


# shooting for alien 1
    shoot_chance = random.randint(1, 400) # a random number between 1 and 400

    if shoot_chance < 5:
        if len(alien_list) > 0: # if there are still aliens on the screen
            random_alien = random.choice(alien_list.sprites()) # choosing a random alien for bullets to come from
            alienlaser = AlienLaser()
            alienlaser.rect.x = random_alien.rect.x  # area were bullets come from
            alienlaser.rect.y = random_alien.rect.y + 25
            alienlaser_list.add(alienlaser)

#shooting chance for alien 2

    shoot_chance = random.randint(1, 800) # a random number between 1 and 800

    if shoot_chance < 5:
        if len(alien2_list) > 0: # if there are still aliens on the screen
            random_alien2 = random.choice(alien2_list.sprites()) # choosing a random alien for bullets to come from
            alienlaser = AlienLaser()
            alienlaser.rect.x = random_alien2.rect.x  # area were bullets come from
            alienlaser.rect.y = random_alien2.rect.y + 25
            alienlaser_list.add(alienlaser)

            #alien 3 shooting chance

    shoot_chance = random.randint(1, 200) # a random number between 1 and 800

    if shoot_chance < 5:
        if len(alien3_list) > 0: # if there are still aliens on the screen
            random_alien3 = random.choice(alien3_list.sprites()) # choosing a random alien for bullets to come from
            alienlaser = AlienLaser()
            alienlaser.rect.x = random_alien3.rect.x  # area were bullets come from
            alienlaser.rect.y = random_alien3.rect.y + 25
            alienlaser_list.add(alienlaser)



    for laser in laser_list: #for lasers
        if laser.rect.y < 0: # if the laser goes off scree
            laser_list.remove(laser) # this removes the laser

#alien 1
        for alien in alien_list: # if a lasr rectangle collides
            if laser.rect.colliderect(alien.rect): # with the alien rectange
                laser_list.remove(laser) # removes laser
                alien_list.remove(alien) #removes the alien
#alien 2
        for alien2 in alien2_list: # if a lasr rectangle collides
            if laser.rect.colliderect(alien2.rect): # with the alien rectange
                laser_list.remove(laser) # removes laser
                alien2_list.remove(alien2) #removes the alien

#alien 3
        for alien3 in alien3_list: # if a lasr rectangle collides
            if laser.rect.colliderect(alien3.rect): # with the alien rectange
                laser_list.remove(laser) # removes laser
                alien3_list.remove(alien3) #removes the alien


        for bunker in bunker_list: # same concept as alien rectangle collision
            if laser.rect.colliderect(bunker.rect): # if the collision of lasers rectangle with bunker rectanger
                laser_list.remove(laser) # remove the laser
                bunker_list.remove(bunker) # remove the bunker

# if the aliens touch the ships 550 coordinate game end s
    if alien.rect.y >= 550:
        alien_list.remove(alien_list)
        alien2_list.remove(alien2_list)
        alien3_list.remove(alien3_list)

    if alien2.rect.y >= 550:
        alien_list.remove(alien_list)
        alien2_list.remove(alien2_list)
        alien3_list.remove(alien3_list)


    if alien3.rect.y >= 550:
        alien_list.remove(alien_list)
        alien2_list.remove(alien2_list)
        alien3_list.remove(alien3_list)








    for alienlaser in alienlaser_list: # same concept
        if alienlaser.rect.y > 600: # removes laser if touches boundry
            alienlaser_list.remove(alienlaser)
        if alienlaser.rect.colliderect(ship.rect): # if rectangles collide
            alienlaser_list.remove(alienlaser) # the health goes down
            ship.health -= 1 # by one health
        for bunker in bunker_list: # if bunker is hit by alien laser
            if alienlaser.rect.colliderect(bunker.rect): # r
                alienlaser_list.remove(alienlaser)# remove the laser
                bunker_list.remove(bunker) #remove the bunker
# ending game
    if ship.health < 3:
        print("2 lives")
        if ship.health < 2:
            print("1 life")
            if ship.health < 1:
                print("GAME OVER")


    if len(alien_list) == 0 and len(alien2_list) == 0 and len(alien3_list) == 0:
        print("YOU WIN")


    #spaceship boundries

    if ship.rect.x <= 0: # boundries so ship doesnt go out the srcreen window
        ship.rect.x = 0
    elif ship.rect.x >= 736: #image is 64 pixel
        ship.rect.x = 736

    update()


pygame.quit()

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y)) # the x and y coordinates of the spaceship


#alien
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets','alien.png'))
        self.rect = self.image.get_rect()
        self.group_rect = pygame.Rect(130, 75, 100,100) # first coordinate where first enemy on left starts, second covers all aliens in the area
        self.direction = 1 # speed
    def update(self):
        self.rect.x += self.direction
        self.group_rect.x += self.direction
        if self.group_rect.x + 500 >= 775: # if grouprectangle passes coordinate 775
            self.direction = -self.direction # change direction to negative
            self.rect.y += 10 # moves down 5 pixles in y direction
        if self.group_rect.x <= 25:
            self.direction = -self.direction
            self.rect.y += 10 # moves down 5 pixles in y direction


#alien 2

class Alien2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets','alien2.png'))
        self.rect = self.image.get_rect()
        self.group_rect = pygame.Rect(130, 75, 100,100) # first coordinate where first enemy on left starts, second covers all aliens in the area
        self.direction = 1 # speed
    def update(self):
        self.rect.x += self.direction
        self.group_rect.x += self.direction
        if self.group_rect.x + 500 >= 775: # if grouprectangle passes coordinate 775
            self.direction = -self.direction # change direction to negative
            self.rect.y += 10 # moves down 5 pixles in y direction
        if self.group_rect.x <= 25:
            self.direction = -self.direction
            self.rect.y += 10 # moves down 5 pixles in y direction


#alien 3

class Alien3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets','alien3.png'))
        self.rect = self.image.get_rect()
        self.group_rect = pygame.Rect(130, 75, 100,100) # first coordinate where first enemy on left starts, second covers all aliens in the area
        self.direction = 1 # speed
    def update(self):
        self.rect.x += self.direction
        self.group_rect.x += self.direction
        if self.group_rect.x + 500 >= 775: # if grouprectangle passes coordinate 775
            self.direction = -self.direction # change direction to negative
            self.rect.y += 10 # moves down 5 pixles in y direction
        if self.group_rect.x <= 25:
            self.direction = -self.direction
            self.rect.y += 10 # moves down 5 pixles in y direction

# bunker
class Bunker(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8, 8])
        self.image.fill(green)
        self.rect = self.image.get_rect()


#spaceship laser
class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 7])
        self.image.fill(green)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += -10

#alien laser 1

class AlienLaser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 7])
        self.image.fill(red)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1



ship = SpaceShip()
ship.rect.x = 370 # setting x and y coordinates of space ship
ship.rect.y = 550

alien2_list = pygame.sprite.Group()
alien_list = pygame.sprite.Group()
alien3_list = pygame.sprite.Group()
bunker_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
alienlaser_list = pygame.sprite.Group()




#alien 1 list
for row in range(3, 5): # spawns 2 rows from row 4 and 5
    for column in range(0, 12): #spawns 10 enemies
        alien = Alien() # the 80 is settimng them in the middle, the 50 is spacing between each alien
        alien.rect.x = 80 + (50 * column) #spacing on x axis
        alien.rect.y = 50 + (50 * row) #spacing on y axis
        alien_list.add(alien)

#alien2 list
for row in range(5, 7): # spawns 2 rows from row 4 and 5
    for column in range(0, 12): #spawns 10 enemies
        alien2 = Alien2() # the 80 is settimng them in the middle, the 50 is spacing between each alien
        alien2.rect.x = 80 + (50 * column) #spacing on x axis
        alien2.rect.y = 50 + (50 * row) #spacing on y axis
        alien2_list.add(alien2)

#alien3 list

for row in range(1, 3): # spawns 2 rows from row 4 and 5
    for column in range(0, 12): #spawns 10 enemies
        alien3 = Alien3() # the 80 is settimng them in the middle, the 50 is spacing between each alien
        alien3.rect.x = 80 + (50 * column) #spacing on x axis
        alien3.rect.y = 50 + (50 * row) #spacing on y axis
        alien3_list.add(alien3)

#bunker list
for bunk in range(4): # spawns 4 bunkers
    for row in range(7): # splits the bunkers into smaller squares from 5 on x
        for column in range(15): # 15 on y
            bunker = Bunker() # calling bunker class
            bunker.rect.x = (50 + (200 * bunk)) + (5 * column) # start bunker at 50 pixels, each bunker spaced 215 pixels, spacing by 10
            bunker.rect.y = 500 + (5 * row)
            bunker_list.add(bunker)



def update():

    screen.fill(black)
    #lives
    lives = pygame
    #sprites
    ship.draw()
    alien_list.draw(screen)
    alien_list.update()
    alien2_list.draw(screen)
    alien2_list.update()
    alien3_list.draw(screen)
    alien3_list.update()
    bunker_list.draw(screen)
    laser_list.update()
    laser_list.draw(screen)
    alienlaser_list.update()
    alienlaser_list.draw(screen)
    pygame.display.update()


running = True # set running to true


while running: # infinite loop

    pygame.time.delay(5)





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    key = pygame.key.get_pressed()# calling the pressed function

    if key[pygame.K_LEFT]: # if the left arrow is pressed
        ship.rect.x += -vel # cange the ships position by vel pixels
    if key[pygame.K_RIGHT]: # if the right arrow is pressed
        ship.rect.x += velr # change the ships position by velr pixels
    if key[pygame.K_SPACE]: # if the space bar is pressed
        if len(laser_list) < 1: # and there are less than  lasers on screen
            laser = Laser() #call the laser class
            laser.rect.x = ship.rect.x + 32 # shoot the laser from position x + 32
            laser.rect.y = ship.rect.y  # shoot the laser from position y
            laser_list.add(laser)


# shooting for alien 1
    shoot_chance = random.randint(1, 400) # a random number between 1 and 400

    if shoot_chance < 5:
        if len(alien_list) > 0: # if there are still aliens on the screen
            random_alien = random.choice(alien_list.sprites()) # choosing a random alien for bullets to come from
            alienlaser = AlienLaser()
            alienlaser.rect.x = random_alien.rect.x  # area were bullets come from
            alienlaser.rect.y = random_alien.rect.y + 25
            alienlaser_list.add(alienlaser)

#shooting chance for alien 2

    shoot_chance = random.randint(1, 800) # a random number between 1 and 800

    if shoot_chance < 5:
        if len(alien2_list) > 0: # if there are still aliens on the screen
            random_alien2 = random.choice(alien2_list.sprites()) # choosing a random alien for bullets to come from
            alienlaser = AlienLaser()
            alienlaser.rect.x = random_alien2.rect.x  # area were bullets come from
            alienlaser.rect.y = random_alien2.rect.y + 25
            alienlaser_list.add(alienlaser)

            #alien 3 shooting chance

    shoot_chance = random.randint(1, 200) # a random number between 1 and 800

    if shoot_chance < 5:
        if len(alien3_list) > 0: # if there are still aliens on the screen
            random_alien3 = random.choice(alien3_list.sprites()) # choosing a random alien for bullets to come from
            alienlaser = AlienLaser()
            alienlaser.rect.x = random_alien3.rect.x  # area were bullets come from
            alienlaser.rect.y = random_alien3.rect.y + 25
            alienlaser_list.add(alienlaser)



    for laser in laser_list: #for lasers
        if laser.rect.y < 0: # if the laser goes off scree
            laser_list.remove(laser) # this removes the laser

#alien 1
        for alien in alien_list: # if a lasr rectangle collides
            if laser.rect.colliderect(alien.rect): # with the alien rectange
                laser_list.remove(laser) # removes laser
                alien_list.remove(alien) #removes the alien
#alien 2
        for alien2 in alien2_list: # if a lasr rectangle collides
            if laser.rect.colliderect(alien2.rect): # with the alien rectange
                laser_list.remove(laser) # removes laser
                alien2_list.remove(alien2) #removes the alien

#alien 3
        for alien3 in alien3_list: # if a lasr rectangle collides
            if laser.rect.colliderect(alien3.rect): # with the alien rectange
                laser_list.remove(laser) # removes laser
                alien3_list.remove(alien3) #removes the alien


        for bunker in bunker_list: # same concept as alien rectangle collision
            if laser.rect.colliderect(bunker.rect): # if the collision of lasers rectangle with bunker rectanger
                laser_list.remove(laser) # remove the laser
                bunker_list.remove(bunker) # remove the bunker







    for alienlaser in alienlaser_list: # same concept
        if alienlaser.rect.y > 600: # removes laser if touches boundry
            alienlaser_list.remove(alienlaser)
        if alienlaser.rect.colliderect(ship.rect): # if rectangles collide
            alienlaser_list.remove(alienlaser) # the health goes down
            ship.health -= 1 # by one health
        for bunker in bunker_list: # if bunker is hit by alien laser
            if alienlaser.rect.colliderect(bunker.rect): # r
                alienlaser_list.remove(alienlaser)# remove the laser
                bunker_list.remove(bunker) #remove the bunker
# ending game
    if ship.health < 3:
        print("2 lives")
        if ship.health < 2:
            print("1 life")
            if ship.health < 1:
                print("GAME OVER")
                running = False

    if len(alien_list) == 0 and len(alien2_list) == 0 and len(alien3_list) == 0:
        print("YOU WIN")
        running = False # ends the loop if all enemies are dead

    #spaceship boundries

    if ship.rect.x <= 0: # boundries so ship doesnt go out the srcreen window
        ship.rect.x = 0
    elif ship.rect.x >= 736: #image is 64 pixel
        ship.rect.x = 736

    update()


pygame.quit()
#alien
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets','alien.png'))
        self.rect = self.image.get_rect()
        self.group_rect = pygame.Rect(130, 75, 250,250) # first coordinate where first enemy on left starts, second covers all aliens in the area
        self.direction = 1 # speed
    def update(self):
        self.rect.x += self.direction
        self.group_rect.x += self.direction
        if self.group_rect.x + 500 >= 775: # if grouprectangle passes coordinate 775
            self.direction = -self.direction # change direction to negative
            self.rect.y += 10 # moves down 5 pixles in y direction
        if self.group_rect.x <= 25:
            self.direction = -self.direction
            self.rect.y += 10 # moves down 5 pixles in y direction




# bunker
class Bunker(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8, 8])
        self.image.fill(green)
        self.rect = self.image.get_rect()


#spaceship laser
class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 7])
        self.image.fill(green)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += -10

#alien laser 1

class AlienLaser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 7])
        self.image.fill(red)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1



ship = SpaceShip()
ship.rect.x = 370 # setting x and y coordinates of space ship
ship.rect.y = 550


alien_list = pygame.sprite.Group()
bunker_list = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
alienlaser_list = pygame.sprite.Group()

#alien 1 list
for row in range(3, 5): # spawns 2 rows from row 4 and 5
    for column in range(0, 12): #spawns 10 enemies
        alien = Alien() # the 80 is settimng them in the middle, the 50 is spacing between each alien
        alien.rect.x = 80 + (50 * column) #spacing on x axis
        alien.rect.y = 50 + (50 * row) #spacing on y axis
        alien_list.add(alien)



for bunk in range(4): # spawns 4 bunkers
    for row in range(7): # splits the bunkers into smaller squares from 5 on x
        for column in range(15): # 15 on y
            bunker = Bunker() # calling bunker class
            bunker.rect.x = (50 + (200 * bunk)) + (5 * column) # start bunker at 50 pixels, each bunker spaced 215 pixels, spacing by 10
            bunker.rect.y = 500 + (5 * row)
            bunker_list.add(bunker)



def update():

    screen.fill(black)
    #lives
    lives = pygame
    #sprites
    ship.draw()
    alien_list.draw(screen)
    alien_list.update()
    bunker_list.draw(screen)
    laser_list.update()
    laser_list.draw(screen)
    alienlaser_list.update()
    alienlaser_list.draw(screen)
    pygame.display.update()


running = True # set running to true


while running: # infinite loop

    pygame.time.delay(5)





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    key = pygame.key.get_pressed()# calling the pressed function

    if key[pygame.K_LEFT]: # if the left arrow is pressed
        ship.rect.x += -vel # cange the ships position by vel pixels
    if key[pygame.K_RIGHT]: # if the right arrow is pressed
        ship.rect.x += velr # change the ships position by velr pixels
    if key[pygame.K_SPACE]: # if the space bar is pressed
        if len(laser_list) < 1: # and there are less than  lasers on screen
            laser = Laser() #call the laser class
            laser.rect.x = ship.rect.x + 32 # shoot the laser from position x + 32
            laser.rect.y = ship.rect.y  # shoot the laser from position y
            laser_list.add(laser)



    shoot_chance = random.randint(1, 300) # a random number between 1 and 300

    if shoot_chance < 5:
        if len(alien_list) > 0: # if there are still aliens on the screen
            random_alien = random.choice(alien_list.sprites()) # choosing a random alien for bullets to come from
            alienlaser = AlienLaser()
            alienlaser.rect.x = random_alien.rect.x  # area were bullets come from
            alienlaser.rect.y = random_alien.rect.y + 25
            alienlaser_list.add(alienlaser)



    for laser in laser_list: #for lasers
        if laser.rect.y < 0: # if the laser goes off scree
            laser_list.remove(laser) # this removes the laser
        for alien in alien_list: # if a lasr rectangle collides
            if laser.rect.colliderect(alien.rect): # with the alien rectange
                laser_list.remove(laser) # removes laser
                alien_list.remove(alien) #removes the alien


        for bunker in bunker_list: # same concept as alien rectangle collision
            if laser.rect.colliderect(bunker.rect): # if the collision of lasers rectangle with bunker rectanger
                laser_list.remove(laser) # remove the laser
                bunker_list.remove(bunker) # remove the bunker







    for alienlaser in alienlaser_list: # same concept
        if alienlaser.rect.y > 600: # removes laser if touches boundry
            alienlaser_list.remove(alienlaser)
        if alienlaser.rect.colliderect(ship.rect): # if rectangles collide
            alienlaser_list.remove(alienlaser) # the health goes down
            ship.health -= 1 # by one health
        for bunker in bunker_list: # if bunker is hit by alien laser
            if alienlaser.rect.colliderect(bunker.rect): # r
                alienlaser_list.remove(alienlaser)# remove the laser
                bunker_list.remove(bunker) #remove the bunker
# ending game
    if ship.health < 0 or len(alien_list) == 0:
        running = False

    #spaceship boundries

    if ship.rect.x <= 0: # boundries so ship doesnt go out the srcreen window
        ship.rect.x = 0
    elif ship.rect.x >= 736: #image is 64 pixel
        ship.rect.x = 736

    update()


pygame.quit()

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
