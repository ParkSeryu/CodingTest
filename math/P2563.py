cnt = int(input())
colorPaper = [[0] * 100 for _ in range(100)]
answer = 0

for i in range(cnt):
    i, j = map(int, input().split())
    for k in range(i, i + 10):
        for l in range(j, j + 10):
            colorPaper[k][l] = 1

for i in range(100):
    for j in range(100):
        if colorPaper[i][j] == 1:
            answer += 1

print(answer)
