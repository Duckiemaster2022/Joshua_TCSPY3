from unit_tester import test
import string


def testsuit():
    test(cleanword("what?") == "what")
    test(cleanword("’now!’") == "now")
    test(cleanword("?+=’w-o-r-d!,@$()’") == "word")
    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))
    test(extract_words("Now is the time! Now is the time? Yes, now.") ==
         ['Now', 'is', 'the', 'time!', 'Now', 'is', 'the', 'time?', 'Yes,', 'now.'])
    test(extract_words("she tried to curtsey as she spoke--fancy") ==
         ["she", "tried", "to", "curtsey", "as", "she", "spoke--fancy"])
    test(wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
    test(wordcount("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
    test(wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
    test(wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)
    test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are", "be", "but", "is", "or"])
    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this", "supercalifragilisticexpialidocious"]) == 34)
    test(longestword([]) == 0)


def cleanword(s):
    punctuation = r"""’!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    s_sans_punct = ""
    for letter in s:
        letter.lower()
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct


def has_dashdash(s):
    if s.find("--") >= 0:
        return True
    return False


def extract_words(s):
    x = s.split()
    return x


def wordcount(word, s):
    x = s.count(word)
    return x


def wordset(list):
    x = []
    for i in list:
        if i in x:
            continue
        x.append(i)
        x.sort()
    return x


def longestword(s):
    x = 0
    for i in s:
        if len(i) > x:
            x = len(i)
        continue
    return x


# testsuit()
