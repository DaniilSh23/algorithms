"""
LeetCode задача № 1
Two Sum
"""
from typing import List

test_data = (
    # nums, target, outpuaz
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1]),
    ([10, 20, 30, 40], 50, [0, 3])
)


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Решение задачи с помощью алгоритма двух указателей
    """
    seen = dict()
    for index, numb in enumerate(nums):
        complement = target - numb
        if complement in seen: return [seen[complement], index]
        seen[numb] = index
    return []

for i_nums, i_target, i_result in test_data:
    result = two_sum(i_nums, i_target)
    if result == i_result: print("ВЕРНО: ", i_nums, i_target, i_result, result)
    else: print("НЕВЕРНО: ", i_nums, i_target, i_result, result)