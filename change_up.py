fts = {}
balls = ["VOID", "red_ball", "blue_ball"]
towers = ["red_left", "red_middle", "red_right", "mid_left",
          "mid_middle", "mid_right", "blue_left", "blue_middle",
          "blue_right"]
num_list = ["first", "second", "third"]


def tower_init(norm=1):
    global fts
    if norm == 0:
        fts = {1: [2, 2, 0], 2: [2, 0, 0], 3: [2, 2, 0],
               4: [2, 0, 0], 5: [2, 2, 2], 6: [2, 0, 0],
               7: [2, 2, 0], 8: [2, 0, 0], 9: [2, 2, 0]}
    else:
        fts = {1: [1, 2, 0], 2: [1, 2, 0], 3: [1, 2, 0],
               4: [1, 2, 1], 5: [0, 0, 0], 6: [2, 1, 2],
               7: [2, 1, 0], 8: [2, 1, 0], 9: [2, 1, 0]}


def print_towers():
    for i in range(1, len(fts) + 1):
        print(towers[i - 1])
        for s in fts[i]:
            print(balls[s])
        print("\n")

def print_one_tower(tower):
    print(towers[tower])
    for i in fts[tower]:
        print(balls[i])

def count():
    red_points = 0
    blue_points = 0
    for i in range(1, len(fts) + 1):
        for s in fts[i]:
            if s == 1:
                red_points += 1
            elif s == 2:
                blue_points += 1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", "\n", red_points, blue_points)
    return red_points, blue_points

def change_tower_scores():
    red_counter = 0
    blue_counter = 0
    for i in range(1, 10):
        counter = 0
        for s in num_list:
            current_tower = input("What ball is in the {0} slot of the {1} tower?".format(s, towers[i - 1]))
            while int(current_tower) < 0 or int(current_tower) > 2:
                print("that is an invalid number please try a different one")
                current_tower = input("What ball is in the {0} slot of the {1} tower?".format(s, towers[i - 1]))
                if int(current_tower) >= 0 and int(current_tower) <= 2:
                    break
            while int(current_tower) == 1 or int(current_tower) == 2:
                if current_tower == 1:
                    if red_counter < 16:
                        red_counter += 1
                        break
                    else:
                        print("you are not allowed to have more then 16 of any one color ball")
                        print("please retry ur input or type exit to quit and reset the tower ball placement")
                        current_tower = input("What ball is in the {0} slot of the {1} tower?".format(s, towers[i]))
                elif current_tower == 2:
                    if blue_counter < 16:
                        blue_counter += 1
                        break
                    else:
                        print("you are not allowed to have more then 16 of any one color ball")
                        print("please retry ur input or type exit to quit and reset the tower ball placement")
                        current_tower = input("What ball is in the {0} slot of the {1} tower?".format(s, towers[i]))
                if current_tower == "exit":
                    tower_init()
                    return
            print(current_tower)
            fts[i][counter] = int(current_tower)
            counter += 1
    count()


tower_init(1)
print_towers()
print_one_tower(4)
count()

# change_tower_scores()
