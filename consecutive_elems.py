

ARRAY = (-3, -2, -1, 0, 0, 2, 3, 5, 6, 7, 7, 7)

def find_consecutive_elements(arr):
    """
    Поиск максимального числа последовательно идущих символов в массиве
    """
    winner = ("", 0)    # (эл-т, кол-во)
    count = 0
    elem = None
    for i_elem in arr:

        # Первая итерация, когда элемента еще нет
        if elem is None:
            elem = i_elem
            count += 1
            continue

        # Последующие итерации: если элемент изменился
        if i_elem != elem:

            # Устанавливаем нового победителя
            winner = (str(elem), count) if winner[1] < count else winner

            elem = i_elem   # Меняем элемент
            count = 1   # Устанавливаем в начало счетчик
            continue

        count += 1  # Инкремент счетчика, если элемент не поменялся

    # Определяем нового победителя и возвращаем из функции
    return (str(elem), count) if winner[1] < count else winner

print(find_consecutive_elements(arr=ARRAY))


