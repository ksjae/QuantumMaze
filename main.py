'''
 여기서 GUI 창 관리 및 커서 관리를 시행합니다
'''

# Import tools
from pygame.locals import *
import pygame
from Maze import Maze
import MazeGenerator
import random
 
class Player:
    x = 1
    y = 1
    speed = 1
 
    def moveRight(self):
        self.x += self.speed
 
    def moveLeft(self):
        self.x -= self.speed
 
    def moveUp(self):
        self.y -= self.speed
 
    def moveDown(self):
        self.y += self.speed

# Initialization code
windowWidth = 1280
windowHeight = 720

player = Player()
SIZE = (19, 11)
FINISH_LINE = (SIZE[0]*2-1, SIZE[1]*2-1)
mazeGenerator = MazeGenerator.MazeGenerator(*SIZE)
maze = mazeGenerator.GetMaze()
maze.Print()
maze = maze.ToList()

pygame.init()
display_surf = pygame.display.set_mode((windowWidth,windowHeight), pygame.HWSURFACE)

pygame.display.set_caption('QuantumMaze')
running = True
image_surf = pygame.image.load("player.bmp").convert()
block_surf = pygame.image.load("block.bmp").convert()

TILE_SIZE = 32

pygame.init()
display_surf = pygame.display.set_mode((windowWidth,windowHeight), pygame.HWSURFACE)

pygame.display.set_caption('QuMa: Quantum Maze')
running = True
image_surf = pygame.image.load("player.bmp").convert()
block_surf = pygame.image.load("block.bmp").convert()
finish_surf = pygame.image.load("wall.bmp").convert()
x_surf = pygame.image.load("x.bmp").convert()
z_surf = pygame.image.load("z.bmp").convert()
s_surf = pygame.image.load("s.bmp").convert()
h_surf = pygame.image.load("h.bmp").convert()

tiles = [block_surf, x_surf, z_surf, s_surf, h_surf]

def render():
    display_surf.fill((0,0,0))
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            r = maze[row][column]
            if maze[row][column] != 0:
                x = column * TILE_SIZE
                y = row * TILE_SIZE
                display_surf.blit(tiles[r-1], (x, y))
    display_surf.blit(finish_surf, (FINISH_LINE[0]* TILE_SIZE, FINISH_LINE[1]* TILE_SIZE))
    display_surf.blit(image_surf,(player.x * TILE_SIZE,player.y * TILE_SIZE))
    pygame.display.flip()

# Game run code

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Usually wise to be able to close your program.
            running = False
            print(player.x, player.y)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.moveUp()
                if maze[player.y][player.x] == 1 or player.y < 0:
                    player.moveDown()
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.moveLeft()
                if maze[player.y][player.x] == 1 or player.x < 0:
                    player.moveRight()
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.moveDown()
                if maze[player.y][player.x] == 1 or player.y > SIZE[1]*2:
                    player.moveUp()
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.moveRight()
                if maze[player.y][player.x] == 1 or player.x > SIZE[0]*2:
                    player.moveLeft()
        if (player.x, player.y) == FINISH_LINE:
            print("SUCCESS!!!!!!!!!")
            running = False
            break

    pygame.time.wait(13)
    render()
