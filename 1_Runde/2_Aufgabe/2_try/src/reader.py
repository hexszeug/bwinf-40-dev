def readHotels():
    count = None
    distance = None
    hotel_distances = []
    hotel_ratings = []
    best = None
    baddest = None
    while True:
        file_name = input("Please enter hotel meta file path: ")
        try:
            with open(file_name, "r") as f:
                count = int(f.readline())
                distance = float(f.readline())
                for i in range(count):
                    line = f.readline().split(" ")
                    hotel_distances.append(float(line[0]))
                    hotel_ratings.append(float(line[1]))
                best = max(hotel_ratings)
                return best, distance, hotel_distances, hotel_ratings
        except:
            print(file_name, "doesn't exist or is no hotel meta file.")