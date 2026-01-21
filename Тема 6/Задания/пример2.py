from turtle import *

k = 20
down()
tracer(0)
x = 1
for i in range(5):
    fd(x * k)
    right(90)
    fd(3 * k)
up()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
exitonclick()