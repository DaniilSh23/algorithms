"""
Binary Search (Бинарный поиск)
Условия: "Найти в отсортированном массиве"
Вариации:
    Поиск первого/последнего вхождения
    Поиск в повёрнутом массиве (#33, #153)
"""

left, right = 0, len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1