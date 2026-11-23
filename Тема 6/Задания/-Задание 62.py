# Решение
from turtle import*

screensize(1920, 6000)
k = 20
tracer(0)
down()

right(180)
for _ in range(9):
    fd(59 * k)
    left(90)
    fd(84 * k)
    left(90)
up()
fd(18 * k)
left(90)
fd(38 * k)
right(90)
down()
for _ in range(9):
    fd(120 * k)
    right(90)
    fd(99 * k)
    right(90)
up()
for x in range(-100, 100):
    for y in range(-200, 200):
        goto(x * k, y * k)
        dot(3)

exitonclick()

answer = 162

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 62, answer, '06409663226af2f3114485aa4e0a23b4'))