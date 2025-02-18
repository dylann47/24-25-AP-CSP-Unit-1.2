#--Setup Code--
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
def draw_symbol(row, col, symbol):
    x = -200 + (row * panel_size)
    y = 200 - (row * panel_size)

    turtle.penup()
    turtle.goto(x,y)
    turtle.write(symbol, align="center", font=("Arial", 36, "normal"))

#--Click For Panels--
def click_on_panel(x,y):
    col = (x + 300) // panel_size
    row = (-y + 300) // panel_size

    if 0 <= row < 3 and 0 <= col < 3 and tic_tac_toe_board[int(row)][int(col)] == "":
        user_input = screen.textinput("Tic-Tac-Toe", "Enter X or O:").upper()  # Get user input
        if user_input in ["X", "O"]:
            tic_tac_toe_board[int(row)][int(col)] = user_input
            draw_symbol(int(row), int(col), user_input)
        else:
            print("Invalid input! Please enter 'X' or 'O'.")


#--Drawing the Board--
draw_board()
screen.onclick(click_on_panel)
screen.mainloop()


