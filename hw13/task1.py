# Напишите функцию real_len, которая подсчитывает и возвращает длину строки без
# следующих управляющих символов: [\n, \f, \r, \t, \v]
#
# Для проверки правильности работы функции real_len ей будут переданы следующие строки:
#
# 'Alex\nKdfe23\t\f\v.\r'
# 'Al\nKdfe23\t\v.\r'
import re
def real_len(name: str):
    new_string = name.replace('\n', '').replace('\f', '').replace('\r', '').replace('\t', '').replace('\v', '')
    print(new_string)
    return len(new_string)


result1 = real_len('Alex\nKdfe23\t\f\v.\r')

def real_len(name: str):
    new_string = re.sub('\n|\f|\r|\t|\v', '', name)
    return len(new_string)


result2 = real_len('Alex\nKdfe23\t\f\v.\r')

print(result1 == result2)
