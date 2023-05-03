N = int(input())
P = list(map(int, input().split()))
tmp = 0
ans = 0

#print(N, P)

while len(P) > 0:
    tmp += min(P)
    ans += tmp
    print(tmp)
    P.remove(min(P))

print(ans)

