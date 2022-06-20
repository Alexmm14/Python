import turtle
import turtle
import time
import random

retraso = 0.009

s= turtle.Screen()
s.setup(650, 650)#Le das un formato de tamaño
s.bgcolor("Red")
s.title("Culebra")

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = "Stop"
serpiente.color("Green")

comida = turtle.Turtle()
comida.shape("circle")
comida.color("White")
comida.penup()
comida.goto(0, 100)
comida.speed(0)

cuerpo = []



def arriba():
    serpiente.direction = "up"

def abajo():
    serpiente.direction = "down"
def derecha():
    serpiente.direction = "right"
def izquierda():
    serpiente.direction = "left"


def movimiento():
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    if serpiente.direction == "right":
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    if serpiente.direction == "left":
        x = serpiente.xcor()
        serpiente.setx(x - 20)

s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")


while True:
    s.update()
    if serpiente.distance(comida) < 20:
        x = random.randint(-250, 250)
        y= random.randint(-250, 250)
        comida.goto(x, y)
    
        Nuevo_cuerpo = turtle.Turtle()
        Nuevo_cuerpo.shape("square")
        Nuevo_cuerpo.color("green")
        Nuevo_cuerpo.penup()
        Nuevo_cuerpo.goto(0,0)
        Nuevo_cuerpo.speed(0)


    movimiento()
    time.sleep(retraso)
    



turtle.done()