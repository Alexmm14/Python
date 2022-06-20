import turtle
import random

s= turtle.Screen()
s.title("Proyecto")
s.bgcolor("red")

player1 = turtle.Turtle()
player2 = turtle.Turtle()
player1.hideturtle()
player2.hideturtle()

player1.shape("turtle")
player1.color("black", "black")
player1.shapesize(2,2,2)
player1.pensize(3)

player2.shape("turtle")
player2.color("blue", "blue")
player2.shapesize(2,2,2)
player2.pensize(3)

player1.penup()
player1.goto(200, 200)
player1.pendown()
player1.circle(40)
player1.penup()
#player1.goto(160, 240)
player1.goto(-200, 240)

player2.penup()
player2.goto(200, -200)
player2.pendown()
player2.circle(40)
player2.penup()
#player2.goto(160, -160)
player2.goto(-200, -160)
player1.showturtle()
player2.showturtle()

dado = [1,2,3,4,5,6]

for i in range(20):
    if player1.pos() >= (140, 240):
        print("Player 1 Win!!")
        break
    elif player2.pos() >= (140, -160):
        print("Player 2 Win!!")
        break
    else:
        turn1 = input("Presiona ENTER para tomar tu turno...")
        turn1 = random.choice(dado)
        turn= turn1*20
        print("Avanzas: ", turn)
        player1.pendown()
        player1.forward(turn)

        turn2 = input("Presiona ENTER para tomar tu turno...")
        turn2 = random.choice(dado)
        turn= turn2*20
        print("Avanzas: ", turn)
        player2.pendown()
        player2.forward(turn)




turtle.done()


