N = int(input())
title = "666"
find_cnt = 1
i = 666

while N > find_cnt:
    i += 1
    if title in str(i):
        find_cnt += 1

print(i)

