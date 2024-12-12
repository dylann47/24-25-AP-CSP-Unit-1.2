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
player.forward(10)

#Randomizer

#Alien turtle
alien = trtl.Turtle()
alien.shape(blue_alien)
alien.penup()

#Movement functions
def w_up():
    player.setheading(90)
    player.forward(50)
def s_down():
    player.setheading(90)
    player.backward(50)

def a_left():
    player.setheading(180)
    player.forward(50)

def d_right():
    player.setheading(180)
    player.backward(50)

#Alien
def i_up():
    alien.setheading(90)
    alien.forward(70)

def k_down():
    alien.setheading(90)
    alien.backward(70)

def j_left():
    alien.setheading(180)
    alien.forward(70)


def l_right():
    alien.setheading(180)
    alien.backward(70)


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