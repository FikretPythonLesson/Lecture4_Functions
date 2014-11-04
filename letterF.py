import turtle

def calcLength(length, scale):
    return length + length * scale / 100

def gotoCenter(distance):
    turtle.penup()
    turtle.forward(distance/2)
    turtle.pendown()
    
def letter_F(height, width, scale):
    turtle.left(90)
    turtle.forward(calcLength(height, scale))
    turtle.right(90)
    turtle.forward(calcLength(width, scale))
    turtle.penup()
    turtle.backward(calcLength(width, scale))
    turtle.left(90)
    turtle.backward(calcLength(height/2, scale))
    turtle.right(90)
    turtle.pendown()
    turtle.forward(calcLength(width/2, scale))
    turtle.backward(calcLength(width/2, scale))
    turtle.left(90)
    turtle.backward(calcLength(height/2, scale))
    turtle.right(90)
    turtle.pendown()



letter_F(100, 50, 0)

turtle.done()
