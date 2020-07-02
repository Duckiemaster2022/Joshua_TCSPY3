from math import sqrt


class Point:
    """point class represents and manupulates x,y coords"""
    def __init__(self, x=0, y=0):
        """create a new point at x, y"""
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """compute my distance from origin"""
        return ((self.x ** 2)+(self.y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """return the midpoint of points p1 and p2"""
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def distance(self, target):
        return sqrt((target.x - self.x) ** 2 + (target.y - self.y) ** 2)

    def reflect_x(self):
        return -self.y

    def slope_from_origin(self,):
        """ask for help"""
        return self.y - self.x

    def get_line_to(self, pt):
        slope = (self.y - pt.y) / (self.x - pt.x)
        return slope, self.y - self.x * slope


class Smsstore:
    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        result = ["unread", text_of_sms, time_arrived, from_number]
        self.inbox.append(result)

    def message_count(self):
        print("You have {0} messages".format(len(p.inbox)))
        return len(p.inbox)

    def get_unread_secrets(self, inbox):
        numbers = []
        for i in range(len(p.inbox)):
            if inbox[i][0] == "unread":
                i += 1
                numbers.append(i)
            else:
                numbers.append(-1)
        if numbers[0] != -1:
            print("Messages {0} are unread still".format(numbers))
        else:
            numbers.remove(-1)
        return numbers

    def get_message(self, index):
        index -= 1
        if index >= len(p.inbox):
            print("this message does not exist")
            return "this message does not exist"
        else:
            p.inbox[index][0] = "read"
            print(p.inbox[index], 1)
            return p.inbox[index]

    def delete(self,index):
        index -= 1
        yes_or_no = input("Are you sure you want to delete this? Y or N")
        if yes_or_no == "Y" or yes_or_no == "y":
            p.inbox.pop(index)
            print("deleted message {0}".format(index + 1))
        elif yes_or_no == "n" or yes_or_no == "N":
            print("canceled delete")
        else:
            print("invalid answer")
            p.delete(index)


    def clear(self):
        yes_or_no = input("Are you sure you want to clear your inbox? Y or N")
        if yes_or_no == "Y" or yes_or_no == "y":
            p.inbox = []
            print("Inbox has been cleared!")
        elif yes_or_no == "n" or yes_or_no == "N":
            print("canceled delete")
        else:
            print("invalid answer")
            p.clear()


p = Smsstore()
p.add_new_arrival(123, 1048, "hello my name is Biblert Bagbins")
p.add_new_arrival(143, 1123, "goodbye Jonathon Smith")
num = p.message_count()
num_of_unread = p.get_unread_secrets(p.inbox)
message = p.get_message(1)
p.delete(1)
message2 = p.get_message(2)
p.clear()
p.get_message(1)
print(p.inbox)
#
# p = Point(-7, 3)
# q = Point(4, 6)
# print(r)
# r = p.reflect_x()
# Point(4, 10).slope_from_origin(Point())
# print(Point(3, 4).halfway(Point(5, 12)))
# print(Point(4, 11).get_line_to(Point(6, 15)))
