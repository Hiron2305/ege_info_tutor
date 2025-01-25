import turtle as tr

screen = tr.Screen()
screen.tracer(0)

k = 15

for i in range(3):
    tr.forward(7 * k)
    tr.right(90)
    tr.forward(12 * k)
    tr.right(90)

tr.up()

tr.forward(4 * k)
tr.right(90)
tr.forward(6 * k)
tr.left(90)

tr.down()

for i in range(4):
    tr.forward(83 * k)
    tr.right(90)
    tr.forward(77 * k)
    tr.right(90)

tr.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        tr.goto(x * k, y * k)
        tr.dot(3)

screen.update()
tr.mainloop()