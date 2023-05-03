from queue import PriorityQueue
import sys

N = int(input())


prQue = PriorityQueue(maxsize=N)

for _ in range(N):
    i = int(sys.stdin.readline())
    if i == 0:
        if prQue.empty():
            print(0)
        else:
            print(-(prQue.get()))
    else:
        prQue.put(-i)




