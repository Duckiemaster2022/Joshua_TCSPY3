import turtle
wn = turtle.Screen()
wn.bgcolor("white")
bob = turtle.Turtle()


def ex_thirteen(t, n):
    t.speed(0)
    for i in range(n):
        t.penup()
        deg = 360 / n
        t.lt(deg)
        t.fd(100)
        t.stamp()
        t.back(100)


def ex_fourteen():
    print("bale", "turn", "dole", "nest")


def ex_fifteen():
    print("pythons,", "no it is a boa,", "No")


# ex_thirteen(bob, 1000)
# ex_fourteen()
# ex_fifteeen()


wn.mainloop()
