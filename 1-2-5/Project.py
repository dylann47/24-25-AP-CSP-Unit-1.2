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
aliens = ["blue_alien", "purple_alien", "red_alien", "indigo_alien"]

#Background
wn.bgpic(background)

#Turtles
#Player turtle
player = trtl.Turtle()
player.shape(human)
player.penup()
player.forward(10)

#Alien vertical turtle
alien_vert = trtl.Turtle()
alien_vert.shape(alien[rand.randint(0, (len(aliens))])
alien_vert.penup()
player.forward(20)

#Alien horizontal turtle
alien_hor = trtl.Turtle()
alien_hor.shape(rand.randchoice(aliens))
alien_hor.penup()
alien_hor.forward(30)



#Turtle screen
wn.mainloop()