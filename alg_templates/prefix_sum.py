"""
Prefix Sum (Префиксные суммы)
Условия: "Подмассив с суммой = K"
Задачи LeetCode: #560 (Subarray Sum Equals K), #974, #325
"""

prefix = {0: -1}
total = 0
for i, num in enumerate(arr):
    total += num
    if total - k in prefix:
        start = prefix[total - k]
        # подмассив: [start + 1, i]
    prefix[total] = i