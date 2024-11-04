# a121_catch_a_turtle.py

#-----import statements-----
import turtle as trtl
from idlelib.configdialog import font_sample_text

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
Score = 0

#-----initialize turtle-----
spot = trtl.turtles()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
spot.penup()
#-----game functions--------
class Change_position:
    pass

def spot_clicked(x, y):
    Change_position()
    update_score()

def change_position(x, ran=None):
    new_xpos = ran.randint(-150, 150)
    new_ypos = ran.randint(-175, 175)
    spot.goto(new_xpos, new_ypos)

def update_score(score=None):
    update_score()
    score +=1
    score_writer.clear()
    score_writer.write(score, font_sample_text)

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()

#-----Score----------------

score_writer = trtl
score_writer.penup()