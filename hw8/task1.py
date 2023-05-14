# Напишіть функцію sum_range(start, end) яка сумує всі цілі числа від значення start до end включно
# Якщо користувач введе перше число більше ніж друге то поміняти їх місцями


def sum_range(start, end):
    result = 0
    if start > end:
        start, end = end, start
    else:
        for i in range(start, end+1):
            result += i
    return result


# 1 + 2 + 3 + 4 + 5 -> 15
if __name__ == "__main__":
    print(sum_range(1, 5))