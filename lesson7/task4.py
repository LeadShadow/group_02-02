price = int(input('Input price of good: '))
user_input = input('Input discount: ') # '30'



# len(str) -> 'Sasha' -> 5
def apply_discount(discount): # '9' -> 0.09
    if len(discount) == 1:
        # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        discount = '0.0' + discount[0]
    elif len(discount) == 2:
        discount = '0.' + discount[0] + discount[1]
    else:
        discount = 1
    return float(discount)


def calculate_price(price, discount):
    result = price * (1 - discount)
    return result
# discount[0] -> discount = 'word', print(discount[0]) -> 'w'
# 50% -> 1000 -> 500
# 34% -> 1250 -> 825
# 34% -> 0.34
discount = apply_discount(user_input)
print(calculate_price(price, discount))