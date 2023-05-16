N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
cnt = 0
i = 0
arr.sort(reverse=True)

while i < M:
    cnt += 1
    if cnt > K:
        answer += arr[1]
        cnt = 0
    else:
        answer += arr[0]
    i += 1
print(answer)

##2. 큰수의 법칙 공식
arr.sort()
first = arr[N - 1]
second = arr[N - 2]

count = int(M / (K + 1)) * K
count += M % (K + 1)

result = 0
result += count * first
result += (M - count) * second

print(result)
