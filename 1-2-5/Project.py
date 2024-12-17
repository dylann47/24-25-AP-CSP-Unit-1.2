#---Setup---
#Import statements
import turtle as trtl
import random as rand

#Turtle screen initialization
wn = trtl.Screen()

#Images
blue_alien = "BlueAlien.gif"
purple_alien = "PurpleAlien.gif"
red_alien = "RedAlien.gif"
indigo_alien = "IndigoAlien.gif"
human = "Human.gif"
background = "bgproject2.gif"

#Add turtle shapes
wn.addshape(blue_alien)
wn.addshape(purple_alien)
wn.addshape(red_alien)
wn.addshape(indigo_alien)
wn.addshape(human)

#Alien image list
aliens = [blue_alien,purple_alien,red_alien,indigo_alien]

    #Background
wn.bgpic(background)

#Turtles
#Player turtle
player = trtl.Turtle()
player.turtlesize()
player.shape(human)
player.penup()
player.goto(150,150)

#Alien turtle
alien = trtl.Turtle()
alien.penup()
choice = rand.randint(0,3)
alien.goto(-150,-150)
alien.shape(aliens[choice])

# Add Timer
timer = 30
timer_display = trtl.Turtle()
timer_display.hideturtle()
timer_display.color("white")
timer_display.penup()
timer_display.goto(0, 250)

# Clock
def update_timer():
    global timer
    if timer > 0:
        timer -= 1
        timer_display.clear()
        timer_display.write(f"Time: {timer}", align="center", font=("Arial", 24, "normal"))
        wn.ontimer(update_timer, 1000)
    else:
        timer_display.write("Game Over", align="center", font=("Arial", 24, "normal"))

update_timer()

#Score Display
score = 0
score_display = trtl.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0,200)

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}",align="center",font=("Arial",36,"normal"))

#Score Display
update_score()



#Check for collision
def check_collision():
    global score
    if abs(player.xcor() - alien.xcor()) < 50 and abs(player.ycor() - alien.ycor()) < 50:
        score += 1
        update_score()
        reset_alien_position()

# Reset alien position after collision
def reset_alien_position():
    alien.goto(rand.randint(-200, 200), rand.randint(-200, 200))


#Movement functions
def w_up():
    player.setheading(90)
    player.forward(50)
    check_collision()

def s_down():
    player.setheading(90)
    player.backward(50)
    check_collision()


def a_left():
    player.setheading(180)
    player.forward(50)
    check_collision()

def d_right():
    player.setheading(180)
    player.backward(50)
    check_collision()

#Alien
def i_up():
    alien.setheading(90)
    alien.forward(50)
    check_collision()

def k_down():
    alien.setheading(90)
    alien.backward(50)
    check_collision()

def j_left():
    alien.setheading(180)
    alien.forward(50)
    check_collision()

def l_right():
    alien.setheading(180)
    alien.backward(50)
    check_collision()


#Player movement
wn.onkey(w_up, "w")
wn.onkey(s_down, "s")
wn.onkey(a_left, "a")
wn.onkey(d_right, "d")

#Alien Movement
wn.onkey(i_up, "i")
wn.onkey(k_down, "k")
wn.onkey(j_left, "j")
wn.onkey(l_right, "l")


#Turtle screen
wn.listen()
wn.mainloop()