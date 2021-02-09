echo "# CSP" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/2023kpeterson/CSP.git
git push -u origin main

import turtle as trtl
import random as rand

wn = trtl.Screen()

mazepainter = trtl.Turtle()
mazecolor = "Blue"
path_width = 10
walls = 26

mazerunner = trtl.Turtle()
mazerunner.pencolor("Red")
mazerunner.penup()
mazerunner.goto(-40,20)
mazerunner.pendown()

mazepainter.speed(0)
mazepainter.pencolor(mazecolor)

#functions 
def draw_barrier(barv):
  mazepainter.forward(barv)
  mazepainter.left(90)
  mazepainter.forward(path_width*2)
  mazepainter.back(path_width*2)
  mazepainter.right(90)

def draw_door(doov): 
  mazepainter.forward(doov)
  mazepainter.penup()
  mazepainter.forward(path_width*2)
  mazepainter.pendown()

#drawing maze  
wall_len = path_width
for w in range(walls):
  wall_len += path_width
  if (w > 4):
    door = rand.randint(path_width*2, (wall_len-path_width*2))
    barrier = rand.randint(path_width*2, (wall_len-path_width*2))
    mazepainter.left(90)

#if a door and barrier rendered on each other
    while (abs(door - barrier) < path_width):
      door = rand.randint(path_width*2, (wall_len-path_width*2))

#door first
    if (door < barrier):
      door1 = door
      draw_door(door1)

#draw barrier
      barrier1 = barrier - door - path_width*2
      draw_barrier(barrier1)
      mazepainter.forward(wall_len - barrier)

#barrier first
    else:
      barrier2 = barrier
      draw_barrier(barrier2)

#draw door
      door2 = door - barrier
      draw_door(door2)
      mazepainter.forward(wall_len - door - path_width*2)
  

mazepainter.hideturtle()

def up():
      mazerunner.setheading(90)

def down():
      mazerunner.setheading(270)

def right():
      mazerunner.setheading(0)

def left():
      mazerunner.setheading(180)

def move_runner():
      mazerunner.forward(5)

wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(move_runner, "g")
     



wn.listen()
wn.mainloop()