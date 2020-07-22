import os
import turtle
import time

win = turtle.Screen()
tess = turtle.Turtle()


def exists(filename):
    try:
        f = open(filename)
        f.close()
        return True
    except:
        return False


def exists_2(filename):
    if os.path.isfile(filename):
        return True
    return False


def get_age():
    age = int(input("please enter your age: "))
    if age < 0:
        # Create a new instance of an exception
        raise ValueError("{0} is not a valid age".format(age))
    return age


def recursion_depth(number):
    print("recursion depth number", number)
    try:
        recursion_depth(number + 1)
    except:
        print("I cannot go any deeper into this wormhole")


def show_poly():
    try:
        n = int(input("How many sides do you want in your polygon?"))
        angle = 360 / n
        for i in range(n):
            tess.forward(10)
            tess.left(angle)
        time.sleep(3)
    finally:
        win.bye()


def readposint():
    age = int(input("please enter your age: "))
    try:
        if age < 0:
            # Create a new instance of an exception
            raise ValueError("{0} is not a valid age".format(age))
    except:



# show_poly()
# show_poly()
# show_poly()
# recursion_depth(0)
# get_age()
readposint()