import turtle

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alex = turtle.Turtle()
alex.color("blue")



def h1():
    tess.forward(30)


def h2():
    tess.left(45)


def h3():
    tess.right(45)


def h4():
    wn.bye()


# def h5(x, y):
#     tess.goto(x, y)


def handler_for_tess(x, y):
    wn.title("tess clicked at {0}, {1}".format(x, y))
    tess.left(42)
    tess.forward(30)



def handler_for_alex(x, y):
    wn.title("alex clicked at {0}, {1}".format(x, y))
    alex.left(42)
    alex.forward(30)

def h6():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(h6, 200)


def draw_housing():
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()



# wn.onkey(h1, "Up")
# wn.onkey(h2, "Left")
# wn.onkey(h3, "Right")
# wn.onkey(h4, "q")
# # wn.onclick(h5)
# tess.onclick(handler_for_tess)
# alex.onclick(handler_for_alex)


h6()

wn.listen()
wn.mainloop()
