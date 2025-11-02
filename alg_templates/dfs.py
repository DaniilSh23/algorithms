"""
DFS (Поиск в глубину)
Условия: "Все пути", "связные компоненты"
Задачи LeetCode: #46 (Permutations), #78 (Subsets), #79 (Word Search)
"""

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor)


# Или с возвратом (backtracking):
def backtrack(path):
    if len(path) == target:
        result.append(path[:])
        return
    for choice in candidates:
        path.append(choice)
        backtrack(path)
        path.pop()