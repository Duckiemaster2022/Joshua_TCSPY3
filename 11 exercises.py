def exer_1():
    print(list(range(10, 9, 1)))
    print("""    the three arguments of range 
    are (start, stop, and step), if start is
    less than stop, and the step is < 0 it returns 
    the a blank list, if start and stop are equal 
    it also returns a blank list, the same goes for
    if start is greater than stop and step is > 0""")


def exer_2():
    import turtle
    tess = turtle.Turtle()
    alex = tess
    alex.color("hotpink")
    print("""tess is assigned to the turtle object, than 
    alex is assigned to tess causing the to refer to the same
    turtle object, so basically tess and alex are two names for
    the same turtle object""")

def exer_3():
    a = [1, 2, 3]
    b = a[:]
    b[0] = 5
    print("""a = [1, 2, 3] b is then 
    assigned to the slice of a (containing 
    all of a), then be is changed to [5, 2,
    3], but since b was assigned to the 
    slice a not the same object it does not 
    change a """)


def exer_4():
    this = ["I", "am", "not", "a", "crook"]
    that = ["I", "am", "not", "a", "crook"]
    print("Test1:{0}".format(this is that))
    that = this
    print("Test2:{0}".format(this is that))
    print("""    this and that use two different 
    string objects unti this is a asigned to
    that is then using the same string object,
    that this is using""")

# exer_1()
# exer_2()
# exer_3()
# exer_4()
