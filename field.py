from goal import Goal
from row import Row


class Field:
    goals = []
    rows = []
    def __init__(self, type):
        if type == "skills":
            self.goals.append(Goal(["blue", "blue"]))
            self.goals.append(Goal(["blue"]))
            self.goals.append(Goal(["blue", "blue"]))
            self.goals.append(Goal(["blue"]))
            self.goals.append(Goal(["blue", "blue", "blue"]))
            self.goals.append(Goal(["blue"]))
            self.goals.append(Goal(["blue", "blue"]))
            self.goals.append(Goal(["blue"]))
            self.goals.append(Goal(["blue", "blue"]))
            self.rows.append(Row([self.goals[0], self.goals[1], self.goals[2]]))
            self.rows.append(Row([self.goals[3], self.goals[4], self.goals[5]]))
            self.rows.append(Row([self.goals[6], self.goals[7], self.goals[8]]))
            self.rows.append(Row([self.goals[0], self.goals[3], self.goals[6]]))
            self.rows.append(Row([self.goals[1], self.goals[4], self.goals[7]]))
            self.rows.append(Row([self.goals[2], self.goals[5], self.goals[8]]))
            self.rows.append(Row([self.goals[0], self.goals[4], self.goals[8]]))
            self.rows.append(Row([self.goals[2], self.goals[4], self.goals[6]]))

    def __str__(self):
        return "{0}".format("hi")

    def total_score(self):
        pass

    def get_all_goal_points(self):
        red_goal_points = 0
        blue_goal_points = 0
        for i in self.goals:
            red_goal_points += Goal.get_points(i, "red")
        for i in self.goals:
            blue_goal_points += Goal.get_points(i, "blue")
        return blue_goal_points, red_goal_points

    def get_all_row_points(self):
        red_rows = 0
        blue_rows = 0
        for i in self.rows:
            red_rows += Row.get_row_owner()
        print(red_rows)

    def print_score(self):
        pass

    def add_ball(self, goal_num, color):
        self.goals[goal_num].add_ball(color)

    def subtract_ball(self, goal_num):
        self.goals[goal_num].remove_ball()

    def display_field(self):
        pass

field1 = Field("skills")
print(field1.get_all_goal_points())
field1.get_all_row_points()