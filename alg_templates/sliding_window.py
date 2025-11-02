"""
Это шаблон для подхода sliding window.
"Найти подмассив/подстроку с условием"

Задачи LeetCode:
#3, #76, #424, #1004, #209
"""

left = 0
result = ...
for right in range(len(arr)):
    # Добавляем arr[right]

    # Пока окно НЕВЕРНОЕ — сужаем слева
    while условие_не_выполнено:
        # Убираем arr[left]
        left += 1

    # Окно [left, right] — валидное
    # Обновляем ответ
    result = update(result, right - left + 1)
