from turtle import *

tracer(0)
koef = 20
down()

for i in range(2):
    fd(9 * koef)
    right(90)
    fd(15 * koef)
    right(90)
up()
fd(12 * koef)
right(90)
down()
for i in range(2):
    fd(6 * koef)
    right(90)
    fd(12 * koef)
    right(90)
up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()