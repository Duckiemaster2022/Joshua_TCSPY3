import urllib.request


def writing_file(testfile):
    with open(testfile, "w") as f:
        f.write("My first file written from python\n")
        f.write("idk what to say")
        f.write("---------------\n")
        f.write("The End\n")


def sorting_text(testfile, sortedtestfile):
    f = open(testfile, "r")
    xs = f.readlines()
    f.close()

    xs.sort()

    g = open(sortedtestfile, "w")
    for v in xs:
        g.write(v)
    g.close()


def counting_words_in_a_file(testfile):
    f = open(testfile)
    content = f.read()
    f.close()

    word = content.split()
    print("there are", len(word), "words in the file")


def filter_(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if text[0] == "#":
            continue
        outfile.write(text)
    infile.close()
    outfile.close()


def how_to_open_files_elsewhere():
    wordsfile = open("c:/users/Hannah/Joshuas python programming/Joshua_TCSPY3/text.txt", "r")
    wordlist = wordsfile.readlines()
    print(wordlist[:6])


def website_stuff():
    url = "https://www.python.org/"
    destination_filename = "rfc793.txt"
    urllib.request.urlretrieve(url, destination_filename)


def retrieve_page(url):
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.readall())
    my_socket.close()
    return dta


# writing_file("test.txt")
# sorting_text("text.txt", "sorted_Text.txt")
# counting_words_ina_file("text.txt")
# how_to_open_files_elsewhere()
the_text = retrieve_page("https://www.python.org/")
