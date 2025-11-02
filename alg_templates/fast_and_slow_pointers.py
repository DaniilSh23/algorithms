"""
Fast & Slow Pointers (Черепаха и заяц)
Условия: "Цикл в связном списке", "середина", "k-й с конца"
Задачи LeetCode: #141 (Linked List Cycle), #142 (Cycle II), #876 (Middle), #19 (Remove Nth From End)
"""

slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow — середина