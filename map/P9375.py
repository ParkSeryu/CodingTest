N = int(input())

for i in range(N):
    cnt = int(input())
    dict = {}
    ans = 1
    for j in range(cnt):
        value, key = input().split()
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    for value in dict.values():
        ans = ans * (value + 1)
    ans -= 1
    print(ans)




