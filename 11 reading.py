# xs = [1, 2, 3, 4, 5]
# print(xs)
# for i in range(len(xs)):
#     xs[i] = xs[i]**2
# # print(xs)
#
#
# for (i, val) in enumerate(xs):
#     print(val, "this be i >", i)
#     xs[i] = val**2
# print(xs)
#
#
# for (i, v) in enumerate(["banana", "apple", "pear", "lemon"]):
#     print(i, v)


# def double_stuff(a_list):
#     for (idx, val) in enumerate(a_list):
#         a_list[idx] = val * 2
#     return a_list

# things = [2, 5, 9]
# print(double_stuff(things))
#
#
# mylist = ["hi", "bye", "lie", "hi"]
# print(mylist.count("hi"))

# def double_stuff_2(a_list):
#     new_list = []
#     for value in a_list:
#         new_elem = 2 * value
#         new_list.append(new_elem)
#     return new_list
#
# things = double_stuff_2(things)
# print(things)
# import turtle
# wn = turtle.Screen()
# tess = turtle.Turtle()
# alex = tess
# alex.color("hotpink")
#
# tess.lt(90)
# tess.fd(100)
# alex.lt(90)
# alex.fd(30)
# wn.mainloop()


a = [1, 2, 3]
b = a[:]
b[0] = 5

print("""a = [1, 2, 3] b is then 
assigned to the slice of a (containing 
all of a), then be is changed to [5, 2,
3], but since b was assigned to the 
slice a not the same object it does not 
change a """)