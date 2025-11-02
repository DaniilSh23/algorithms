"""
Heap (Куча)
Условия: "Топ-K", "приоритет"
Задачи LeetCode: #215 (Kth Largest), #347 (Top K Frequent), #295 (Median Stream)
"""

import heapq
heap = []
for num in arr:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)
# heap[0] — k-й наибольший
# Или min-heap для max:
heapq.heappush(heap, -num)
