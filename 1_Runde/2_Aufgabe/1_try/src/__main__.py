import reader
import printer

DISTANCEPERDAY = 6 * 60
DAYS = 5
BADDEST = 0.0
BEST = 5.0

distance = 0
hotel_distances = []
hotel_valuations = []

possibles = []

def getShortest(hotelID, leftDays):
    min = distance - leftDays * DISTANCEPERDAY
    i = hotelID + 1
    while i < len(hotel_distances) and hotel_distances[i] < min:
        i += 1
    return i

def getFarest(hotelID):
    max = hotel_distances[hotelID] + DISTANCEPERDAY
    i = hotelID + 1
    while i < len(hotel_distances) and hotel_distances[i] <= max:
        i += 1
    return i - 1

def calcPossibles(hotelID, leftDays, hotelsBefore):
    hotelsNow = hotelsBefore[:]
    hotelsNow.append(hotelID)
    if hotel_distances[hotelID] == distance:
        possibles.append(hotelsNow)
        return
    first = getShortest(hotelID, leftDays)
    last = getFarest(hotelID)
    # print(leftDays, hotelID, first, last)
    for i in range(first, last + 1):
        calcPossibles(i, leftDays - 1, hotelsNow)

distance, hotel_distances, hotel_valuations = reader.readHotels()

hotel_distances.insert(0, 0.0)
hotel_valuations.insert(0, BEST)
hotel_distances.append(distance)
hotel_valuations.append(BEST)

calcPossibles(0, DAYS, [])

baddest = BADDEST
bestWay = None

for way in possibles:
    for i in way:
        if hotel_valuations[i] > baddest:
            baddest = hotel_valuations[i]
            bestWay = way[:]
    # print(getWayDisplay(way))
print(printer.getWayDisplay(bestWay, hotel_distances, hotel_valuations))