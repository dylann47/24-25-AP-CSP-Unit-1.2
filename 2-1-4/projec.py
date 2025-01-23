#--Setup--
#--Import Statements--
import turtle as turtle

#--Turtle Screen Initialization--
screen = turtle.Screen()
screen.setup(width=550, height=550)

#--Variables--
tic_tac_toe_board = [["" for _ in range(3)] for _ in range(3)]
player_one = "X"
panel_size = 200

#--TicTacToeBoard--
def draw_board():
    turtle.penup()
    turtle.goto(100, -300)
    turtle.pendown()
    turtle.goto(100, 300)
    turtle.penup()
    turtle.goto(-100, -300)
    turtle.pendown()
    turtle.goto(-100, 300)
    turtle.penup()
    turtle.goto(300, -100)
    turtle.pendown()
    turtle.goto(-300, -100)
    turtle.penup()
    turtle.goto(300, 100)
    turtle.pendown()
    turtle.goto(-300, 100)
    turtle.penup()


#--Draw X--
def draw_x(x, symbol):
    turtle.penup()
    turtle.goto(x, symbol)
    turtle.write(symbol, align="center", font=("Arial", 24, "normal"))

#--Click For Panels--



#--Drawing the Board--
draw_board()
screen.mainloop()

