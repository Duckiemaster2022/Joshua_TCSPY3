import sys
import turtle
import random
bob = turtle.Turtle()
wn = turtle.Screen()


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "test at line {0} OK.".format(linenum)
    else:
        msg = ("test at line {0} FAILED".format(linenum))
    print(msg)


def test_suite():
    test(counting_odd() == 5)
    test(sum_even() == 20)
    test(sum_of_neg() == -22)
    test(word_counting() == 2)
    test(counting_all_odd() == 4)
    test(countin_till_sam(["hi", "bye", "alive", "drive", "sam"]) == 4)
    test(countin_till_sam(["hi", "bye", "bob", "-1", "sam"]) == 4)
    test(countin_till_sam(["hi", "bye", "sammy", "drive", "sam"]) == 4)
    test(countin_till_sam(["hi", "bye", "alive", "sam", "light"]) == 3)
    test(countin_till_sam(["sam", "bye", "alive", "drive", "cucumber"]) == 0)
    test(countin_till_sam(["hi", "bye", "alive", "drive", "lol"]) == 5)
    test(countin_till_sam(["hi", "bye", "alive", "drive", 1]) == 4)
    test(newtons_sqrt(25) == 5.0)
    test(print_triangle_num(1) == 1)
    test(print_triangle_num(2) == 3)
    test(print_triangle_num(3) == 6)
    test(print_triangle_num(4) == 10)
    test(print_triangle_num(5) == 15)
    test(is_prime(73))
    test(is_prime(7))
    test(is_prime(2))
    test(is_prime(11))
    test(not is_prime(10))
    test(is_prime(23))
    test(is_prime(20050201))
    test(not is_prime(20000322))
    test(sum_of_squares(2, 3, 4) == 29)


def counting_odd():
    count_amount = 0
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in numbers:
        if i % 2 == 1:
            count_amount += 1
        elif i % 2 == 0:
            continue
    return count_amount


def sum_even():
    sum_of_num = 0
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in numbers:
        if i % 2 == 0:
            sum_of_num += i
        else:
            continue
    return sum_of_num


def sum_of_neg():
    number = [-1, -2, 3, -4, 5, -6, 7, 8, -9]
    sum_of_num = 0
    for i in number:
        if i < 0:
            sum_of_num += i
        else:
            continue
    return sum_of_num


def word_counting():
    word_list = ["hi", "bye", "alive", "drive"]
    count = 0
    for i in word_list:
        if len(i) == 5:
            count += 1
    return count


def counting_all_odd():
    numbers = [1, 3, 4, 5, 6, 7, 8, 9]
    sum_of_num = 0
    for i in numbers:
        if i % 2 == 1:
            sum_of_num += i
        elif i % 2 == 0:
            break
    return sum_of_num


def countin_till_sam(word_list):
    count = 0
    for i in word_list:
        if i == "sam":
            break
        elif type(i) != str:
            print(i, "is not a word")
            continue
        else:
            count += 1
    return count


def newtons_sqrt(n):
    approx = n / 2.0
    while True:
        better = (approx + n / approx) / 2.0
        if abs(approx - better) < 0.00000000000000000000000000001:
            return better
        approx = better


def print_triangle_num(n):
    return int(n * (n + 1) / 2)


def is_prime(numb):
    if numb == 2 or numb == 3 or numb == 5 or numb == 7:
        return True
    elif numb % 2 == 0:
        return False
    elif numb % 3 == 0:
        return False
    elif numb % 5 == 0:
        return False
    elif numb % 7 == 0:
        return False
    return True


def drunk_pirate(t):
    turn_list = [(160, 20), (-43, 10), (270, 8), (-43, 12)]
    for (turn, forw) in turn_list:
        t.fd(forw * 10)
        t.lt(turn)


def draw_house(t):
    t.seth(90)
    turn_list = [(50, 60), (29.5, 60), (29.5, 60), (50, 90), (50, 135), (70, -135), (50, -135.5), (70, 0)]
    for (forw, turn) in turn_list:
        t.fd(forw)
        t.lt(turn)
    t.pu()
    t.fd(300)


# def num_even_digits():
#     numb = 2091
#     str(numb)
#     print(numb[1])

def sum_of_squares(length, h, w):
    area = (length ** 2) + (h ** 2) + (w ** 2)
    return area


def play_once(c, y, t, who_played_first):
    score_c = c
    score_y = y
    score_t = t
    rng = random.Random()
    result = rng.randrange(-1, 2)
    computer = "computer"
    tie = "tie"
    you = "YOU"
    if who_played_first == 0:
        who_played_first += 1
        who_play_first = "You play first"
    else:
        who_played_first -= 1
        who_play_first = "computer plays first"
    if result == -1:
        score_y += 1
        print("{0}... the winner is.... {1}". format(who_play_first, you))
    elif result == 0:
        score_t += 1
        print("{0}... the winner is.... {1}".format(who_play_first, tie))
    elif result == 1:
        score_c += 1
        print("{0}... the winner is.... {1}".format(who_play_first, computer))
    print("you've tied", score_t, "times", "...", "You've lost", score_c, "times", "...", "You've won", score_y, "...", "times")
    print("your win percentage is... ", end=" ")
    print(adding_averages(score_y, score_c, score_t))
    play_again = (input("Do you want to play again [Y or N]"))
    if play_again == "Y" or play_again == "y":
        play_once(score_c, score_y, score_t, who_played_first)
    elif play_again == "N" or play_again == "n":
        print("Goodbye....")


def adding_averages(wins, two, three):
    total = (wins + two + three)
    win_percentage = ((wins / total) * 100)
    return win_percentage


# test_suite()
# drunk_pirate(bob)
# draw_house(bob)
# num_even_digits()
play_once(0, 0, 0, 0)


# wn.mainloop()
