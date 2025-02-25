#--Setup Code--
#--Import Statements--
import turtle as turtle

#--Turtle Screen Initialization--
screen = turtle.Screen()
screen.setup(width=600, height=600)

#--Variables--
tic_tac_toe_board = [["" for _ in range(3)] for _ in range(3)]
player_one = "X"
panel_size = 200
offset = 300

#--TicTacToeBoard--
def draw_board():
    turtle.speed(0)
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
def draw_symbol(row, col, symbol):
    x = -200 + (col * panel_size)
    y = 200 - (row * panel_size)

    if symbol == "X":
        turtle.pencolor("Orange")
    elif symbol == "O":
        turtle.pencolor("Teal")
    else:
        turtle.pencolor("black")

    turtle.penup()
    turtle.goto(x,y)
    turtle.write(symbol, align="center", font=("Arial", 36, "normal"))

#--Click For Panels-- **Ask how to cite external website**
def click_on_panel(x,y):
    col = int((x + offset) // panel_size)
    row = int((offset - y) // panel_size)

    if row in (0, 1, 2) and col in (0, 1, 2) and tic_tac_toe_board[row][col] == "":
        user_input = screen.textinput("TicTacToe", "Choose Input").upper()
        if user_input in ["X", "O"]:
            tic_tac_toe_board[row][col] = user_input
            draw_symbol(row, col, user_input)
        else:
            print("Not a valid choice")

#--Drawing the Board--
draw_board()
screen.onclick(click_on_panel)
screen.mainloop()


