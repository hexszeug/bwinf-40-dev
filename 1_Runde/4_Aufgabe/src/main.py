import reader
import game
import pgbar
import printer
from multiprocessing.pool import Pool
from sys import argv

simulations_per_dice_pair = 1000000

def game_thread(arg):
    index = arg[0]
    dice_a = arg[1]
    dice_b = arg[2]
    id = arg[3]
    result = None
    a_can_win = 6 in dice_a
    b_can_win = 6 in dice_b
    if a_can_win and not b_can_win:
        result = 0
    if b_can_win and not a_can_win:
        result = 1
    if not a_can_win and not b_can_win:
        result = -1
    if result == None:
        frame_output = (index % (simulations_per_dice_pair / 10)) == 0
        result = game.run(dice_a, dice_b, id=id, frame_output=frame_output)
    return result

# def simulate_games(a, b, dices):
#     results = []
#     for i in range(simulations_per_dice_pair):
#         results.append(game_thread(i, dices[a], dices[b], "{}vs{}_{}".format(a, b, i)))
#     return results

def simulate_games(a, b, dices):
    results = []
    iterable = []
    for i in range(simulations_per_dice_pair):
        iterable.append((i, dices[a], dices[b], "{}vs{}_{}".format(a, b, i)))
    pool = Pool()
    tasks = pool.imap_unordered(game_thread, iterable, chunksize=int(simulations_per_dice_pair / 1000))
    pool.close()
    pgbar.setup(simulations_per_dice_pair)
    for i, _ in enumerate(tasks, 1):
        pgbar.update(i)
        results.append(_)
    return results

def run():
    global simulations_per_dice_pair
    if len(argv) > 1:
        try:
            simulations_per_dice_pair = int(argv[1])
            if(simulations_per_dice_pair < 1000):
                simulations_per_dice_pair = 1000
            print("Running with different simulation count:", simulations_per_dice_pair)
        except Exception as e:
            pass
    dices = reader.load_dices()
    games = []
    for i in range(len(dices)):
        for j in range(len(dices)):
            if i < j:
                games.append((i, j))
    for i in games:
        a = i[0]
        b = i[1]
        dice_a = dices[a]
        dice_b = dices[b]
        printer.print_simulation_start(dice_a, dice_b, games.index(i) + 1, len(games), simulations_per_dice_pair)
        results = simulate_games(a, b, dices)
        wins_a = results.count(0)
        wins_b = results.count(1)
        ties = results.count(-1)
        printer.print_results(dice_a, dice_b, wins_a, wins_b, ties)
