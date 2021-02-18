'''
 여기서 GUI 창 관리 및 커서 관리를 시행합니다
'''

# Import tools
from pygame.locals import *
import pygame
import qmaze
 
class Player:
    x = 44
    y = 44
    speed = 1
 
    def moveRight(self):
        self.x = self.x + self.speed
 
    def moveLeft(self):
        self.x = self.x - self.speed
 
    def moveUp(self):
        self.y = self.y - self.speed
 
    def moveDown(self):
        self.y = self.y + self.speed

# Initialization code
windowWidth = 800
windowHeight = 600

running = False
display_surf = None
image_surf = None
block_surf = None
player = Player()
maze = qmaze.Maze()

def init():
    pygame.init()
    display_surf = pygame.display.set_mode((windowWidth,windowHeight), pygame.HWSURFACE)
    
    pygame.display.set_caption('Pygame pythonspot.com example')
    running = True
    image_surf = pygame.image.load("player.png").convert()
    block_surf = pygame.image.load("block.png").convert()



# Game run code

def on_event(event):
    if event.type == QUIT:
        running = False

def on_loop():
    pass

def render():
    display_surf.fill((0,0,0))
    display_surf.blit(image_surf,(player.x,player.y))
    maze.draw(display_surf, block_surf)
    pygame.display.flip()

def cleanup():
    pygame.quit()


init()

while(running):
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    
    if (keys[K_RIGHT]):
        player.moveRight()

    if (keys[K_LEFT]):
        player.moveLeft()

    if (keys[K_UP]):
        player.moveUp()

    if (keys[K_DOWN]):
        player.moveDown()

    if (keys[K_ESCAPE]):
        running = False

    on_loop()
    render()
cleanup()