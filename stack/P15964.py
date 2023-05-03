import sys
a = list()

for i in range(1, 29):
    a.append(int(sys.stdin.readline()))

for i in range(1, 31):
    if i not in a:
        print(i)

