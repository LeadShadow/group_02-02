from time import time
file = open('test_file.txt')
# щось записали в файл
file.close()

# 'r' -> відкриття на читання(є значенням за замовчуванням)
# 'w' -> відкриття на запис, зміст файла видаляється, якщо файла не існує створюється новий
# 'x' -> відкриття на запис, якщо файла не існує буде помилка
# 'a' -> відкриття на дозапис, інформація додається в кінець файла
# 'b' -> відкриття для двійкового формату
# 101010010101010101011010101101010110101011011010101011010
# 't' -> аналогічно до r
# '+' -> відкриття на читання і на запис  'w+'

# file = open('test.txt', 'w')
# symbols_written = file.write('hello!\n')
# file.write('hello!\n')
# file.write('hello!\n')
# file.write('hello!\n')
# file.write('hello!')
# print(symbols_written)
# file.close()


file = open('test.txt', 'r')
start = time()
print(file.read())
print(time() - start)

file = open('test.txt', 'r')
counter = 0
while True:
    counter += 1
    line = file.readline()
    if counter >= 5:
        break
    print(line, end='')