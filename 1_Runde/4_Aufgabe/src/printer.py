def create_file(output_file_name="0.txt"):
    f = open(output_file_name, 'w')
    f.write("")
    f.close()

def print_to_file(output_file_name, frame):
    f = open(output_file_name, 'a')
    f.write(frame)
    f.close()

def generate_frame(pos_a, pos_b, dice_top, p, field_size=40):
    ###Capital letters for the moved one
    A = "A"
    B = "b"
    if p:
        A = "a"
        B = "B"
    ###GENERATE FRAME
    frame = ""
    ###Show top side of dice and player on move
    frame += "+++++  *****\n"
    frame += "+ "
    if p:
        frame += B
    else:
        frame += A
    frame += " +  * " + str(dice_top) + " *\n"
    frame += "+++++  *****\n\n"
    ###Show a pieces on -1
    for i in pos_a:
        if i == -1:
            frame += A
    frame += "\n"
    ###Show a pices on goal fields
    frame += "a  b  c  d\n"
    for i in range(field_size, field_size + 4):
        add = " "
        if i in pos_a:
            add = A
            frame += add + "  "
    frame += "\n"
    ###Show normal field with pieces
    between_fields = ""
    upper_fields = ""
    lower_fields = ""
    for i in range(int(field_size / 2)):
        between_fields += "#####  "
        add_upper = " "
        add_lower = " "
        if i in pos_a:
            add_upper = A
        if i in pos_b:
            add_upper = B
        if (field_size - 1) - i in pos_a:
            add_lower = A
        if (field_size - 1) - i in pos_b:
            add_lower = B
        upper_fields += "# " + add_upper + " #  "
        lower_fields += "# " + add_lower + " #  "
    frame += between_fields + "\n" + upper_fields + "\n" + between_fields + "\n" + lower_fields + "\n" + between_fields + "\n"
    ###Show b pieces on goal field
    frame += "\na  b  c  d\n"
    for i in range(field_size, field_size + 4):
        add = " "
        if i in pos_b:
            add = B
            frame += add + "  "
    ###Show b pieces on -1
    frame += "\n"
    for i in pos_b:
        if i == -1:
            frame += B
    ###End
    frame += "\n\n------------\n"
    return frame

def print_table(keys, values):
    max_len_keys = 0
    for i in keys:

        if len(str(i)) > max_len_keys:
            max_len_keys = len(str(i))
    max_len_values = 0
    for i in values:
        if len(str(i)) > max_len_values:
            max_len_values = len(str(i))
    for i in range(len(keys)):
        len_key = len(str(keys[i]))
        len_value = len(str(values[i]))
        print("{}{}  {}{}".format(keys[i], " " * (max_len_keys - len_key), " " * (max_len_values - len_value), values[i]))

def print_results(dice_a, dice_b, wins_a, wins_b, ties):
    print_table([dice_a, dice_b, "game timeout / tie"], [wins_a, wins_b, ties])

def print_simulation_start(dice_a, dice_b, game, total_games, total_simulations):
    print("\n\nSimulating game {}/{} {} times ({} vs. {})".format(game, total_games, total_simulations, dice_a, dice_b))
