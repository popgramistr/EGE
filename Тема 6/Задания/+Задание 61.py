# Решение

from turtle import *

k = 20
left(90)
x = 3
tracer(0)

forward((x + 2) * k)
for i in range(4):
    forward(x * k)
    right(90)
    forward((x + 2) * k)
right(90)
forward(x * k * 2)
for i in range(4):
    right(90)
    forward((3 * x - 1) * k)

up()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(3)
exitonclick()

x = 0
ans = 0
while ans <= 2000:
    x += 1
    ans = 11 * x ** 2 - 2 * x + 5
    print(x, ans)

answer = 14

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 61, answer, 'aab3238922bcc25a6f606eb525ffdc56'))