from random import randrange
import printer

field_size = 40 #count of fields every player can go on
max_moves_per_game = 4096 #max moves after which the game gets cancelled

def roll(dice):
    return dice[randrange(0, len(dice))]

def opp_view(pos, turning_point=(field_size / 2)):
    res = -1
    if pos == -1 or pos >= turning_point * 2:
        res == pos
    elif pos < turning_point:
        res = pos + turning_point
    elif pos >= turning_point:
        res = pos - turning_point
    return res

def run(dice_a, dice_b, frame_display=False, frame_output=False, id='0'):
    ###Prepare output file
    output_file_name = id + ".txt" #generate frame output file name
    if frame_output:
        printer.create_file(output_file_name)
    ###Prepare game
    pos = [[0, -1, -1, -1], [0, -1, -1, -1]]
    d = [dice_a, dice_b]
    p = None
    ###Roll out starting player
    while p == None:
        a = roll(d[0])
        b = roll(d[1])
        if a != b:
            p = a < b
    ###GAME LOOP
    for move_index in range(max_moves_per_game):
        pos[p].sort() #sort pieces
        dice_top = roll(d[p]) #roll dice
        ###Precalculate move
        piece = None
        move_to = None
        if dice_top == 6 and -1 in pos[p] and 0 not in pos[p]: #rolled a 6, piece on -1 and no piece on 0 -> get piece away from -1
            piece = pos[p].index(-1)
            move_to = 0
        else:
            for i in pos[p]: #select first piece which can move
                if i + dice_top not in pos[p] and i + dice_top < field_size + 4 and i != -1:
                    piece = pos[p].index(i)
                    move_to = i + dice_top
                    if i == 0 and -1 in pos[p]:
                        break
        ###Execute precalculated move
        if piece != None: #test if move can be made
            pos[p][piece] = move_to #actual move
            if opp_view(move_to) in pos[not p] and move_to < field_size: #moved to a field the opponent stands on -> capture its piece
                pos[not p][pos[not p].index(opp_view(move_to))] = -1 #capture opponents piece
        ###Print frame
        if frame_output or frame_display:
            pos_a = pos[0][:]
            pos_b = pos[1][:]
            for i in range(len(pos_b)):
                pos_b[i] = opp_view(pos_b[i])
            frame = printer.generate_frame(pos_a, pos_b, dice_top, p, field_size)
            if frame_output:
                printer.print_to_file(output_file_name, frame)
            if frame_display:
                print(frame)
        ###Win detection
        if min(pos[p]) >= field_size:
            return int(p)
        ###Select other player
        if dice_top != 6:
            p = not p
    return -1

if __name__ == '__main__':
    print(run([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], False, True))
