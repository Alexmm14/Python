import turtle

s= turtle.Screen()
t= turtle.Turtle()

'''
t.begin_fill()
t.circle(100)
t.end_fill()

t.begin_fill()
t.color("white", "white")
t.circle(50)
t.end_fill()
'''
t.shape("turtle")

t.fd(100)
t.penup()#Levanta la pluma y deja de dibujar
t.fd(50)
t.pendown()#Baja la pluma para dibujar
t.fd(100)

t.undo()#Elimina el ultimo trazo
t.clear()#Elimina todos los trazos, pero no la posicion en el plano
t.reset()#Lo resetea


turtle.done()