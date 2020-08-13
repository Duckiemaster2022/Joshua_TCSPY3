class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = int(totalsecs // 3600)
        leftoversecs = totalsecs % 3600
        self.minutes = int(leftoversecs // 60)
        self.seconds = int(leftoversecs % 60)

    def __str__(self):
        return"{0} {1} {2}".format(self.hours, self.minutes, self.seconds)

    def increment(self, secs):
        final_secs = self.to_seconds() + secs
        final_time = MyTime(0, 0, final_secs)
        self.hours, self.minutes, self.seconds = final_time.hours, final_time.minutes, final_time.seconds

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __ge__(self, other):
        return self.to_seconds() >= other.to_seconds()

    def __le__(self, other):
        return self.to_seconds() <= other.to_seconds()

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    def between(self, other_2, other):
        print(self.to_seconds() <= other_2.to_seconds() < other.to_seconds())
        return self.to_seconds() <= other_2.to_seconds() < other.to_seconds()


def add_time(ti1, ti2):
    secs = ti1.to_seconds() + ti2.to_seconds()
    return MyTime(0, 0, secs)


# current_time = MyTime(9, 14, 30)
# bread_time = MyTime(3, 35, 0)
# done_time = add_time(current_time, bread_time)
# print(done_time)
# current_time.increment(500)
# print(current_time)
# done_time = add_time(current_time, bread_time)
# print(done_time)
# t1 = MyTime(10, 55, 12)
# t2 = MyTime(10, 48, 22)
# print(MyTime.after(t1, t2))
# t3 = t1 + t2
# print(t3)
# t3 = t1 - t2
# print(t3)
#
# if current_time.after(done_time):
#     print("The bread will be done before it starts!")
time = MyTime(9, 30, 0)
time2 = MyTime(9, 31, 0)
time3 = MyTime(9, 32, 0)
MyTime.increment(time, 60)
print(time)
MyTime.between(time, time2, time3)
