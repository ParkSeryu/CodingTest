N, B = input().split()
answer = 0
for i in range(len(N) - 1, -1, -1):
    if N[i].isdigit():
        answer += int(N[i]) * (int(B) ** (len(N) - 1 - i))
    else:
        answer += (ord(N[i - len(N)]) - 55) * (int(B) ** (len(N) - i - 1))

print(answer)
