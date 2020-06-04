import random
import time
import adding
drng = random.Random(123)


def make_random_ints(num, lower_bound, upper_bound):
    rng = random.Random()
    results = []
    for i in range(num):
        results.append(rng.randrange(lower_bound, upper_bound))
    return results


def make_random_ints_2():
    xs = list(range(1, 13))
    rng = random.Random()
    rng.shuffle(xs)
    result = xs[:5]
    print(result)


def make_random_ints_no_dups(num, lower_bound, upper_bound):
    result = []
    rng = random.Random()
    for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
        print(result)
    return result


def do_my_sum(xs):
    sums = 0
    for v in xs:
        sums += v
    return sums


def time_stuff():
    sz = 10000000
    testdata = range(sz)
    t0 = time.clock()
    my_result = do_my_sum(testdata)
    t1 = time.clock()
    print("mr_result = {0}, (time taken = {1:.4f} seconds").format(my_result, t1 - t0)
    t2 = time.clock()
    their_result = sum(testdata)
    t3 = time.clock()
    print("their_result = {0} (time taken = {1:.4f} seconds").format(their_result, t3 - t2)


print(adding.add(5, 4))
# print(make_random_ints(5, 1, 13))
# print(make_random_ints_2())
# xs = make_random_ints_no_dups(5, 1, 10000000)
