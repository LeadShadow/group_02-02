# Как мы уже знаем, ключ в словаре должен быть уникальным, а вот значение его нет. Реализуйте
# функцию lookup_key для поиска всех ключей по значению в словаре. Первым параметром в функцию
# мы передаем словарь, а вторым — значение, которое хотим найти. Таким образом результат
# может быть как список ключей, так и пустой список, если мы ничего не найдем.

# dict = {'one': 1, 'two': 2}
# for i in dict:
# for i in dict.keys()
# if dict[i] -> 1, 2
def lookup_key(data: dict, value) -> list:
    result = []
    for key in data:
        if data[key] == value:
            result.append(key)
    return result


if __name__ == "__main__":
    print(lookup_key({'one': 1, 'two': 2, 'three': 2}, 2))

# ['two', 'three']