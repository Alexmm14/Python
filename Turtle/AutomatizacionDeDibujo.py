import turtle

s=turtle.Screen()
t= turtle.Turtle()

for i in range(4):
    t.fd(100)
    t.rt(90)

a=0

while a<=100:
    t.circle(a)
    a=a+10


turtle.done()