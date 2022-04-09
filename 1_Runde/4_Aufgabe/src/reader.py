def load_dices():
    """Questions dice meta file path, reads it and returns its content as a list."""

    dice_count = 0
    dices = []

    while True:
        file_name = input("Enter dice meta file path: ")
        #open file
        try:
            file = open(file_name, 'r', encoding='utf8')
        except Exception as e:
            print(file_name, "doesn't exist. Please enter an existing file path.")
            continue
        #decode file
        print("Decoding", file_name + "...")
        try:
            i = 0
            for line in file:
                if i == 0:
                    dice_count = int(line)
                elif i > dice_count:
                    break
                else:
                    side_count = 0
                    dice = []
                    j = 0
                    for side in line.split():
                        if j == 0:
                            side_count = int(side)
                        elif j > side_count:
                            break
                        else:
                            dice.append(int(side))
                        j += 1
                    dices.append(dice)
                i += 1
        except Exception as e:
            print(file_name, "is not in the dice meta format. Please enter a path to a dice meta file.")
            continue
        #close file
        file.close()
        print("Sucessfully loaded {} dices from {}:".format(dice_count, file_name))
        for dice in dices:
            print(dice)
        return dices
