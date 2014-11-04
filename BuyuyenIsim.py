import turtle
import letters

def ileriGit(adim):
    turtle.penup()
    turtle.forward(adim)
    turtle.pendown()

def basaDon():
    turtle.penup()
    turtle.backward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()

def solUstKoseyeGit():
    turtle.penup()
    turtle.goto(-turtle.window_width()/2, turtle.window_height()/2)
    turtle.pendown()
    
turtle.speed(0)
solUstKoseyeGit()

for i in range(5):
    for letter in 'AF':
        letters.drawLetter(letter, 10, 5, i * 20)
        ileriGit(100)
    basaDon()    
        
turtle.done()        
