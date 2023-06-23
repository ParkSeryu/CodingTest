N = int(input())
score = dict()

for i in range(N):
    a, b = input().split()
    score[a] = b

score = sorted(score.items())
print(score)

for i in score:
    print(i[0], end=' ')
