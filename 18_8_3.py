import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.speed(4)




def s_triangle(t, order, size):
    if order == 0:
        for i in range(3):
            t.forward(size)
            t.left(120)
    else:
        s_triangle(t, order - 1, size / 2)
        t.right(120)
        s_triangle(t, order - 1, size / 2)
        t.right(120)
        t.forward(size / 2)
        t.right(120)
        s_triangle(t, order - 1, size / 2)


s_triangle(t, 4, 900)
s.mainloop()
