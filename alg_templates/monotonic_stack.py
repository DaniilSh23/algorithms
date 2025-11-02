"""
Monotonic Stack (Монотонный стек)
Условия: "Ближайший больший/меньший"
Задачи LeetCode: #739 (Daily Temperatures), #496 (Next Greater), #42 (Trapping Rain Water)
"""

stack = []
for i, num in enumerate(arr):
    while stack and arr[stack[-1]] < num:
        idx = stack.pop()
        # arr[idx] — ближайший меньший слева
    stack.append(i)