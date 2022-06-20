import turtle

s= turtle.Screen()
t= turtle.Turtle()

t.speed(10)#Velocidad
t.circle(10)#Dibuja un circulo
t.speed(10)
t.circle(50)
t.dot(40)# CIrculo relleno

t.hideturtle()#Desaparece ala fleca
t.circle(60)
t.showturtle()#Lo muestra de nuevo
t.circle(100)

t.setx(100)#Manda turtle a la cordenada x=100
t.sety(-100)#Manda turtle a la cordenada Y=-100
t.setx(0)
t.sety(0)


turtle.done()