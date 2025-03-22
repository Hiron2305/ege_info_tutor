from turtle import *

Sc = Screen()
Sc.tracer(0)

l = 10

for i in range(3):
    forward(19 * l)
    right(90)
    forward(3 * l)
    right(90)

for i in range(3):
    forward(5 * l)
    right(90)
    forward(11 * l)
    right(90)

up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * l, y * l)
        dot(3)

Sc.update()
Sc.mainloop()

#28