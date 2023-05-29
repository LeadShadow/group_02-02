# Мы разрабатываем кулинарный блог. И в рецептах, при написании списка ингредиентов, мы
# разделяем их запятыми, а перед последним ставим союз "and", как в примере ниже:
#
# 2 eggs, 1 liter sugar, 1 tsp salt and vinegar
# Напишите функцию format_ingredients, которая будет принимать на вход список из ингредиентов
# ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] и возвращать собранную строку из его
# элементов в описанный выше способ. Ваша функция должна уметь обрабатывать списки любой длины.
# ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] -> 'eggs, 1 liter sugar, 1 tsp salt and vinegar'

# ["2 eggs"] -> "2 eggs"

# join -> ', '.join(items)
# ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] -> "2 eggs, 1 liter sugar, 1 tsp salt, vinegar"
def format_ingredients(items: list) -> str:
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        # result = ''
        # for i in items[:-1]:
        #     result += i + ', '
        # return result[:-2] + ' and ' + items[-1]
        return ', '.join(items[:-1]) + ' and ' + items[-1]


print(format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]))

