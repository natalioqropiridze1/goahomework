import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Function to draw a rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)

# Function to draw a triangle
def draw_triangle(size):
    for _ in range(3):
        pen.forward(size)
        pen.left(120)

# Function to draw battlements
def draw_battlements(width):
    for _ in range(width // 20):
        pen.forward(20)
        pen.left(90)
        pen.forward(10)
        pen.right(90)
        pen.forward(20)
        pen.right(90)
        pen.forward(10)
        pen.left(90)


pen.penup()
pen.goto(-150, 0)
pen.pendown()
pen.fillcolor("darkgray")
pen.begin_fill()
draw_rectangle(50, 150)
pen.end_fill()

# Draw the right tower
pen.penup()
pen.goto(100, 0)
pen.pendown()
pen.begin_fill()
draw_rectangle(50, 150)
pen.end_fill()

# Draw the central part of the castle
pen.penup()
pen.goto(-100, 0)
pen.pendown()
pen.fillcolor("light gray")
pen.begin_fill()
draw_rectangle(200, 150)
pen.end_fill()


pen.penup()
pen.goto(-150, 150)
pen.pendown()
pen.fillcolor("light gray")
draw_battlements(100)


pen.penup()
pen.goto(50,150)
pen.pendown()
draw_battlements(50)

# draw rectangles
pen.penup()
pen.goto(-150, 150)
pen.pendown()
pen.fillcolor("light gray")
pen.begin_fill()
draw_rectangle(300, 200)
pen.end_fill()

# Draw the roof of the central part
pen.penup()
pen.goto(-50, 150)
pen.pendown()
pen.fillcolor("red")
pen.begin_fill()
draw_triangle(100)
pen.end_fill()

# Draw the left tower roof
pen.penup()
pen.goto(-150, 150)
pen.pendown()
pen.fillcolor("red")
pen.begin_fill()
draw_triangle(50)
pen.end_fill()

# Draw the right tower roof
pen.penup()
pen.goto(100, 150)
pen.pendown()
pen.begin_fill()
draw_triangle(50)
pen.end_fill()

# Draw the door
pen.penup()
pen.goto(-20, -100)
pen.pendown()
pen.fillcolor("brown")
pen.begin_fill()
draw_rectangle(40, 50)
pen.end_fill()

# Draw windows
for x in [-90, -10, ]:
    pen.penup()
    pen.goto(x, -50)
    pen.pendown()
    pen.fillcolor("yellow")
    pen.begin_fill()
    draw_rectangle(20, 30)
    pen.end_fill()


turtle.done()