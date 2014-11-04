import turtle
import letters

turtle.speed(0)

for letter in ('I LOVE PYTHON'):
    letters.drawLetter(letter, 100,50,0)
        
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()

turtle.done()

