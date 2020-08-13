import os
import turtle
import time

# win = turtle.Screen()
# tess = turtle.Turtle()


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


def show_poly_2():
    try:
        win = turtle.Screen()   # Grab/create a resource, e.g. a window
        tess = turtle.Turtle()

        # This dialog could be cancelled,
        #   or the conversion to int might fail, or n might be zero.
        n = int(input("How many sides do you want in your polygon?"))
        angle = 360 / n
        for i in range(n):      # Draw the polygon
            tess.forward(10)
            tess.left(angle)
        time.sleep(3)
        win.bye()
        print("byebye")
        # Make program wait a few seconds
    finally:
        print("hi")
        pass  # Close the turtle's window


def readposint():
    age = (input("please enter your age: "))
    try:
        val = int(age)
        if val <= 0:
            print("{0} is a integer, but isnt positive!".format(val))
        else:
            print("{0} is a positive integer".format(val))
    except:
        if age == "":
            raise TypeError("you didnt type in anything!")
        else:
            raise TypeError("{0} isn't a integer!".format(age))

# show_poly_2()
# show_poly_2()
# show_poly_2()
# recursion_depth(0)
# get_age()


readposint()
