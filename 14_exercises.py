from unit_tester import test

my_tickets = [[7, 17, 37, 19, 23, 43],
              [7,  2, 13, 41, 31, 43],
              [2,  5,  7, 11, 13, 17],
              [13, 17, 37, 19, 23, 43]]

prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def testsuite():
    # test(merge_1([1, 3, 4, 5, 5], [1, 2, 4, 5, 6]) == [1, 4, 5])
    # test(merge_1([1, 2, 5, 5, 8], [2, 8, 11]) == [2, 8])
    # test(merge_1([10], [9]) == [])
    # test(merge_1([-4, -3, 3, 4], [-4, -3, 0, 7, 9]) == [-4, -3])
    # test(merge_1([1], [0, 3, 5, 7, 9]) == [])
    # test(merge_2([10, 9, 8, 7], [6, 5, 4, 3]) == [10, 9, 8, 7])
    # test(merge_3([10, 9, 8, 7], [6, 5, 4, 3]) == [6, 5, 4, 3])
    # test(merge_4([1, 2, 3, 4, 5, 6], [1, 2, 3, 5, 7, 9]) == [4, 6, 7, 9])
    # test(merge_5([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]) == [5, 11, 11, 12, 13])
    # test(not share_diagonal(5, 2, 2, 0))
    # test(share_diagonal(5, 2, 3, 0))
    # test(share_diagonal(5, 2, 4, 3))
    # test(share_diagonal(5, 2, 4, 1))
    # test(not col_clashes([6, 4, 2, 0, 5], 4))
    # test(not col_clashes([6, 4, 2, 0, 5, 7, 1, 3], 7))
    # test(col_clashes([0, 1], 1))
    # test(col_clashes([5, 6], 1))
    # test(col_clashes([6, 5], 1))
    # test(col_clashes([0, 6, 4, 3], 3))
    # test(col_clashes([5, 0, 7], 2))
    # test(not col_clashes([2, 0, 1, 3], 1))
    # test(col_clashes([2, 0, 1, 3], 2))
    # test(not has_clashes([6, 4, 2, 0, 5, 7, 1, 3]))  # Solution from above
    # test(has_clashes([4, 6, 2, 0, 5, 7, 1, 3]))  # Swap rows of first two
    # test(has_clashes([0, 1, 2, 3]))  # Try small 4x4 board
    # test(not has_clashes([2, 0, 3, 1]))
    # test(lotto_check([42, 4, 7, 11, 1, 13], [2, 5, 7, 11, 13, 17]) == 3)
    # test(lotto_check2(my_tickets, [2, 5, 7, 11, 13, 17]) == [2, 3, 6, 2])
    # test(return_prime([42, 4, 7, 11, 1, 13]) == 3)
    # test(prime_discover([[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]], prime_nums) == [[47]])
    test(lotto_check3(my_tickets) == 4)

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


def merge_1(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):           # If xs list is finished, # Add remaining items from ys
            return result           # And we're done.
        if yi >= len(ys):           # Same again, but swap roles
            return result
        if xs[xi] == ys[yi]:
            result.append(xs[xi])
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1


def merge_2(xs, ys):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            return result
        if yi >= len(ys):
            result.extend(xs[xi])
            return result

        if xs[xi] != ys[yi]:
            result.append(xs[xi])
            xi += 1
            yi += 1
        elif xs[xi] == ys[yi]:
            xi += 1
            yi += 1


def merge_3(xs, ys):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result
        if yi >= len(ys):
            return result
        if xs[xi] != ys[yi]:
            result.append(ys[yi])
            xi += 1
            yi += 1
        elif xs[xi] == ys[yi]:
            xi += 1
            yi += 1


def merge_4(xs, ys):
    result = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            result.extend(ys[yi:])
            return result
        if yi >= len(ys):
            result.extend(xs[xi:])
            return result
        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            result.append(ys[yi])
            yi += 1


def merge_5(xs, ys):
    result = xs[:]
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs):
            return result
        if yi >= len(ys):
            return result
        if xs[xi] == ys[yi]:
            result.remove(xs[xi])
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1


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
    print(posi_lotto_nums)
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


def return_prime_2(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) != 0:
                return False
        return True


def prime_discover(num, prime_list):
    result = []
    yi = 0
    xi = 0
    for lists in num:
        while True:
            if xi >= len(lists):
                result.append(prime_list[yi + 1:])
                return result
            lists.sort()
            if lists[xi] > prime_list[yi]:
                if return_prime_2(lists[xi]):
                    result.append(prime_list[xi:xi + 1])
                yi += 1
                xi += 1
            elif prime_list[yi] >= lists[xi]:
                xi += 1
            else:
                xi += 1
                yi += 1


def lotto_check3(ticket_num):
    win = lotto_math()
    result = []
    av_loss = 0
    for lotto_tickets in ticket_num:
        win_num = 0
        for i in lotto_tickets:
            if i in win:
                win_num += 1
        result.append(win_num)
        if win_num <= 3:
            av_loss += 1
    return av_loss


# draw = lotto_math()
testsuite()
# main()
