import turtle

s= turtle.Screen()
t= turtle.Turtle()

s.bgcolor("violet")#COlor de fondo
s.title("Personalizar")#Titulo de la ventana


t.shapesize(4,4,4) #Tamaño de la tortuga(Ancho, largo, borde)
t.fillcolor("green") #FOndo de la tortuga
t.forward(100)
t.pencolor("orange") #COlor del borde de la tortuga y la tinta de la linea
t.right(90)
t.forward(100)

t.color("yellow", "grey") #COlor del borde de la tortuga y la tinta de la linea y despues el fondo
t.pensize(5)#tamaño de la tinta
t.right(90)
t.forward(100)

turtle.done()