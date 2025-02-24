from turtle import *

#we want to paint a house

#step 1:  draw square
speed(5)
width(10)
color("brown")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square  

#drawing a door
begin_fill()
forward(70)
color("black")
left(90)
forward(120)# height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
color("brown")
pendown()
left(30)
forward(70)
color("brown")
left(90)
forward(8)
color("white")
forward(15)
begin_fill()
color("blue")
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()
left(90)
forward(38)
color("white")
forward(80)

begin_fill()
color("blue")
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

exitonclick()