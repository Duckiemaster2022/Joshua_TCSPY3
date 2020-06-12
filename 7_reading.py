import sys
import random
rng = random.Random()
number = rng.randrange(1, 1000)


guesses = 0
msg = ""


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        mesg = "test at line {0} OK.".format(linenum)
    else:
        mesg = ("test at line {0} FAILED".format(linenum))
    print(mesg)


def test_suite():
    test(num_zero_and_five_digits(1055030250) == 7)
    test(num_zero_and_five_digits(0) == 1)


def seq3np1(n):
    """ Print the 3n+1 sequence from n,
    3 terminating when it reaches 1. 4 """
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:      # n is even #
            n = n // 2
        else:               # n is odd
            n = n * 3 + 1
    print(n, end=".\n")


def num_zero_and_five_digits(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n // 10
    return count

        
def two_squared(am_of_times_done):
    for x in range(am_of_times_done):
        print(x, "\t", 2 ** x)


def print_multiples(n, high):
    for i in range(1, high + 1):
        print(n * i, end="\t")
    print()


def print_mult_table(high):
    for i in range(1, high + 1):
        print_multiples(i, i)


def test_for_odd():
    for i in [12, 16, 17, 24, 29, 30]:
        if i % 2 == 1:
            continue
        print(i)
    print("done")


def sqrt(n):
    approx = n/2.0
    while True:
        better = (approx + n/approx) / 2.0
        if abs(approx - better) < 0.00001:
            return better
        approx = better
    return approx


# while True:
#     guess = int(input(msg + "\nGuess my number between 1 and 1000: "))
#     guesses += 1
#     if guess > number:
#         msg += str(guess) + " is too high.\n"
#     elif guess < number:
#         msg += str(guess) + " is too low.\n"
#     elif guess == number:
#         msg += str(guess) + " is correct!\n"
#         print(msg)
#         break


# test_suite()
# two_squared(13)
# test_for_odd()
print_mult_table(7)
print(sqrt(2))