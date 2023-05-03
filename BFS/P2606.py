from collections import deque

N = int(input())
M = int(input())
connectVirus = [list(map(int, input().split())) for _ in range(M)]
visit = list()

for i in range(1, N + 1):
    visit.append(i)


q = deque()
q.append(1)

def bfs():
    while q:
        key = q.popleft()
        for k in range(0, len(connectVirus)):
            if key == connectVirus[k][0]:
                q.append(connectVirus[k][1])
                connectVirus[k][0] = -1
                connectVirus[k][1] = -1
            elif key == connectVirus[k][1]:
                q.append(connectVirus[k][0])
                connectVirus[k][0] = -1
                connectVirus[k][1] = -1
        if key in visit:
            visit.remove(key)


bfs()
print(N - 1 - len(visit))


