from collections import deque
import sys

input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue = deque([(a, b)])
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

paint_count = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            paint_count += 1
            max_size = max(max_size, bfs(i, j))

print(paint_count)
print(max_size)