import sys

N, M = map(int, input().split())
iceMaker = list()
for i in range(N):
    iceMaker.append(list(map(int, sys.stdin.readline().rstrip())))


def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    if iceMaker[x][y] == 0:
        iceMaker[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1
print(result)
