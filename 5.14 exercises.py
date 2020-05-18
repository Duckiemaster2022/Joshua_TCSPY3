import turtle


def exer_5_14_1(num):
    print(num)
    one = "sun"
    two = "mon"
    three = "tues"
    four = "wed"
    five = "thurs"
    six = "fri"
    seven = "sat"


def exer_5_14_2(days):
    print(days % 7 + 1)


def exer_5_14_6(mark):
    if mark >= 75:
        print("first")
    elif mark < 75 and mark >= 70:
        print("upper second")
    elif mark < 70 and mark >= 60:
        print("second")
    elif mark < 60 and mark >= 50:
        print("third")
    elif mark < 50 and mark >= 45:
        print("F1 Supp")
    elif mark < 45 and mark >= 40:
        print("F2")
    elif mark < 40:
        print("F3")


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


def draw_bar(t, h):
    height = h
    if height >= 200:
        t.color("blue", "red")
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

    if height <= 200 and height >= 100:
        t.color("blue", "yellow")
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

    if height < 100:
        t.color("blue", "green")
        t.begin_fill()
        t.lt(90)
        t.fd(height)
        if height <= 0:
            t.pu()
            t.back(15)
            t.write("  " + str(height))
            t.back(-15)
            t.pd()
            t.rt(90)
            t.fd(40)
            t.rt(90)
            t.fd(height)
            t.lt(90)
            t.end_fill()
            t.pu()
            t.fd(10)
            t.pd()


xs = [-48, 117, 200, 240, 160, 260, 220]


# exer_5_14_1(two)
# exer_5_14_2(137)
# exer_5_14_6(int(input("what is their grade")))
for a in xs:
    draw_bar(bob, a)

import math

