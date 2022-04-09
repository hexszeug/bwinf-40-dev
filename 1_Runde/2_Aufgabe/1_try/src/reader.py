def readHotels():
    count = 0
    distance = 0
    hotel_distances = []
    hotel_valuations = []
    while True:
        file_name = input("Please enter hotel meta file path: ")
        try:
            with open(file_name, "r") as f:
                count = int(f.readline())
                distance = float(f.readline())
                for i in range(count):
                    line = f.readline().split(" ")
                    hotel_distances.append(float(line[0]))
                    hotel_valuations.append(float(line[1]))
                return distance, hotel_distances, hotel_valuations
        except:
            print(file_name, "doesn't exist or is no hotel meta file.")