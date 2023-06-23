N = int(input())
su = list()
for _ in range(N):
    su.append(int(input()))

su.sort(reverse=True)

for i in su:
    print(i, end= ' ')