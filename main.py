'''
 여기서 GUI 창 관리 및 커서 관리를 시행합니다
'''

# Import tools
from pygame.locals import *
import pygame
from Maze import Maze
import MazeGenerator
 
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
windowWidth = 640
windowHeight = 480

player = Player()
SIZE = (10, 8)
SIZE_MINUS_ONE = (SIZE[0]-1, SIZE[1]-1)
mazeGenerator = MazeGenerator.MazeGenerator(*SIZE)
maze = mazeGenerator.GetMaze()
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


def render():
    display_surf.fill((0,0,0))
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == 1:
                x = column * TILE_SIZE
                y = row * TILE_SIZE
                display_surf.blit(block_surf, (x, y))
    display_surf.blit(image_surf,(player.x * TILE_SIZE,player.y * TILE_SIZE))
    pygame.display.flip()

# Game run code

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Usually wise to be able to close your program.
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.moveUp()
                if maze[player.y][player.x] == 1:
                    player.moveDown()
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.moveLeft()
                if maze[player.y][player.x] == 1:
                    player.moveRight()
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.moveDown()
                if maze[player.y][player.x] == 1:
                    player.moveUp()
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.moveRight()
                if maze[player.y][player.x] == 1:
                    player.moveLeft()

        if (player.x, player.y) == SIZE_MINUS_ONE:
            print("SUCCESS!!!!!!!!!")
            running = False
            break

    pygame.time.wait(13)
    render()
