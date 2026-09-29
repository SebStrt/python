import turtle as t
import math as m

screen = t.Screen()

size = 100
padding = size * 0.1 

t.speed(5)
t.pensize(size * 0.1)
t.bgcolor("gray")
screen.screensize(3*size, 2*size)

pos = 1

def printpos():
    global pos
    print("Koordinaten Kreis " + str(pos) + ": " + str(t.pos()))
    pos += 1

def drawcircle():
    global pos
    t.pendown()
    t.setheading(0)
    t.circle(size)
    t.penup()
    printpos()

def drawoverlap(start, end, color):
    t.color(color)
    t.setheading(0)
    t.penup()
    t.circle(size, start)
    t.pendown()
    t.circle(size, end)

#circle 1
t.teleport(-2 * size - 2 * padding, 0)
t.color("blue")
drawcircle()

#cirlce 2
t.teleport(-size - padding, -size - padding)
t.color("yellow")
drawcircle()

#cirlce 3
t.teleport(0, 0)
t.color("black")
drawcircle()

#cirlce 4
t.teleport(size + padding, -size - padding)
t.color("green")
drawcircle()

#cirlce 5
t.teleport(2 * size + 2 * padding, 0)
t.color("red")
drawcircle()

#redraw overlapping circles

#redraw circle 1
t.teleport(-2 * size - 2 * padding, 0)
drawoverlap(45, 90, "blue")

#redraw circle 2
t.teleport(-size - padding, -size - padding)
drawoverlap(135, 45, "yellow")

#redraw circle 3
t.teleport(0, 0)
drawoverlap(45, 90, "black")

#redraw circle 4
t.teleport(size + padding, -size - padding)
drawoverlap(135, 45, "green")

#redraw circle 5
t.teleport(2 * size + 2 * padding, 0)
drawoverlap(135, 45, "red")

t.done()