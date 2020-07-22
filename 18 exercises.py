import turtle


t = turtle.Turtle()
sc = turtle.Screen()
t.color("blue")
t.speed(0)


def koch(a, order, size, s):
    if order == 0:
        a.forward(size)
    else:
        for angle in [95, 95, 95, 95, 95]:
            s = -s
            if s >= 0:
                a.color("red")
            else:
                a.color("blue")
            koch(a, order-1, size/3, 9)
            a.left(angle)

koch(t, 4, 10000, 6)
sc.mainloop()
