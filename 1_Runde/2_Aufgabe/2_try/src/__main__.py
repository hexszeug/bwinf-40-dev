import reader
import printer

import easteregg

DISTANCEPERDAY = 6 * 60
DAYS = 5
BEST = None
TOTALDISTANCE = None

hotel_distances = None
hotel_ratings = None
hotel_ids = None

def getOneWay():
    way = [0]
    hotelID = 0
    for day in range(DAYS):
        find = hotel_distances[hotelID] + DISTANCEPERDAY
        end = len(hotel_distances) - 1
        while hotelID <= end and hotel_distances[hotelID] <= find:
            hotelID += 1
        hotelID -= 1
        way.append(hotelID)
        if hotelID == end:
            return way
    return None

BEST, TOTALDISTANCE, hotel_distances, hotel_ratings = reader.readHotels()

hotel_distances.insert(0, 0)
hotel_ratings.insert(0, BEST + 1.0)
hotel_distances.append(TOTALDISTANCE)
hotel_ratings.append(BEST + 1.0)

hotel_distances_backup = hotel_distances[:]
hotel_ratings_backup = hotel_ratings[:]
hotel_ids = list(range(len(hotel_distances)))

removed_position = None
removed_distance = None
removed_valuation = None
removed_id = None

while getOneWay() != None:
    removed_position = hotel_ratings.index(min(hotel_ratings))
    removed_distance = hotel_distances.pop(removed_position)
    removed_valuation = hotel_ratings.pop(removed_position)
    removed_id = hotel_ids.pop(removed_position)

if removed_position != None:
    hotel_distances.insert(removed_position, removed_distance)
    hotel_ratings.insert(removed_position, removed_valuation)
    hotel_ids.insert(removed_position, removed_id)

    bestWay = []

    for hotelID in getOneWay():
        bestWay.append(hotel_ids[hotelID])

    print(printer.getWayDisplay(bestWay, hotel_distances_backup, hotel_ratings_backup))
else:
    print("Its not possible to reach the destination with driving only {} minutes on {} days and sleeping at the given hotels.".format(DISTANCEPERDAY, DAYS))