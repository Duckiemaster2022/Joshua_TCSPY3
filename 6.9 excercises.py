import sys
import math


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "test at line {0} OK.".format(linenum)
    else:
        msg = ("test at line {0} FAILED".format(linenum))
    print(msg)


def test_suite():
    test(turn_clockwise("north") == "east")
    test(turn_clockwise("east") == "south")
    test(turn_clockwise("south") == "west")
    test(turn_clockwise("west") == "north")
    test(day_counter(0) == "Sun")
    test(day_counter(1) == "Mon")
    test(day_counter(2) == "Tues")
    test(day_counter(3) == "Wed")
    test(day_counter(4) == "Thur")
    test(day_counter(5) == "Fri")
    test(day_counter(6) == "Sat")
    test(day_counter_inverse("sunday") == 0)
    test(day_counter_inverse("monday") == 1)
    test(day_counter_inverse("tuesday") == 2)
    test(day_counter_inverse("wednesday") == 3)
    test(day_counter_inverse("thursday") == 4)
    test(day_counter_inverse("friday") == 5)
    test(day_counter_inverse("saturday") == 6)
    test(day_counter_inverse_2("monday", 4) == "friday")
    test(day_counter_inverse_2("thursday", -7) == "thursday")
    test(days_in_month("january") == 31)
    test(days_in_month("march") == 31)
    test(to_secs(1, 1, 60) == 3720)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433, 0, 0) == 8758)
    test(to_secs(0, 6.32, 0) == 379)
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)
    test(len("hello, world!") == 13)
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    # test(slope(5, 3, 4, 2) == 1.0)
    # test(slope(1, 2, 3, 2) == 0.0)
    # test(slope(1, 2, 3, 3) == 0.5)
    # test(slope(2, 4, 1, 2) == 2.0)
    # test(intercept(1, 6, 3, 12) == 3.0)
    # test(intercept(6, 1, 1, 6) == 7.0)
    # test(intercept(4, 6, 12, 8) == 5.0)
    test(is_even(8))
    test(not is_even(7))
    test(not is_even(349))
    test(is_odd(349))
    test(not is_odd(348))
    test(is_factor(3, 12))
    test(not is_factor(12, 3))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
    test(f2c(212) == 100)
    test(f2c(32) == 0)
    test(f2c(-40) == -40)
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)


def turn_clockwise(direc):
    s = "south"
    w = "west"
    n = "north"
    e = "east"
    if direc == n:
        return e
    elif direc == e:
        return s
    elif direc == s:
        return w
    elif direc == w:
        return n


def day_counter(nm):
    sun = 0
    mon = 1
    tues = 2
    wed = 3
    thur = 4
    fri = 5
    sat = 6

    if nm == sun:
        return "Sun"
    elif nm == mon:
        return "Mon"
    elif nm == tues:
        return "Tues"
    elif nm == wed:
        return "Wed"
    elif nm == thur:
        return "Thur"
    elif nm == fri:
        return "Fri"
    elif nm == sat:
        return "Sat"


def day_counter_inverse(num):
    sunday = "sunday"
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"
    saturday = "saturday"
    if num == sunday:
        return 0
    elif num == monday:
        return 1
    elif num == tuesday:
        return 2
    elif num == wednesday:
        return 3
    elif num == thursday:
        return 4
    elif num == friday:
        return 5
    elif num == saturday:
        return 6


def day_counter_inverse_2(cur_day, days_away):
    sunday = "sunday"
    monday = "monday"
    tuesday = "tuesday"
    wednesday = "wednesday"
    thursday = "thursday"
    friday = "friday"
    saturday = "saturday"
    sun = 0
    mon = 1
    tues = 2
    wed = 3
    thur = 4
    fri = 5
    sat = 6

    if cur_day == sunday:
        days_from_cur_day = (0 + days_away) % 7
        if days_from_cur_day == sun:
            return sunday
        elif days_from_cur_day == mon:
            return monday
        elif days_from_cur_day == tues:
            return tuesday
        elif days_from_cur_day == wed:
            return wednesday
        elif days_from_cur_day == thur:
            return thursday
        elif days_from_cur_day == fri:
            return friday
        elif days_from_cur_day == sat:
            return saturday
    elif cur_day == monday:
        days_from_cur_day = (1 + days_away) % 7
        if days_from_cur_day == sun:
            return sunday
        elif days_from_cur_day == mon:
            return monday
        elif days_from_cur_day == tues:
            return tuesday
        elif days_from_cur_day == wed:
            return wednesday
        elif days_from_cur_day == thur:
            return thursday
        elif days_from_cur_day == fri:
            return friday
        elif days_from_cur_day == sat:
            return saturday
    elif cur_day == tuesday:
        days_from_cur_day = (2 + days_away) % 7
        if days_from_cur_day == sun:
            return sunday
        elif days_from_cur_day == mon:
            return monday
        elif days_from_cur_day == tues:
            return tuesday
        elif days_from_cur_day == wed:
            return wednesday
        elif days_from_cur_day == thur:
            return thursday
        elif days_from_cur_day == fri:
            return friday
        elif days_from_cur_day == sat:
            return saturday
    elif cur_day == wednesday:
        days_from_cur_day = (3 + days_away) % 7
        if days_from_cur_day == sun:
            return sunday
        elif days_from_cur_day == mon:
            return monday
        elif days_from_cur_day == tues:
            return tuesday
        elif days_from_cur_day == wed:
            return wednesday
        elif days_from_cur_day == thur:
            return thursday
        elif days_from_cur_day == fri:
            return friday
        elif days_from_cur_day == sat:
            return saturday
    elif cur_day == thursday:
        days_from_cur_day = (4 + days_away) % 7
        if days_from_cur_day == sun:
            return sunday
        elif days_from_cur_day == mon:
            return monday
        elif days_from_cur_day == tues:
            return tuesday
        elif days_from_cur_day == wed:
            return wednesday
        elif days_from_cur_day == thur:
            return thursday
        elif days_from_cur_day == fri:
            return friday
        elif days_from_cur_day == sat:
            return saturday
    elif cur_day == friday:
        days_from_cur_day = (5 + days_away) % 7
        if days_from_cur_day == sun:
            return sunday
        elif days_from_cur_day == mon:
            return monday
        elif days_from_cur_day == tues:
            return tuesday
        elif days_from_cur_day == wed:
            return wednesday
        elif days_from_cur_day == thur:
            return thursday
        elif days_from_cur_day == fri:
            return friday
        elif days_from_cur_day == sat:
            return saturday
    elif cur_day == saturday:
        days_from_cur_day = (6 + days_away) % 7
        if days_from_cur_day == sun:
            return sunday
        elif days_from_cur_day == mon:
            return monday
        elif days_from_cur_day == tues:
            return tuesday
        elif days_from_cur_day == wed:
            return wednesday
        elif days_from_cur_day == thur:
            return thursday
        elif days_from_cur_day == fri:
            return friday
        elif days_from_cur_day == sat:
            return saturday


def days_in_month(month):
    jan = "january"
    feb = "febuary"
    march = "march"
    april = "april"
    may = "may"
    june = "june"
    july = "july"
    aug = "august"
    sep = "september"
    octo = "october"
    nov = "november"
    dec = "december"

    if month == jan:
        return 31
    elif month == feb:
        return 28
    elif month == march:
        return 31
    elif month == april:
        return 30
    elif month == may:
        return 31
    elif month == june:
        return 30
    elif month == july:
        return 31
    elif month == aug:
        return 31
    elif month == sep:
        return 30
    elif month == octo:
        return 30
    elif month == nov:
        return 30
    elif month == dec:
        return 31


def to_secs(hr, minute, sec):
    min_from_hr = hr * 60
    sec_from_min_from_hr = int(min_from_hr * 60)
    secs_from_min = int(minute * 60)
    tot_secs = int(sec) + sec_from_min_from_hr + secs_from_min
    return tot_secs


def hours_in(hr):
    hours = int((((hr / 60) / 60) % 60))
    return hours


def minutes_in(minute):
    minutes = int(((minute / 60) % 60))
    return minutes


def seconds_in(secd):
    seconds = int(secd % 60)
    return seconds


def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1


def hypotenuse(a, b):
    c_squared = float(((a ** 2) + (b ** 2)))
    return math.sqrt(c_squared)


def slope(x1, y1, x2, y2):
    if x2 == x1:
        return "slope of vertical line is undefined"
    return (y2 - y1) / (x2 - x1)


def intercept(x1, y1, y2, x2):
    intercep = y2 - (slope(x1, y1, x2, y2)) * x2
    return intercep


def is_even(numb):
    if numb % 2 <= 0:
        return True
    else:
        return False


def is_odd(numb):
    if numb % 2 > 0:
        return True
    else:
        return False


def is_factor(numb_one, numb_two):
    if numb_two % numb_one == 0:
        return True
    return False


def is_multiple(numb_one, numb_two):
    if numb_one % numb_two == 0:
        return True
    return False


def f2c(f):
    temp = round(((f - 32) / 1.8))
    return temp


def c2f(c):
    temp = round(((c * 1.8) + 32))
    return temp


test_suite()
