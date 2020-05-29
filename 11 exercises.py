import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        mesg = "test at line {0} OK.".format(linenum)
    else:
        mesg = ("test at line {0} FAILED".format(linenum))
    print(mesg)


def test_suite():
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 1, 1], [1, 2, 3]) == [2, 3, 4])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    test(dot_product([1, 1], [1, 1]) == 2)
    test(dot_product([1, 2], [1, 4]) == 9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    test(exer_10("i am old are u old is anyone else old", "old", "new") == "i am new are u new is anyone else new")


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


def add_vectors(a_list, b_list):
    empty_list = []
    temp_3 = 0
    temp_4 = 0
    temp_5 = 0
    if len(a_list) == 2:
        for (a, b) in a_list, b_list:
            temp_3 += a
            temp_4 += b
        empty_list.append(temp_3)
        empty_list.append(temp_4)
        return empty_list
    if len(a_list) == 3:
        for (a, b, c) in a_list, b_list:
            temp_3 += a
            temp_4 += b
            temp_5 += c
        empty_list.append(temp_3)
        empty_list.append(temp_4)
        empty_list.append(temp_5)
        return empty_list


def scalar_mult(mult_num, a_list):
    empty_string = []
    for i in a_list:
        answer = mult_num * i
        empty_string.append(answer)
    return empty_string


def dot_product(a_list, b_list):
    temp_3 = 1
    temp_4 = 1
    temp_5 = 1
    if len(a_list) == 2:
        for (a, b) in a_list, b_list:
            temp_3 = a * temp_3
            temp_4 = b * temp_4
            temp_5 = temp_3 + temp_4
        return temp_5
    if len(a_list) == 3:
        for (a, b, c) in a_list, b_list:
            temp_3 = a * temp_3
            temp_4 = b * temp_4
            temp_5 = c * temp_5
            temp_6 = temp_3 + temp_4 + temp_5
        return temp_6


def exer_9():
    song = "The rain in Spain..."
    print(" ".join(song.split()))
    print(song)
    print("its the same")


def exer_10(b_list, repla, new):
    a_list = b_list[:]
    for i in a_list:
        if repla not in a_list:
            break
        index = a_list.index(repla)
        a_list = a_list[:index] + a_list[len(repla) + index:]
        a_list = a_list[:index] + new + "" + a_list[(len(repla) - len(new)) + index:]
    return a_list


def exer_11():
    def swap_correct(x, y):
        print("before swap statement: x:", x, "y:", y)
        (x, y) = (y, x)
        print("after swap statement: x:", x, "y:", y)


    a = ["this", "is", "fun"]
    b = [2, 3, 4]
    swap_correct(a, b)
    print("this is a and b but their values haven't changed", a, b)


    def swap(x, y):
        return y, x
    a, b = swap(["this", "is", "fun"], [2, 3, 4])
    print(a, b)


# exer_1()
# exer_2()
# exer_3()
# exer_4()
# exer_9()
test_suite()
# exer_11()
