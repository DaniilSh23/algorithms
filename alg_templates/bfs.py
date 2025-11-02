"""
BFS (Поиск в ширину)
Условия: "Кратчайший путь в графе/сетке"
Задачи LeetCode: #1091 (Shortest Path in Binary Matrix), #994 (Rotting Oranges), #200 (Islands)
"""

from collections import deque
q = deque([(start, 0)])  # (позиция, шаг)
visited = {start}

while q:
    pos, dist = q.popleft()
    if pos == target:
        return dist
    for next_pos in neighbors(pos):
        if next_pos not in visited:
            visited.add(next_pos)
            q.append((next_pos, dist + 1))

"""
Хз насколько верно иллюстрирует подход код выше, его сгенерила нейронка
"""