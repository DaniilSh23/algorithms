"""
DP (Динамическое программирование)
Условия: "Оптимизация с перекрывающимися подзадачами"
Задачи LeetCode: #70 (Climbing Stairs), #198 (House Robber), #62 (Unique Paths), #1143 (LCS)
"""

# 1D DP
dp = [0] * len(arr)
for i in range(1, len(arr)):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])  # House Robber


# 2D DP
dp = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # Unique Paths