from alphabet import *

def load_parking():
    while True:
        file_name = input("Enter parking meta file path: ")
        try:
            file = open(file_name, "r", encoding="utf-8")
        except Exception as e:
            print("This file doesn't exist.")
            continue
        try:
            header = file.readline()
            header = header.split()
            size = i_(header[1]) + 1
            cars_count = int(file.readline().split()[0])
            cars = []
            for i in range(cars_count):
                line = file.readline()
                line = line.split()
                cars.append(int(line[1]))
            return size, cars
        except Exception as e:
            print(file_name, "is no parking meta file.")
