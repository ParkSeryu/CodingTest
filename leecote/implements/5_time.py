N = int(input())
h, m, s = 0, 0, 0
answer = 0

for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            sen = str(h) + str(m) + str(s)
            if '3' in sen:
                answer += 1

print(answer)

