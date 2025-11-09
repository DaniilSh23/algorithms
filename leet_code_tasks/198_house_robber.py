"""
LeetCode #198 House Robber.
Решаем через DP (dynamic Programming)
"""
from typing import List

test_data = (
    # input, result
    ([1,2,3,1], 4),
    ([2,7,9,3,1], 12),
    ([10, 1, 0, 0, 0, 0, 9], 19),
    ([1, 10, 0, 0, 0, 9, 0], 19),
)


def rob(houses_money: List[int]) -> int:
    """
    Решение задачки по ограблению: выполняем с помощью динамического программирования.
    """
    houses_count = len(houses_money)
    if houses_count == 0: return 0  # Если домов нет, то нечего и грабить
    elif houses_count == 1: return houses_money[0]  # Если доступен всего один дом, то грабим только его и все

    # Создаем список, который будет соответствовать кол-ву домов. В данном списке будет храниться максимальная сумма
    # денег, которую можно украсть до данного дома, включая его. Короче, как будто мы идем слева направо по списку
    # домов, грабим их, если можем и в каждый дом складываем уже награбленное.
    max_lot_for_houses = [0] * houses_count

    # В первом доме можно украсть только его деньги
    max_lot_for_houses[0] = houses_money[0]

    # Второй дом: определяем, какой вариант ограбления даст больше денег. Берем максимальное значение из двух
    # вариантов: грабим первый дом, но тогда не грабим второй ведь они соседи, или грабим только сам второй дом,
    # но не грабим первый, они соседи.
    max_lot_for_houses[1] = max(houses_money[0], houses_money[1])

    # Для остальных домов выбираем лучший вариант на каждом шаге
    # Первый и второй дом мы уже рассчитали, в цикле идем от третьего дома и до конца
    for house_index in range(2, houses_count):
        max_lot_for_houses[house_index] = max(
            # Не грабим текущий дом
            max_lot_for_houses[house_index - 1],
            # Грабим текущий дом: берем деньги в нем и все награбленное до дома, который расположен через один назад
            max_lot_for_houses[house_index - 2] + houses_money[house_index]
        )

    return max_lot_for_houses[-1]  # Ответ — максимальная сумма к последнему дому


for i_arr, i_res in test_data:
    result = rob(i_arr)
    if result == i_res: print("ВЕРНО", i_arr, i_res, result)
    else: print("NOT ВЕРНО", i_arr, i_res, result)