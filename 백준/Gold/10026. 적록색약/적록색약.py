from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

encoded_graph = [[0 for _ in range(n)] for _ in range(n)]
encoded_graph_color = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            encoded_graph[i][j] = 1
            encoded_graph_color[i][j] = 1
        elif graph[i][j] == 'G':
            encoded_graph[i][j] = 2
            encoded_graph_color[i][j] = 1
        else:  # 'B'
            encoded_graph[i][j] = 3
            encoded_graph_color[i][j] = 2

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(matrix, x, y):
    queue = deque()
    queue.append((x, y))
    color = matrix[x][y]
    matrix[x][y] = 0  

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == color:
                matrix[nx][ny] = 0  
                queue.append((nx, ny))

def count_areas(matrix):
    count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                bfs(matrix, i, j)
                count += 1
    return count

normal_count = count_areas([row[:] for row in encoded_graph])

color_blind_count = count_areas([row[:] for row in encoded_graph_color])

print(normal_count, color_blind_count)