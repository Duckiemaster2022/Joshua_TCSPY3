mynewhandle = open("text.txt", "r")
while True:
    theline = mynewhandle.readline()
    if len(theline) == 0:
        break
    print(theline, end="")
