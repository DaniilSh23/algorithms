"""
LeetCode 167
"""
from typing import List

test_data = (
    # heights, expected_volume
    ([2,7,11,15], 9, [1,2]),
    ([2,3,4], 6, [1,3]),
    ([-1,0], -1, [1,2]),
)


def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    Используем метод двух указателей
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target: left += 1
        else: right -= 1
    return []


for i_arr, i_target, i_res in test_data:
    result = two_sum(i_arr, i_target)
    if result == i_res: print("ВЕРНО", i_arr, i_res, result)
    else: print("NOT ВЕРНО", i_arr, i_res, result)