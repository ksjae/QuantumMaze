'''
 여기서 GUI 창 관리 및 커서 관리를 시행합니다
'''

# Import tools
import turtle
import qmaze
 
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
windowWidth = 800
windowHeight = 600

player = Player()
maze = qmaze.Maze()

pygame.init()
display_surf = pygame.display.set_mode((windowWidth,windowHeight), pygame.HWSURFACE)

pygame.display.set_caption('QuantumMaze')
running = True
image_surf = pygame.image.load("player.bmp").convert()
block_surf = pygame.image.load("block.bmp").convert()

TILE_SIZE = 64

# Warp turtle back to home when maze draw is done
t.home()

# Predefined turtle motion function
def moveTurtleFoward():
    t.forward(50)

def endGame():
    print("Click to exit")
    tScreen.exitonclick()

def render():
    display_surf.fill((0,0,0))
    for row in range(len(maze.maze)):
        for column in range(len(maze.maze[row])):
            if maze.maze[row][column] == 1:
                x = column * TILE_SIZE
                y = row * TILE_SIZE
                display_surf.blit(block_surf, (x, y))
    display_surf.blit(image_surf,(player.x * TILE_SIZE,player.y * TILE_SIZE))
    pygame.display.flip()

# Call func when key pressed
tScreen.listen()
tScreen.onkeypress(moveTurtleFoward, 'Right') 
tScreen.onkeypress(endGame, 'Escape') 

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Usually wise to be able to close your program.
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.moveUp()
                if maze.maze[player.y][player.x] == 1:
                    player.moveDown()
            elif event.key == pygame.K_a:
                player.moveLeft()
                if maze.maze[player.y][player.x] == 1:
                    player.moveRight()
            elif event.key == pygame.K_s:
                player.moveDown()
                if maze.maze[player.y][player.x] == 1:
                    player.moveUp()
            elif event.key == pygame.K_d:
                player.moveRight()
                if maze.maze[player.y][player.x] == 1:
                    player.moveLeft()

    pygame.time.wait(13)
    on_loop()
    render()
cleanup()
