def exer_1(file, file_2):
    with open(file, "w") as f:
        f.write("hellooo\n")
        f.write("hello there\n")
        f.write("hellp\n")

    with open(file_2, "w") as f:
        for line in reversed(list(open(file_2))):
            f.write(line.rstrip)
            f.write("\n")


def exer_2(file, ):
    infile = open(file, "r")
    while True:
        text = infile.readline()
        if "snake" not in text:
            continue
        if text == 0:
            break
        print(text)
    infile.close()


def exer_3():
    infile = open("3.8_excercises.py", "r")
    outfile = open("exer_3_output_2.txt", "w")
    line_num = 1
    while True:
        text = infile.readline()
        outfile.write("{0:>5} {1}".format(line_num, text))
        if len(text) == 0:
            break
        line_num += 1
    outfile.close()
    infile.close()


def exer_4():
    infile = open("exer_3_output_2.txt", "r")
    outfile = open("exer_4_input.txt", "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        outfile.write("{0}\n".format(text[6:].rstrip()))
    outfile.close()
    infile.close()


# exer_3()
exer_4()

# exer_2("text.txt")
