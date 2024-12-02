import turtle as trtl

# Initialize Variables
wn = trtl.Screen()
maze = trtl.Turtle()
length = 30
path_width = 30

# Setup Turtle
maze.left(90)
maze.pensize(5)
maze.speed(0)

# Draw Maze
# Process:
# Draw a Line
# Turn Left
# Increment Length
# Repeat
def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.backward(path_width)
    maze_painter.left(90)

for wall in range(21):
    maze_painter.forward(length/3)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    if(wall > 5):
        draw_barrier()
    maze_painter.forward(length- path_width - length/3)
    maze_painter.left(90)
    length += 15


wn.listen()
wn.mainloop()