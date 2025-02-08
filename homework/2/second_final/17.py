from turtle import *

screen = Screen()
screen.tracer(0)

k = 10

for i in range(2):
    forward(10 * k)
    right(90)
    forward(18 * k)
    right(90)

up()

forward(5 * k)
right(90)
forward(7 * k)
left(90)

down()

for i in range(2):
    forward(10 * k)
    right(90)
    forward(7 * k)
    right(90)


up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3)

screen.update()
mainloop()
#249

# 18 - 12, 19 - 4, 20 - 132, 21 - 10