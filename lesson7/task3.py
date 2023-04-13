base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):
    global total_trip
    total_trip += 1
    sum = base_rate + price_per_km * path  # 40 + 10 * 5 -> 90
    return sum


print(trip_price(5))
print(total_trip)
print(trip_price(7))
print(total_trip)
print(trip_price(3))
print(total_trip)