# зробити задачу, якщо а буде лежати в проміжку між числами 10 і 50, то вивести на екран
# (а належить проміжку (10, 50), якщо а не лежить в межах
# від 10 до 50, то вивести на екран (а не належить проміжку(10, 50))
a = int(input("Enter a number: "))

if 10 <= a <= 50:
    print(a, 'знаходиться між 10 - 50')
else:
    print(a, 'не знаходиться між 10 - 50')
