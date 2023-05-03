import itertools


def find_combinations(arr, r):
    return list(itertools.combinations(arr, r))


dwarf = []

for _ in range(9):
    dwarf.append(int(input()))

combinations = find_combinations(dwarf, 7)
temp = []

for index, combination in enumerate(combinations, 1):
    answer = 0
    for s in combination:
        answer += s
    if answer == 100:
        temp = combination
        break

#temp.sort()
ans = list(temp)
ans.sort()
for i in ans:
    print(i)