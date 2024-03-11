from turtle import *

k = 37
speed(0)
delay(0)

for _ in range(3):
    rt(45)
    fd(10 * k)
    rt(45)

rt(315)
fd(10 * k)

for _ in range(2):
    rt(90)
    fd(10 * k)

penup()

for x in range(-15, 10):
    for y in range(-15, 8):
        goto(x * k, y * k)
        dot(4, 'red')

mainloop()