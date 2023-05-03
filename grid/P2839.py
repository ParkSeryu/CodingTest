N = int(input())
cnt = -1

if N // 5 < 1:
    if N % 3 == 0:
        cnt = N // 3
    else:
        cnt = -1
else:
    for i in range(N // 5, 0, -1):
        if N - (5 * i) == 0:
            cnt = i
            break
        elif (N - (5 * i)) % 3 == 0:
            cnt = i + ((N - 5 * i) // 3)
            break
        elif N % 3 == 0:
            cnt = N // 3
print(cnt)
