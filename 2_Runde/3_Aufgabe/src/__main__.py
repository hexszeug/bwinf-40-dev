import argparse
from os import get_terminal_size
import solution
import way
import ssn_drawer

def num_list_to_hex(num):
    num = num[:]
    result = ""
    for digit in num:
        if digit < 10: result += str(digit)
        if digit == 10: result += "A"
        if digit == 11: result += "b"
        if digit == 12: result += "C"
        if digit == 13: result += "d"
        if digit == 14: result += "E"
        if digit == 15: result += "F"
    return result

#parse arguments
argparser = argparse.ArgumentParser()
argparser.add_argument("input_file", help="file path to input-file", type=str)
argparser.add_argument("-p", "-pc", "--print", "--print-to-console", help="print way to console", action="store_true", default=False)
argparser.add_argument("-pf", "--print-to-file", help="print way to given file", default=None)
args = argparser.parse_args()
input_file = args.input_file
output_file = args.print_to_file
print_way = args.print

#load input file
try:
    with open(input_file) as f:
        initial_num = [int(x, 16) for x in list(f.readline().replace("\n", ""))]
        max_moves = int(f.readline().replace("\n", ""))
except FileNotFoundError:
    print(f"Passed input file doesn't exist.")
    exit()

#create output file
if output_file != None:
    while True:
        try:
            with open(output_file, "x") as f: pass
            break
        except FileExistsError:
            new_output_file = input(f"Passed output file \"{output_file}\" already exists. To override it press enter. Otherwise type alternative filename: ")
            if new_output_file == "": break
            output_file = new_output_file
            del new_output_file

#print input
print(f"Input: {max_moves} moves, {len(initial_num)} digits, {num_list_to_hex(initial_num)}")

#caluclate solution
print(f"Calculating highest reachable number ({len(initial_num)} digits)...")
optimized_num, moves_used = solution.get_best_number(initial_num, max_moves)
print("Done!")

#print output
solution_str = "-" * get_terminal_size().columns + f"\nStart: {num_list_to_hex(initial_num)}\
    \n...{moves_used} steps ...\nEnd:   {num_list_to_hex(optimized_num)}\n" + "-" * get_terminal_size().columns
print(solution_str)

#calculate way
if output_file != None or print_way:
    print("Calculating way...")
    way_str = way.generate_way_ascii(initial_num, optimized_num, get_terminal_size().columns)
    print("Done!")

#print way to file
if output_file != None:
    with open(output_file, "w", encoding="utf-8") as f:
        print(f"Printing way to {output_file}...")
        f.write(f"{solution_str}\n{way_str}")
        print("Done!")

#print way to console
if print_way:
    rows = way_str.count("\n")
    if input(f"To print the whole way ({rows}rows) press enter. (Type c to cancel) ") == "":
        print(way_str)
