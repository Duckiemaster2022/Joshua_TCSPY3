import turtle
from unit_tester import test
import time
import os

bob = turtle.Turtle()
sc = turtle.Screen()
bob.speed(0)


def koch(t, order, size, s):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            s = -s
            if s >= 0:
                t.color("red")
            else:
                t.color("blue")
            koch(t, order-1, size/3, 9)
            t.left(angle)

def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot


def r_max(nxs):
    """
    Find the maximum in a recursive structure of lists within other lists.
    precondition: No lists or sublists are empty
    """
    Largest = None
    first_time = True
    for e in nxs:
        if type(e) == type([]):
            val = r_max(e)
        else:
            val = e

        if first_time or val > largest:
            largest = val
            first_time = False

    return largest


def recursion_depth(number):
    print("{0}, ".format(number), end="")
    recursion_depth(number + 1)


def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t


def get_dirlist(path):
    """
    Return a sorted list of all entries in path.
    This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist


def print_files(path, prefix = ""):
    """Print recursive listing of contents of path"""
    if prefix == "": # detect outermost call, print a heading
        print("Folder listing for", path)
        prefix = "| "
    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix + f)
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            print_files(fullname, prefix + "| ")


print_files('C:/Users/Hannah')
# t0 = time.time()
# n = 35
# result = fib(n)
# t1 = time.time()
# print("fib({0}) = {1}, ({2:.2f} secs)". format(n, result, t1-t0))
# recursion_depth(0)
# koch(bob, 4, 1000, 9)
# test(r_max([2, 9, [1, 13], 8, 6]) == 13)
# test(r_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
# test(r_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
# test(r_max(["joe", ["sam", "ben"]]) == "sam")
#
#
# sc.mainloop()
