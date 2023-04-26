def dfs(matrix, visited, i, j):
    if i < 0 or i >= 5 or j < 0 or j >= 5:
        return False
    
    if matrix[i][j] == 1 or visited[i][j]:
        return False
    
    visited[i][j] = True
    
    if i == 4 and j == 4:
        return True
    
    return dfs(matrix, visited, i+1, j) or dfs(matrix, visited, i-1, j) or dfs(matrix, visited, i, j+1) or dfs(matrix, visited, i, j-1)


def solve(matrix):
    visited = [[False for _ in range(5)] for _ in range(5)]
    
    if dfs(matrix, visited, 0, 0):
        return "COPS"
    else:
        return "ROBBERS"


t = int(input())

for _ in range(t):
    matrix = []
    for _ in range(5):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    print(solve(matrix))
