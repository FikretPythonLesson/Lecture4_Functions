import turtle
# Rotating square
# ---------------------------

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t2.pencolor("white")

t1.speed(0)
t2.speed(0)

size = 100
angle = 10

for _ in range(5):
    for _ in range(9):
        t1.left(angle)   # tilt with the given angle
        t1.forward(size)
        t1.left(90)
        t1.forward(size)
        t1.left(90)
        t1.forward(size)
        t1.left(90)
        t1.forward(size)
        t1.left(90)

        t2.left(angle)   # tilt with the given angle
        t2.forward(size)
        t2.left(90)
        t2.forward(size)
        t2.left(90)
        t2.forward(size)
        t2.left(90)
        t2.forward(size)
        t2.left(90)

    t1.right(90)
    t1.backward(size)

    t2.right(90)
    t2.backward(size)

turtle.done()
