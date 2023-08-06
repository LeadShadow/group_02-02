from calculations import salary_calculations
from datetime import datetime

salary = 1000
bonus = 15
salary_with_bonus = salary_calculations.add_bonus(salary, bonus)
print(salary_with_bonus)
# 2004.11.28 -> 18
# 2005.11.28 -> 17

first = datetime(year=2004, month=11, day=28)
second = datetime(year=2005, month=11, day=28)

print(datetime.now().year - first.year > datetime.now().year - second.year)
