from turtle import *
screen = Screen()
screen.tracer(0)
k = 10

for i in range(6):
    forward(25 * k)
    right(120)
up()

forward(20 * k)
left(90)
back(5 * k)
down()
for i in range(2):
    forward(20 * k)
    left(90)
    forward(10 * k)
    left(90)

up()

for x in range(-50, 50):
    for y in range(-50, 60):
        goto(x * k, y * k)
        dot(3)

update()
mainloop()