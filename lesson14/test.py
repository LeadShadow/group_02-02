string1 = 'Hi there!'
string2 = "Hi\nthere!"
print(string2)
print(string1 == string2)


will = """Як умру, то поховайте
Мене на могилі
Серед степу широкого
На Вкраїні милій,
Щоб лани широкополі,
І Дніпро, і кручі
Було видно, було чути,
Як реве ревучий.
Як понесе з України
У синєє море
Кров ворожу... отойді я
І лани і гори —
Все покину, і полину
До самого Бога
Молитися... а до того
Я не знаю Бога.
Поховайте та вставайте,
Кайдани порвіте
І вражою злою кров’ю
Волю окропіте.
І мене в сем’ї великій,
В сем’ї вольній, новій,
Не забудьте пом’янути
Незлим тихим словом."""
print(will)

print('spam ' 'eggs' == 'spam eggs')

# \n - переведення рядка
# \f - переведення сторінки
# \r - повернення каретки
# \t - горизонтальна табуляція
print('\tHello')
# \v - вертикальна табуляція

s = 'Hi there!'
# er
start = 0
end = 7

print(s.find('er', start, end))
print(s.find('q'))

print(s.rfind('e', start, end))


# розбиття рядка на декілька підрядків
s = 'I am learning strings in Python. Some new methods got now'
sentences = s.split('. ')  # ['I am learning strings in Python', 'Some new methods got now']
print(sentences)
print(sentences[0])
print(sentences[1])

# ['I am learning strings in Python', 'Some new methods got now']

text = '. '.join(sentences)
print(text)

clean = '    spacious'.strip()
print(clean)

dogs_text = 'All dogs bark like dogs.'
cats_text = dogs_text.replace('dogs', 'cats')
print(cats_text)

# 380937316048
# +380937316048
# +38093(731)(60-48)
print('TestHook'.removeprefix('Test'))
print('TestHook'.removeprefix('Hook'))

print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))
