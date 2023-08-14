from datetime import datetime, timedelta

first_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
first_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = first_day_2020 - first_day_2019
print(difference)  # timedelta
print(difference.total_seconds() / 60 / 60 / 24)

four_week_interval = timedelta(weeks=4)
print(first_day_2020 + four_week_interval)

delta = timedelta(
    days=50,
    seconds=27,
    milliseconds=4932492,
    microseconds=10,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)

ts = first_day_2020.timestamp()
print((ts / 60 / 60 / 24 / 30 - 8.5) / 12)
print(type(first_day_2020))
print(type(first_day_2020.strftime('%A %d %B %Y')))

s = input('Input date: ')  # 10 January 2020
print(type(datetime.strptime(s, '%d %B %Y').date()))
