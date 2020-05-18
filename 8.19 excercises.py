import sys


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        mesg = "test at line {0} OK.".format(linenum)
    else:
        mesg = ("test at line {0} FAILED".format(linenum))
    print(mesg)


def test_suite():
    # test(func_1() == None)
    # test(func_2() == None)
    # test(count_letters("kiwi", "i") == 2)
    # test(count_letters_2("banana", "a") == 3)
    test(finding_letters_in_paragraphs("""I don't know what to
    # say but there needs to be at least a couple of
    # e's in this paragraph so that it can actually
    # count something, otherwise i will get errors
    # galore... which would be very sad""") == 16)
    test(print_mult_table_12x12() == None)
    # test(reversing_strings("hello") == "olleh")
    # test(mirroring_strings("Hello") == "olleHHello")
    # test(removing_letters("bananajklad", "a") == "bnnjkld")
    # test(palindrome_check("bob") == "bob")
    # test(counting_substrings("bobbobbobbob", "bob") == 4)
    # test(removing_first_substring_ina_string("banana", "an") == "bana")
    # test(removing_first_substring_ina_string("bicycle", "cyc") == "bile")
    # test(removing_first_substring_ina_string("mississippi", "iss") == "missippi")


def func_1():
    print("y")
    print("g")
    print("9")
    print("myst")
    print("True")
    print("True")
    print("True")
    print("False")


def func_2():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter == "O" or letter == "Q":
            print(letter + "u" + suffix)
        print(letter + suffix)


def count_letters(fruit, letter):
    count = 0
    for char in fruit:
        if char == letter:
            count += 1
    return count


def count_letters_2(fruit, letter):
    word_length = len(fruit)
    count = 0
    start_num = 0
    old_index_num = -1
    temp_num = 0
    index_num = 0
    while index_num != -1:
        index_num = fruit.find(letter, start_num)
        temp_num = index_num - start_num
        start_num += (temp_num + 1)
        if old_index_num != index_num:
            count += 1
    return count

def count_letters_3_epic_version(fruit, letter):
    count = 0
    found = -1
    while fruit.find(letter, (found + 1)) != -1:
        found = fruit.find(letter, (found + 1))
        count += 1
    return count

# print(count_letters_3_epic_version("banana", "a"))

def percentages(e, everything_else):
    total = (e + everything_else)
    win_percentage = ((e / total) * 100)
    return win_percentage


def finding_letters_in_paragraphs(para):
    count = 0
    count_2 = 0
    para_split = para.split()
    for letter in para:
        if letter == "e":
            count += 1
        count_2 += 1
    percent = percentages(count, count_2)
    print('your text contains {0} words, of which {1} ({2}%) contain an "e"'.format(len(para_split), count, round(percent, 1)))
    return count


def print_mult_table_12x12():
    for i in range(1, 13):
        for s in range(1, 13):
            print(i * s, end="\t")
        print()


def reversing_strings(word):
    i = len(word) - 1
    reverse = ""
    while True:
        reverse += word[i]
        i -= 1
        if i == -1:
            break
    return reverse


def mirroring_strings(word):
    i = len(word) - 1
    reverse = ""
    while True:
        reverse += word[i]
        i -= 1
        if i == -1:
            i += 1
            while True:
                reverse += word[i]
                i += 1
                if i == len(word):
                    break
            break
    return reverse


def removing_letters(fruit, letter):
    word_without_the_letter = ""
    for char in fruit:
        if char == letter:
            continue
        word_without_the_letter += char
    return word_without_the_letter


def palindrome_check(word):
    i = len(word) - 1
    reverse = ""
    reverse_2 = ""
    while True:
        reverse += word[i]
        i -= 1
        if i == -1:
            i += 1
            while True:
                reverse_2 += word[i]
                i += 1
                if i == len(word):
                    break
            break
    if reverse == reverse_2:
        print("Its a palindrome!")
    else:
        print("This is not a palindrome!")
    return reverse


def counting_substrings(fruit, letter):
    word_length = len(fruit)
    count = 0
    start_num = 0
    loop_num = 0
    old_index_num = -1
    temp_num = 0
    while loop_num <= word_length:
        index_num = fruit.find(letter, start_num, word_length)
        if index_num == -1:
            break
        temp_num = index_num - loop_num
        loop_num += (temp_num + 1)
        start_num = loop_num
        if old_index_num != index_num:
            count += 1
    return(count)


def removing_first_substring_ina_string(fruit, letter):
    bob = fruit.find(letter)
    temp_num = bob
    temp_num_2 = bob + len(letter)
    temp_string = fruit[0:temp_num]
    temp_string_2 = fruit[temp_num_2:]
    string = temp_string + temp_string_2
    return string


# doesnt work
def removing_all_substrings_in_a_string_2(fruit, letter):
    word_length = len(fruit)
    start_num = 0
    temp_num_2 = 0
    string_2 = ""
    old_bob = 0
    while temp_num_2 <= word_length:
        bob = fruit.find(letter, start_num, word_length)
        print("hi")
        if temp_num_2 == word_length:
            print("failed")
            break
        temp_num = bob
        temp_num_2 = bob + len(letter)
        temp_string = fruit[start_num:temp_num]
        temp_string_2 = fruit[temp_num_2:]
        string = temp_string + temp_string_2
        string_2 = string_2 + string[old_bob:bob]
        start_num = temp_num_2
        old_bob = bob
    print(string_2)


test_suite()


# removing_all_substrings_in_a_string_2("banana", "an")
import math
math.ceil()
