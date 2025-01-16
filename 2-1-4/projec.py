#--Setup--
#---Import Statements---
import turtle
import turtle as trtl
import random as random

#--Turtle Screen Initialization--
screen = turtle.Screen()
screen.setup(width=600, height=600)

#--Board--
board = [["" for _ in range(3)] for _ in range(3)]
player_1 = "X"
tile_size = 250

#--Drawing Board--
def draw_board(board):
    turtle_speed(10)
    turtle.penup()
    turtle.goto(-300, 100)
    turtle.pendown()
    turtle.goto(300, 100)
    turtle.penup()
    turtle.goto(-300, -100)
    turtle.pendown()
    turtle.goto(300, -100)
    turtle.penup()
    turtle.goto(-100, 300)
    turtle.pendown()
    turtle.goto(-100, -300)
    turtle.penup()
    turtle.goto(100, 300)
    turtle.pendown()
    turtle.goto(100, -300)
    turtle.penup()