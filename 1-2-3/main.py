import random as rand
import turtle as trtl
from operator import index

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
apple_list = []
apple_letters = []

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

wn.bgpic("background.gif")
apple = trtl.Turtle()
wn.tracer(False)

for i in range (5):
  apple_list.append(trtl.turtles())
  apple_letters.append(rand.choice(letters))

#-----functions-----
def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  apple.list[index].penup()
  wn.tracer(False)
  apple.list[index].setx(rand.randint(-150, 150))
  apple.list[index].sety(rand.randint(-15, 100))
  apple.list[index].color("White")
  apple.list[index].write(apple_letters[index],font=("Arial", 30, "bold"))
  apple.list[index].sety(apple_list[index].ycor() + 30)
  apple.list[index].showturtle()
  wn.tracer(False)
  wn.update()

def drop_apple(index):
  apple_list[index].penup()
  apple_list[index].clear()
  apple_list[index].sety(-150)
  apple_list[index].hideturtle()

def reset_apple(apple):
  if len(letters) > 0:
    newX = rand.randint(-200, 200)
    newY = 0
    new_letter = rand.randint(0, len(letters))
    apple.goto(newX, newY)
    draw_apple(apple, letters.pop(new_letter))

def typeda():
  for i in range (5):
    if apple_letters[i] == "A":
      drop_apple(i)

def typedb():
  for i in range (5):
    if apple_letters[i] == "B":
      drop_apple(i)

def typedC():
  for i in range (5):
    if apple_letters[i] == "C":
      drop_apple(i)

def typedD():
  for i in range (5):
    if apple_letters[i] == "D":
      drop_apple(i)

def typedE():
  for i in range (5):
    if apple_letters[i] == "E":
      drop_apple(i)

def typedF():
  for i in range(5):
    if apple_letters[i] == "F":
      drop_apple(i)

def typedG():
  for i in range (5):
    if apple_letters[i] == "G":
      drop_apple(i)

def typedH():
  for i in range (5):
    if apple_letters[i] == "H":
      drop_apple(i)

def typedI():
  for i in range (5):
    if apple_letters[i] == "I":
      drop_apple(i)

def typedJ():
  for i in range (5):
    if apple_letters[i] == "J":
      drop_apple(i)

def typedK():
  for i in range (5):
    if apple_letters[i] == "K":
      drop_apple(i)

def typedL():
  for i in range (5):
    if apple_letters[i] == "L":
      drop_apple(i)

def typedM():
  for i in range (5):
    if apple_letters[i] == "M":
      drop_apple(i)

def typedN():
  for i in range (5):
    if apple_letters[i] == "N":
      drop_apple(i)

def typedO():
  for i in range (5):
    if apple_letters[i] == "O":
      drop_apple(i)

def typedP():
  for i in range (5):
    if apple_letters[i] == "P":
      drop_apple(i)

def typedQ():
  for i in range (5):
    if apple_letters[i] == "Q":
      drop_apple(i)

def typedR():
  for i in range (5):
    if apple_letters[i] == "R":
      drop_apple(i)

def typedS():
  for i in range (5):
    if apple_letters[i] == "S":
      drop_apple(i)

def typedT():
  for i in range (5):
    if apple_letters[i] == "T":
      drop_apple(i)

def typedU():
  for i in range (5):
    if apple_letters[i] == "U":
      drop_apple(i)

def typedV():
  for i in range (5):
    if apple_letters[i] == "V":
      drop_apple(i)

def typedW():
  for i in range (5):
    if apple_letters[i] == "W":
      drop_apple(i)

def typedY():
  for i in range (5):
    if apple_letters[i] == "Y":
      drop_apple(i)

def typedZ():
  for i in range (5):
    if apple_letters[i] == "Z":
      drop_apple(i)

#   a123_apple_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the
# turtle with a new letter selected at random from the list of letters

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the
# apple and letter have dropped, call the apple resetting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

#-----function calls-----
wn.listen()
trtl.mainloop()
draw_apple(apple, "a")
wn.onkeypress(drop_apple, "a")

wn.listen()
trtl.mainloop()