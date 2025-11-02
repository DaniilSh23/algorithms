"""
LeetCode # 200 Number Of Islands. (BFS)
"""
from collections import deque
from typing import List

test_data = (
    # grid, islands numb
    (
        [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ],
        1,
    ),
    (
        [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ],
        3,
    ),
)


def numb_islands_bfs(grid: List[List[str]]) -> int:
    """
    Решение алгоритмом BFS
    """
    if not grid: return 0

    rows_numb, cols_numb = len(grid), len(grid[0])    # Определяем количество строк и колонок
    islands = 0     # Задаем переменную для подсчета результата
    queue = deque()     # Создаем очередь, в которую можно добавлять эл-ты как сначала, так и с конца

    for i_row_indx in range(rows_numb):
        for i_col_indx in range(cols_numb):

            # Проверяем на суше ли мы сейчас стоим
            if grid[i_row_indx][i_col_indx] == "1":
                islands += 1    # Если на суше, то добавляем остров к числу найденных
                queue.append((i_row_indx, i_col_indx))  # Закидываем в очередь координату, где мы наткнулись на остров

                # Затапливаем весь остров, чтобы больше на него не натыкаться, когда будем далее исследовать карту
                grid[i_row_indx][i_col_indx] = "0"  # Топим клетку, на которой сейчас стоим

                # Крутим цикл, пока в очереди есть элементы.
                # Это значит, что цикл будет крутиться, пока сверху, снизу, слева, справа есть суша.
                # Наша цель в этом цикле последовательно затупить всю сушу данного острова.
                # В этом же цикле мы будем пополнять очередь, если по соседству еще будет суша.
                # Таким образом получится, что цикл закончится тогда, когда мы затопим всю сушу найденного острова.
                while queue:
                    current_row, current_col = queue.popleft()

                    # Определяем соседние ячейки, которые могут быть сушей и их надо будет затапливать
                    neighbours = (
                        # Слева: строка текущая, для колонки исключаем выход левее карты, если выходим за пределы - это None
                        (current_row, current_col - 1 if current_col > 0 else None),
                        # Справа: строка текущая, для колонки исключаем выход правее карты, если выходим за пределы - это None
                        (current_row, current_col + 1 if current_col < cols_numb - 1 else None),
                        # Сверху: исключаем выход выше карты, или ставим None, строка текущая
                        (current_row - 1 if current_row > 0 else None, current_col),
                        # Снизу: исключаем выход ниже карты, или ставим None, строка текущая
                        (current_row + 1 if current_row < rows_numb - 1 else None, current_col),
                    )

                    # Обходим соседние ячейки с возможной сушей
                    for neighbour_row, neighbour_col in neighbours:

                        # Отдельным условием проверим, что сосед не выходит за пределы карты
                        if neighbour_row is None or neighbour_col is None: continue

                        # Окей, сейчас соседняя ячейка в пределах карты, но является ли она сушей?
                        if grid[neighbour_row][neighbour_col] == "1":
                            # Соседняя ячейка является сушей и ее надо затопить, сделаем же это!
                            grid[neighbour_row][neighbour_col] = "0"
                            # Добавим соседнюю ячейку в очередь, чтобы в будущей итерации цикла while проверить и ее
                            # соседей на предмет наличия суши
                            queue.append((neighbour_row, neighbour_col))

    return islands


def numb_islands_dfs(grid: List[List[str]]) -> int:
    """
    Решение методом DFS
    """
    if not grid: return 0

    rows_numb = len(grid)
    cols_numb = len(grid[0])
    islands = 0

    def flood_island(flood_row, flood_col):
        """
        Функция для затопления острова.
        Принимает на вход координаты, где была обнаружена суша и затапливает весь остров.
        Затопление острова происходит путем рекурсивного вызова функцией самой себя.
        :param flood_row: строка карты для затопления, на которой была обнаружена суша.
        :param flood_col: колонка карты для затопления, на которой была обнаружена суша.
        """
        grid[flood_row][flood_col] = "0"    # Затапливаем сушу

        # Определяем соседние ячейка
        neighbors = (
            # Слева: строка текущая, колонка не должна уйти левее карты
            (flood_row, flood_col - 1 if flood_col > 0 else None),
            # Правее: строка текущая, колонка не должна уйти правее карты
            (flood_row, flood_col + 1 if flood_col < cols_numb - 1 else None),
            # Выше: строка не должна уйти выше карты, колонка текущая
            (flood_row - 1 if flood_row > 0 else None, flood_col),
            # Ниже: строка не должна уйти ниже карты, колонка текущая
            (flood_row + 1 if flood_row < rows_numb - 1 else None, flood_col),
        )

        # Теперь обходим соседей
        for neighbor_row, neighbor_col in neighbors:
            # Проверим, что:
            if (
                    # ячейка в пределах карты
                    neighbor_row is not None and neighbor_col is not None
                    # и на ней суша
                    and grid[neighbor_row][neighbor_col] == "1"
            ):
                # Рекурсивно затапливаем сушу и внутри рекурсии проверим есть ли там тоже суша по соседству
                flood_island(flood_row=neighbor_row, flood_col=neighbor_col)

    # Обходим строки карты
    for i_row in range(rows_numb):
        # Обходим колонки на строке
        for i_col in range(cols_numb):
            # Если наткнулись на сушу
            if grid[i_row][i_col] == "1":
                # Добавляем найденный остров к общему числу островов
                islands += 1
                # Рекурсивно топим всю сушу найденного острова, начиная от данной ячейки, на которой мы нашли сушу
                flood_island(flood_row=i_row, flood_col=i_col)

    return islands


for i_grid, i_numb_islands in test_data:
    # result = numb_islands_bfs(i_grid)
    result = numb_islands_dfs(i_grid)
    if result == i_numb_islands: print("ВЕРНО", i_grid, i_numb_islands, result)
    else: print("NOT ВЕРНО", i_grid, i_numb_islands, result)