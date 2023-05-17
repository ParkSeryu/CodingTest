T = int(input())

dp = [0] * 15
for i in range(1, 15):
    dp[i] = i

for i in range(T):
    k = int(input())
    n = int(input())
    for floor in range(k):
        temp = 0
        for j in range(1, n + 1):
            temp += dp[j]
            dp[j] = temp
    print(dp)
