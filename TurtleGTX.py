import turtle
import random
rng = random.Random()
scr = turtle.Screen()
bilbo = turtle.Screen()


class TurtleGTX:
    def __init__(self):
        self.bob = turtle.Turtle()
        self.break_down_num = rng.randrange(100, 2000)
        self.odometer = 0
        print(self.break_down_num)

    def forward(self, dist):
        gap_between_odom_and_break_num = self.break_down_num - self.odometer
        if dist < 0:
            dist = -dist
        if self.odometer < self.break_down_num:
            if dist > gap_between_odom_and_break_num:
                self.bob.fd(gap_between_odom_and_break_num)
                self.odometer += gap_between_odom_and_break_num
            else:
                self.bob.fd(dist)
                self.odometer += dist
        else:
            print("your turtles wheel has broken down after {0} miles".format(self.odometer))
        print("odom num", self.odometer)

    def backward(self, dist):
        gap_between_odom_and_break_num = self.break_down_num - self.odometer
        if dist < 0:
            dist = -dist
        if self.odometer < self.break_down_num:
            if dist > gap_between_odom_and_break_num:
                self.bob.backward(gap_between_odom_and_break_num)
                self.odometer += gap_between_odom_and_break_num
            else:
                self.bob.backward(dist)
                self.odometer += dist
        else:
            print("your turtles wheel has broken down after {0} miles".format(self.odometer))
        print("odom num", self.odometer)

    def odometer_num(self):
        return "{0} odom num".format(self.odometer)

    def change_color(self, colors):
        self.bob.color(colors)

    def change_size(self, size):
        self.bob.pensize(size)

    def change_tyre(self):
        self.odometer = 0


turtle_stuff = TurtleGTX()
turtle_stuff.change_color("red")
turtle_stuff.change_size(5)
turtle_stuff.forward(50)
turtle_stuff.backward(-150)
turtle_stuff.forward(100)
turtle_stuff.backward(1)
turtle_stuff.forward(25)
turtle_stuff.change_tyre()
turtle_stuff.backward(200)
turtle_stuff.backward(100)
turtle_stuff.forward(500)
turtle_stuff.change_tyre()
turtle_stuff.backward(1)


scr.mainloop()