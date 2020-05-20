import turtle


# turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alex = turtle.Turtle()
bobby = turtle.Turtle()
pen = 3
shape = 0
size = 3
state_num = 0
state_num_2 = 2


def h1():
    tess.forward(30)


def h2():
    tess.left(45)


def h3():
    tess.right(45)


def h4():
    print("goodbye.... :(.... forever... :)")
    wn.bye()


def h5(x, y):
    tess.goto(x, y)


def h6():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(h6, 200)


def color_r():
    tess.color("red")


def color_b():
    tess.color("blue")


def color_g():
    tess.color("green")


def size_plus():
    global pen
    wn.title("tess pensize {0}".format(pen))
    if pen >= 20:
        return
    else:
        pen += 1
        tess.pensize(pen)


def size_minus():
    global pen
    wn.title("tess pensize {0}".format(pen))
    if pen <= 0:
        return
    else:
        pen += -1
        tess.pensize(pen)


def tess_shape():
    global shape
    if shape == 0:
        tess.shape("circle")
    elif shape == 1:
        tess.shape("arrow")
    elif shape == 2:
        tess.shape("square")
    elif shape == 3:
        tess.shape("turtle")
    shape += 1
    if shape >= 4:
        shape = 0


def tess_size_u():
    global size
    if size >= 20:
        return
    else:
        size += 1
        tess.shapesize(size)


def tess_size_d():
    global size
    wn.title("tess shape size {0}".format(size))
    if size <= 1:
        return
    else:
        size -= 1
        tess.shapesize(size)


def handler_for_tess(x, y):
    wn.title("tess clicked at {0}, {1}".format(x, y))
    tess.left(42)
    tess.forward(30)


def handler_for_alex(x, y):
    wn.title("alex clicked at {0}, {1}".format(x, y))
    alex.left(42)
    alex.forward(30)


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


def init_stoplight():
    draw_housing()
    tess.hideturtle()
    tess.penup()
    tess.forward(40)
    tess.left(90)
    tess.forward(50)
    tess.shape("circle")
    tess.shapesize(3)
    tess.fillcolor("yellow")
    tess.goto(40.0, 119)
    alex.penup()
    alex.hideturtle()
    alex.shape("circle")
    alex.shapesize(3)
    alex.fillcolor("red")
    alex.goto(40.0, 189)
    bobby.penup()
    bobby.goto(40.0, 48)
    bobby.shape("circle")
    bobby.shapesize(3)
    bobby.fillcolor("green")


def init_stoplight_2():
    draw_housing()
    tess.hideturtle()
    tess.penup()
    tess.forward(40)
    tess.left(90)
    tess.forward(50)
    tess.shape("circle")
    tess.shapesize(3)
    tess.fillcolor("darkgoldenrod")
    tess.goto(40.0, 119)
    alex.hideturtle()
    alex.penup()
    alex.shape("circle")
    alex.shapesize(3)
    alex.fillcolor("darkred")
    alex.goto(40.0, 189)
    bobby.hideturtle()
    bobby.penup()
    bobby.goto(40.0, 48)
    bobby.shape("circle")
    bobby.shapesize(3)
    bobby.fillcolor("DarkOliveGreen")
    tess.showturtle()
    alex.showturtle()
    bobby.showturtle()


def advance_state_machine():
    global state_num
    if state_num == 0:
        tess.goto(40.0, 119)
        tess.fillcolor("yellow")
        state_num = 1
    elif state_num == 1:
        tess.goto(40.0, 189)
        tess.fillcolor("red")
        state_num = 2
    else:
        tess.goto(40.0, 48)
        tess.fillcolor("green")
        state_num = 0


def advance_state_machine_2():
    global state_num_2
    if state_num_2 == 0:
        bobby.goto(40.0, 119)
        bobby.fillcolor("yellow")
    elif state_num_2 == 1:
        bobby.goto(40.0, 189)
        bobby.fillcolor("red")
    elif state_num_2 == 2:
        bobby.goto(40.0, 48)
        bobby.fillcolor("green")
    state_num_2 += 1
    if state_num_2 >= 3:
        state_num_2 = 0
    wn.ontimer(advance_state_machine_2, 2000)


def advance_state_machine_fixed_2():
    global state_num_2
    if state_num_2 == 0:
        bobby.hideturtle()
        tess.showturtle()
    elif state_num_2 == 1:
        tess.hideturtle()
        alex.showturtle()
    elif state_num_2 == 2:
        alex.hideturtle()
        bobby.showturtle()
    state_num_2 += 1
    if state_num_2 >= 3:
        state_num_2 = 0
    wn.ontimer(advance_state_machine_fixed_2, 2000)


def advance_state_machine_3():
    global state_num_2
    if state_num_2 == 0:
        tess.fillcolor("yellow")
        bobby.fillcolor("DarkOliveGreen")
    elif state_num_2 == 1:
        alex.fillcolor("red")
        tess.fillcolor("darkgoldenrod")
    elif state_num_2 == 2:
        bobby.fillcolor("green1")
        alex.fillcolor("darkred")
    state_num_2 += 1
    if state_num_2 >= 3:
        state_num_2 = 0
    wn.ontimer(advance_state_machine_3, 2000)


def green():
    bobby.fillcolor("green1")
    alex.fillcolor("darkred")
    wn.ontimer(green_yellow, 3000)


def green_yellow():
    tess.fillcolor("yellow")
    wn.ontimer(yellow, 1000)


def yellow():
    tess.fillcolor("yellow")
    bobby.fillcolor("DarkOliveGreen")
    wn.ontimer(red, 1000)


def red():
    alex.fillcolor("red")
    tess.fillcolor("darkgoldenrod")
    wn.ontimer(green, 2000)


def advance_state_machine_4():
    green()


def excer_2():
    init_stoplight()
    advance_state_machine_2()


def excer_3():
    init_stoplight()
    advance_state_machine_fixed_2()


def excer_4():
    init_stoplight_2()
    advance_state_machine_3()


def excer_5():
    init_stoplight_2()
    advance_state_machine_4()


# excer_2()
# excer_3()
# excer_4()
# excer_5()
# excer_6()


wn.onkey(tess_size_u, "u")
wn.onkey(tess_size_d, "j")
wn.onkey(size_plus, "=")
wn.onkey(size_minus, "-")
wn.onkey(advance_state_machine, "space")
wn.onkey(color_b, "b")
wn.onkey(color_r, "r")
wn.onkey(color_g, "g")
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onclick(h5)
tess.onclick(handler_for_tess)
alex.onclick(handler_for_alex)
# h6()


wn.listen()
wn.mainloop()
