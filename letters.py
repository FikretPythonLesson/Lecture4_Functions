import turtle

def calcLength(length, scale):
    return length + length * scale / 100

def gotoCenter(distance):
    turtle.penup()
    turtle.forward(distance/2)
    turtle.pendown()
    
def letter_A(height, width, scale):
    turtle.left(90)
    turtle.forward(calcLength(height, scale))
    turtle.right(90)
    turtle.forward(calcLength(width, scale))
    turtle.right(90)
    turtle.forward(calcLength(height, scale))
    turtle.penup()
    turtle.backward(calcLength(height/2, scale))
    turtle.pendown()
    turtle.right(90)
    turtle.forward(calcLength(width, scale))
    turtle.penup()
    turtle.left(90)
    turtle.forward(calcLength(height/2, scale))
    turtle.left(90)
    turtle.pendown()
    
    gotoCenter(width)
    
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

def drawLetter(letter, height, width, scale):
    if letter == 'A':
        letter_A(height, width, scale)
    elif letter == 'F':    
        letter_F(height, width, scale)


