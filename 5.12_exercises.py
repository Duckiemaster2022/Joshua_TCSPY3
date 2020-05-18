import turtle


def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, coolr, sz, spd):
    t = turtle.Turtle()
    t.pensize(sz)
    t.color(colr, coolr)
    t.speed(spd)
    return t


wn = make_window("limegreen", "hi")
bob = make_turtle("blue", "orange", 3, 3)


def draw_bar(t, height):
    t.begin_fill()
    t.lt(90)
    t.fd(height)
    t.write("  " + str(height))
    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(height)
    t.lt(90)
    t.end_fill()
    t.pu()
    t.fd(10)
    t.pd()


xs = [48, 117, 200, 240, 160, 260, 220]

for a in xs:
    draw_bar(bob, a)


wn.mainloop()
