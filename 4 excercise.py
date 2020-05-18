import turtle


def make_turtle(colr, sz, spd):
    t = turtle.Turtle()
    t.pensize(sz)
    t.color(colr)
    t.speed(spd)
    return t


def make_window(colr, ttle):
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def draw_square(t):
    for f in range(5):
        for i in range(4):
            t.fd(20)
            t.lt(90)
        t.penup()
        t.seth(0)
        t.fd(40)
        t.pendown()


def draw_bigger_squares(t):
    s = 20
    for f in range(10):
        for i in range(4):
            t.fd(s)
            t.lt(90)
        s = s + 20
        t.penup()
        t.setpos(t.xcor() - 10, t.ycor()- 10)
        t.pendown()

def poly(t, n, sz):
    for i in range(n):
        t.fd(sz)
        t.lt(360/n)


def epic_squares(t, n):
    for i in range(n):
        t.lt(360 / n)
        for y in range(4):
            t.fd(100)
            t.lt(90)


def draw_spiral_squares(t):
    sides = 20
    for i in range(50):
        t.fd(sides)
        t.lt(90)
        sides = sides + 5


def draw_spiral_squares2(t):
    sides = 20
    for i in range(50):
        t.fd(sides)
        t.lt(91)
        sides = sides + 5


def draw_equitriangle(t, sz):
    poly(t, 3, sz)


def sum_to(n):
    sm = 0
    num = 0
    for i in range(n):
        num = num + 1
        sm = sm + num
        print(sm)


def area_of_circle(r):
    print(int(3.141592653589793238 * (r ** 2)))


def star(t):
    t.lt(36)
    for f in range(5):
        t.fd(100)
        t.lt(144)


def star2(t):
    t.lt(36)
    for i in range(5):
        for f in range(5):
            t.fd(100)
            t.lt(144)
        t.penup()
        t.fd(350)
        t.lt(144)
        t.pendown()


def star3(t):
    t.lt(36)
    for i in range(5):
        for f in range(5):
            t.fd(100)
            t.lt(144)
        t.fd(350)
        t.lt(144)


wn = make_window("limegreen", "Squares Everywhere!")
bob = make_turtle("blue", 3, 3)
# draw_square(bob)
# draw_bigger_squares(bob)
# poly(bob, 8, 50)
# epic_squares(bob, 20)
# draw_spiral_squares(bob)
# draw_spiral_squares2(bob)
# draw_equitriangle(bob, 100)
# sum_to(10)
# area_of_circle(25)
# star(bob)
# star2(bob)
# star3(bob)


wn.mainloop()
