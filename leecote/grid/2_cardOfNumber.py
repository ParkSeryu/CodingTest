N, M = map(int, input().split())
card = []
answer = 0

for i in range(N):
    card.append(list(map(int, input().split())))

for i in range(len(card)):
    if answer < min(card[i]):
        answer = min(card[i])

print(answer)
