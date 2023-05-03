from queue import PriorityQueue
import sys

N = int(input())
prQue = PriorityQueue(maxsize=N)

for _ in range(N):
    prQue.put(int(sys.stdin.readline()))

answer = 0

while prQue.qsize() > 1:
    sum = prQue.get() + prQue.get()
    prQue.put(sum)
    answer += sum

print(answer)


