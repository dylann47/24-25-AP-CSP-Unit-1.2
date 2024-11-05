
import turtle as trtl
import random as rand

# circular turtle will not use a global variable
spot = trtl.Turtle()
spot.goto(-100, 0)
spot.shape("circle")
spot.shapesize(3)

# square shaped turtle will use a global variable
box = trtl.Turtle()
box.goto(100,0)
box.shape("square")
box.shapesize(3)

# attempts to update the score for spot, but will not work because this function
# does not have access to the score that was created above
def update_score_for_spot(x,y):
  score += 1
  print(score)

# update_score_for_box will update the score for spot
def update_score_for_box(x,y):
  global score # gives this function access to the score that was created above
  score += 1
  print(score)
  spot.goto(x,y)

#---------events----------
spot.onclick(update_score_for_spot)
box.onclick(update_score_for_box)
wn = trtl.Screen()
wn.mainloop()