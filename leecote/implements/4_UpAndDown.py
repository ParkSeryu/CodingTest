N = int(input())
plans = list(input().split())
x, y = 1, 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cases = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(cases)):
        if plan == cases[i]:
            if 1 < x + dx[i] < N:
                x += dx[i]
            if 1 < y + dy[i] < N:
                y += dy[i]

print(y, x)