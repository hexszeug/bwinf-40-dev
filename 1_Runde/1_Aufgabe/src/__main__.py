from alphabet import *
import reader

size = None
cars = None
spots = None

def push_car(car, move, dir):
    spot = cars[car]
    if move > [spots[spot:], spots[:spot]][dir].count(None):
        return None
    can = 0
    for i in range(1, move + 1):
        if (dir and spots[spot - i] == None) or (not dir and spots[spot + i + 1] == None):
            can += 1
        else:
            break
    push = move - can
    res_cars = []
    res_moves = []
    if push > 0:
        res_cars, res_moves = push_car(car + dir * -2 + 1, push, dir)
    res_cars.append(car)
    res_moves.append(move)
    return res_cars, res_moves


size, cars = reader.load_parking()

line_spots = ""
line_cars = ""

spots = [None] * size
for i in range(size):
    line_spots += c_(i) + " "
    if i in cars:
        spots[i] = spots[i+1] = cars.index(i)
        line_cars += c_(spots[i] + size) + "-" + c_(spots[i+1] + size) + " "
    elif i - 1 not in cars:
        line_cars += "  "

print("\n" + line_spots + "\n" + line_cars + "\n")

result = ""

for spot in range(size):
    result += "{}: ".format(c_(spot))
    car = spots[spot]
    if car != None:
        offset = cars[car] != spot #False: left side of car is blocking the spot; True: right side of the car is blocking the spot
        solution = [None] * 2
        solution[0] = push_car(car, 1 + (not offset), True) #calculate solution to left
        solution[1] = push_car(car, 1 + offset, False) #calculate solution to right
        better = None
        if solution[0] == None or solution[1] == None:
            better = solution[0] == None
        elif len(solution[0][0]) == len(solution[1][0]):
            better = sum(solution[0][1]) > sum(solution[1][1])
        else:
            better = len(solution[0][0]) > len(solution[1][0])
        if solution[better] != None:
            for i in range(len(solution[better][0])):
                if i > 0:
                    result += ", "
                result += "{} {} {}".format(c_(solution[better][0][i] + size), solution[better][1][i], d_(better))
        else:
            result += "impossible"
    result += "\n"
print(result)
