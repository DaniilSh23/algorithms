"""
LeetCode #1091. Shortest Path in Binary Matrix
"""
from typing import List
from collections import deque


test_data = (
    # grid, expected_result
    (
        [
            [0,1],
            [1,0],
        ],
        2,
    ),
    (
        [
            [0,0,0],
            [1,1,0],
            [1,1,0],
        ],
        4,
    ),
    (
        [
            [1,0,0],
            [1,1,0],
            [1,1,0],
        ],
        -1,
    ),
)

def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
    """
    Решение с помощью алгоритма поиска в ширину BFS.
    Наша задача найти путь из левого верхнего угла к правому нижнему. Ходить мы можем только по клеткам, отмеченным 0,
    клетки отмеченные 1 - это препятствия.
    Если пути нет, то мы должны вернуть -1, а если путь есть, то вернуть кол-во шагов до целевой клетки.
    Клетка, на которой стоим на старте, тоже считается, как +1 к шагам.
    """
    # Сразу проверяем крайний случай, когда клетка, с которой стартуем, является препятствием.
    if grid[0][0] == 1: return -1

    # Определяем переменные для хранения размеров сетки, итогового количества шагов, флаг финиша и очередь
    rows_numb, cols_numb = len(grid), len(grid[0])
    steps = 0
    queue = deque()

    # В очередь сразу кладем клетку, с которой стартуем.
    queue.append((0, 0))
    # Затем начинаем крутить цикл до тех пор, пока в очереди есть клетки, по которым можно ходить.
    while queue:
        steps += 1  # Увеличиваем кол-во шагов

        # Выполняем столько итерации, сколько сейчас у нас есть доступных клеток для передвижения
        for _ in range(len(queue)):

            # Достаем из очереди точку, от которой будем искать клетки для передвижения
            current_row, current_col = queue.popleft()

            # Помечаем текущую клетку, как препятствие, чтобы по-новой ее не посещать
            grid[current_row][current_col] = 1

            # Проверка не добрались ли мы до пункта назначения (текущие координаты равны координатам целевой клетки)
            if current_row == rows_numb - 1 and current_col == cols_numb - 1:
                # Возвращаем результат из функции (кол-во шагов до цели)
                return steps

            # Ищем соседние клетки, на которые можно передвигаться
            neighbors = (
                # Влево: строка текущая, колонка не должна уйти левее карты
                (current_row, current_col - 1 if current_col > 0 else None),
                # Влево-вверх(по диагонали): строка не должна уйти выше карты, колонка не должна уйти левее карты
                (current_row - 1 if current_row > 0 else None, current_col - 1 if current_col > 0 else None),
                # Влево-вниз(по диагонали): строка не должна уйти ниже карты, колонка не должна уйти левее карты
                (current_row + 1 if current_row < rows_numb - 1 else None, current_col - 1 if current_col > 0 else None),
                # Вправо: строка текущая, колонка не должна уйти правее карты
                (current_row, current_col + 1 if current_col < cols_numb - 1 else None),
                # Вправо-вверх(по диагонали): строка не должна уйти выше карты, колонка не должна уйти правее карты
                (current_row - 1 if current_row > 0 else None, current_col + 1 if current_col < cols_numb - 1 else None),
                # Вправо-вниз(по диагонали): строка не должна уйти ниже карты, колонка не должна уйти правее карты
                (current_row + 1 if current_row < rows_numb - 1 else None, current_col + 1 if current_col < cols_numb - 1 else None),
                # Вверх: строка не должна уйти выше карты, колонка текущая
                (current_row - 1 if current_row > 0 else None, current_col),
                # Вниз: строка не должна уйти ниже карты, колонка текущая
                (current_row + 1 if current_row < rows_numb - 1 else None, current_col),
            )

            # Итерируемся по соседним клеткам, чтобы проверить их на возможность передвижения
            for neighbor_row, neighbor_col in neighbors:
                # Если соседняя клетка не является препятствием и по ней можно двигаться
                if (
                    # Координаты данной клетки не вышли за пределы карты
                    neighbor_row is not None and neighbor_col is not None
                    # Клетка не является препятствием
                    and grid[neighbor_row][neighbor_col] == 0
                ):
                    # Добавляем ее в очередь для проверки на следующем шаге (итерации основного цикла while)
                    queue.append((neighbor_row, neighbor_col))

    # Если в цикле не дошли до целевой точки и, соответственно не вернули из функции результат, то значит пути к цели нет
    return -1


for i_grid, i_result in test_data:
    input(i_grid)
    result = shortest_path_binary_matrix(i_grid)
    if result == i_result: print("ВЕРНО", i_grid, i_result, result)
    else: print("NOT ВЕРНО", i_grid, i_result, result)
