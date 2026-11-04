# Пример из книги «Грокаем алгоритмы» по рекурсии и стеку вызовов (факториал).

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
print(fact(int(input())))