from turtle import *
screen = Screen()
screen.tracer(0)
k = 10

for i in range(2):
    forward(5 * k)
    right(90)
    forward(15 * k)
    right(90)

up()

forward(-7 * k)
right(90)
forward(12 * k)
left(90)

down()

for i in range(2):
    forward(65 * k)
    right(90)
    forward(120 * k)
    right(90)


up()

for x in range(-50, 50):
    for y in range(-50, 60):
        goto(x * k, y * k)
        dot(3)

update()
mainloop()