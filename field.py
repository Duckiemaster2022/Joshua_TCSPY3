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

    def total_score(self, point_1, point_2):
        return point_1 + point_2

    def get_all_goal_points(self, color):
        goal_points = 0
        for i in self.goals:
            goal_points += Goal.get_points(i, color)
        return goal_points

    def get_all_row_points(self, color):
        points = 0
        for row in self.rows:
            if row.get_row_owner() == color:
                points += 6
        return points

    def print_score(self, tot_score, color):
        print("{0} team scored {1} points".format(color, tot_score))

    def add_ball(self, goal_num, color):
        self.goals[goal_num].add_ball(color)

    def subtract_ball(self, goal_num):
        self.goals[goal_num].remove_ball()

    def display_field(self):
        pass

field1 = Field("skills")
goal_point = field1.get_all_goal_points("blue")
rows_point = field1.get_all_row_points("blue")
tot_score = field1.total_score(goal_point, rows_point)
field1.print_score(tot_score, "blue")
