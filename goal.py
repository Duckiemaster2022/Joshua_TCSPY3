class Goal:
    def __init__(self, balls=[]):
        self.balls = balls

    def add_ball(self, color):
        self.balls.insert(0, color)

    def get_owner(self):
        return self.balls[0]

    def __str__(self):
        return("{0}".format(self.balls))

    def get_points(self, color):
        points = 0
        for ball in self.balls:
            if ball == color:
                points += 1
        return points

    def remove_ball(self):
        self.balls.pop()


# game1 = Goal()
# game1.add_ball("red")
# game1.add_ball("blue")
# print(game1)
# print(game1.get_owner())
# print(game1.get_points("blue"))
# print(game1.get_points("red"))