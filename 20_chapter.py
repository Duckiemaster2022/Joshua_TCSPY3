from unit_tester import test as t

opposites = {"up": "down", "right": "wrong", "yes": "no"}
alias = opposites
copy = opposites.copy() # Shallow copy
matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}


alreadyknown = {0: 0, 1: 1}
def test_suite():
    new_inventory = {}
    add_fruit(new_inventory, "strawberries", 10)
    print(new_inventory)
    t("strawberries" in new_inventory)
    t(new_inventory["strawberries"] == 10)
    add_fruit((new_inventory, "strawberries", 25))
    t(new_inventory["strawberries"] == 35)


def fib(n):
    if n not in alreadyknown:
        new_value = fib(n - 1) + fib(n - 2)
        alreadyknown[n] = new_value
    return alreadyknown[n]


def frequency_counting(word):
    letter_counts = {}
    for letter in word:
        letter.lower()
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    letter_items = list(letter_counts.items())
    letter_items.sort()
    print(letter_items)
    return letter_items


def alpha_strings(word):
    letter_counts = {}
    for letter in word:
        letter.lower()
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    del letter_counts[" "]
    letter_items = list(letter_counts.items())
    letter_items.sort()
    num = 0
    for letter in letter_items:
        print("{0}  {1}".format(letter_items[num][0], letter[1]))
        num += 1
    return letter_items


def exerc_2():
    print("a, instantiates a new dictionary")
    print("b, adds he key oranges with the value 20 to the dictionary")
    print("c, True")
    print("d, KeyError: 'pears'")
    print("e, adds pears to d with a value of 0 since it didnt exist already")
    print("f, creates a list of the keys from d and prints them")
    print("g, deletes the apple key from d then asks whethi er its"
          "in it or not, prints False")


def add_fruit(inventory, fruit, quantity=0):
    if fruit not in inventory:
        inventory.get(fruit, quantity)
    else:
        inventory[fruit] += quantity
    print(inventory)
    return inventory


# alpha_strings("ThiS is STring with Upper and lower case Letters")
# frequency_counting("mississippi")
# print(fib(995))
# test_suite()
