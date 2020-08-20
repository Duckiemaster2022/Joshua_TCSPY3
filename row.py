from goal import Goal
class Row:
    def __init__(self, goals=[]):
        self.goals = goals

    def get_row_owner(self):
        owns0 = self.goals[0].get_owner()
        if owns0 == self.goals[1].get_owner() == self.goals[2].get_owner():
            return owns0
        else:
            return None
