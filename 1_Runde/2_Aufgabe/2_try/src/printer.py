def getWayDisplay(way, hotel_distances, hotel_ratings):
    res = ""
    for i in range(len(way) - 1):
        start = hotel_distances[way[i]]
        end = hotel_distances[way[i + 1]]
        res += getHotelDisplay(way[i], hotel_distances, hotel_ratings) + " --" + str(end - start) + "-- "
    return res + getHotelDisplay(len(hotel_distances) - 1, hotel_distances, hotel_ratings)

def getHotelDisplay(hotelID, hotel_distances, hotel_ratings):
    between = str(hotelID) + ":" + str(hotel_distances[hotelID]) + "(" + str(hotel_ratings[hotelID]) + ")"
    if hotel_distances[hotelID] == 0:
        between = "S"
    if hotel_distances[hotelID] == hotel_distances[len(hotel_distances) - 1]:
        between = "E"
    return "|" + between + "|"