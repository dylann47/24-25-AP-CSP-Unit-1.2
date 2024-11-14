#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def apple_down(active_apple):
  x_coordinate = active_apple.xcor()
  y_coordinate = active_apple.ycor()
  active_apple.goto(x_coordinate, y_coordinate - 300)
#-----function calls-----
draw_apple(apple)
apple_down(apple)
wn.bgpic("background.gif")
wn.mainloop()
