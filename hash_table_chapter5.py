# Пример работы с хеш‑таблицами (в Python — словари).
# Демонстрация быстрого поиска O(1), проверки принадлежности и кэширования.
# Глава о хеш‑таблицах из книги «Грокаем алгоритмы».

seen = {}
words = ['apple', 'banana', 'apple', 'cherry', 'banana']

for word in words:
    if word in seen:
        print(f'{word} уже встречалось')
    else:
        seen[word] = True