'''
 여기서 GUI 창 관리 및 커서 관리를 시행합니다
'''

# Import tools
import turtle

# Initialize GUI Window
tScreen = turtle.Screen()
tScreen.setup(width=500, height=450, startx=0, starty=0)
turtle.title("QuMa - A Quantum Powered Maze")
t = turtle.Turtle()
t.fillcolor("red") # Set color of the cursor aka TURTLE

# Moving turtle
t.right(90)
t.forward(100)

# Warp turtle back to home when maze draw is done
t.home()

# Predefined turtle motion function
def moveTurtleFoward():
    t.forward(50)

def endGame():
    print("Click to exit")
    tScreen.exitonclick()


# Call func when key pressed
tScreen.listen()
tScreen.onkeypress(moveTurtleFoward, 'Right') 
tScreen.onkeypress(endGame, 'Escape') 

# When game is done
tScreen.mainloop()