# Решение

from turtle import *

tracer(0)
koef = 35
left(90)
for i in range(4):
    forward(14 * koef)
    right(90)
for i in range(5):
    forward(5 * koef)
    right(45)

up()
for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)

exitonclick()

answer = 61

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 15, answer, '093f65e080a295f8076b1c5722a46aa2'))