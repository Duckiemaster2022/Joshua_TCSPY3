from unit_tester import test
import seqtools
import calendar
import math
import copy
cal = calendar.TextCalendar()


def test_suite():
    test(exer_7(",", ";", "this,that,andsomeotherthing") ==
         "this;that;andsomeotherthing")
    test(exer_7(" ", "**", "Words will now be separated by stars.") ==
    "Words**will**now**be**separated**by**stars.")


def exer_1():
    cal.setfirstweekday(3)
    # print(cal.pryear(2020))
    cal.setfirstweekday(0)
    print(cal.formatmonth(2020, 2))
    d = calendar.LocaleTextCalendar(6, "JAPANESE")
    d.pryear(2012)


def exer_2():
    print("there are 55 math functions")
    print("they do floor and ceiling division")
    print("by doing the simple math that equates the same awnser")
    print("the three are", "e,", "tau,", "pi,")


def exer_3():
    x = 2
    y = 5
    c = copy.copy(x)
    x = 3
    c = copy.deepcopy(x)
    x = 4
    print(c)


def exer_6():
    print("that they're a good a idea")


def exer_7(old, new, s):
    """ Replace all occurrences of old with new in s. """
    x = new.join(s.split(old))
    return x


def exer_8():
    print("string.punctuation is missing the punctuation ’ ")
    print("it gave me a string like this:", "’now’", "rather than this:", "now")
# exer_1()
# exer_2()
# exer_3()
exer_8()

# test_suite()
