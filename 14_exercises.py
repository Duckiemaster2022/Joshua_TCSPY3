from unit_tester import test

my_tickets = [[7, 17, 37, 19, 23, 43],
              [7,  2, 13, 41, 31, 43],
              [2,  5,  7, 11, 13, 17],
              [13, 17, 37, 19, 23, 43]]


def testsuite():
    # test(merge2([10, 7, 3, 4], [10, 3, 7, 0, 9]) == [10, 7, 3])
    # test(merge2([10], [9]) == [])
    # test(merge2([10, -3, 3, 4], [10, -3, 7, 0, 9]) == [10, -3])
    # test(merge2(["help"], [10, 3, 7, 0, 9]) == [])
    # test(merge3([10, 9, 8, 7], [6, 5, 4, 3]) == [10, 9, 8, 7])
    # test(merge4([10, 9, 8, 7], [6, 5, 4, 3]) == [6, 5, 4, 3])
    # test(merge5([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]) == [5, 11, 11, 12, 13])
    # test(not share_diagonal(5, 2, 2, 0))
    # test(share_diagonal(5, 2, 3, 0))
    # test(share_diagonal(5, 2, 4, 3))
    # test(share_diagonal(5, 2, 4, 1))
    # test(not col_clashes([6, 4, 2, 0, 5], 4))
    # test(not col_clashes([6, 4, 2, 0, 5, 7, 1, 3], 7))
    # test(col_clashes([0,1], 1))
    # test(col_clashes([5,6], 1))
    # test(col_clashes([6,5], 1))
    # test(col_clashes([0,6,4,3], 3))
    # test(col_clashes([5,0,7], 2))
    # test(not col_clashes([2,0,1,3], 1))
    # test(col_clashes([2,0,1,3], 2))
    # test(not has_clashes([6, 4, 2, 0, 5, 7, 1, 3]))  # Solution from above
    # test(has_clashes([4, 6, 2, 0, 5, 7, 1, 3]))  # Swap rows of first two
    # test(has_clashes([0, 1, 2, 3]))  # Try small 4x4 board
    # test(not has_clashes([2, 0, 3, 1]))
    # test(lotto_check([42, 4, 7, 11, 1, 13], [2, 5, 7, 11, 13, 17]) == 3)
    # test(lotto_check2(my_tickets, [2, 5, 7, 11, 13, 17]) == [2, 3, 6, 2])
    test(return_prime([42, 4, 7, 11, 1, 13]) == 3)


def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):           # If xs list is finished,
            result.extend(ys[yi:])  # Add remaining items from ys
            return result           # And we're done.
        if yi >= len(ys):           # Same again, but swap roles
            result.extend(xs[xi:])
            return result
        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def merge2(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    for i in xs:
        if i in ys:
            result.append(i)
        continue
    return result


def merge3(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    for i in xs:
        if i not in ys:
            result.append(i)
        continue
    return result


def merge4(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    for i in ys:
        if i not in xs:
            result.append(i)
        continue
    return result


def merge5(xs, ys):
    for i in ys:
        if i in xs:
            xs.remove(i)
    return xs


def share_diagonal(x0, y0, x1, y1):
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    return dx == dy


def col_clashes(bs, c):
    for i in range(c):
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False


def has_clashes(the_board):
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def main():
    import random
    rng = random.Random()
    bd = list(range(8))  # just change the number in range to change board size
    num_found = 0
    tries = 0
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("found solution {0} in {1} tries".format(bd, tries))
            tries = 0
            num_found += 1


def main2():
    import random
    rng = random.Random()
    bd = list(range(8))  # just change the number in range to change board size
    num_found = 0
    tries = 0
    solutions = []
    while num_found < 10:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            if bd not in solutions:
                continue
            solutions.append(bd)
            print("found solution {0} in {1} tries".format(bd, tries))
            tries = 0
            num_found += 1


def lotto_math():
    import random
    rng = random.Random()
    posi_lotto_nums = list(range(1, 50))
    rng.shuffle(posi_lotto_nums)
    return posi_lotto_nums


def lotto_check(ticket_num, lotto_draw):
    win_num = 0
    for i in ticket_num:
        if i in lotto_draw:
            win_num += 1
    return win_num


def lotto_check2(ticket_num, lotto_draw):
    result = []
    for lotto_tickets in ticket_num:
        win_num = 0
        for i in lotto_tickets:
            if i in lotto_draw:
                win_num += 1
        result.append(win_num)
    return result


def return_prime(xs):
    prime_nums = 0
    for num in xs:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_nums += 1
    return prime_nums


# draw = lotto_math()
testsuite()
# main()

