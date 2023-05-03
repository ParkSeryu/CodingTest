str = input()
list = str.split(sep='-')

for i in range(len(list)):
    sum = 0
    split = list[i].split(sep='+')
    for j in split:
        sum += int(j)
    list[i] = sum

answer = int(list[0])

for i in range(1, len(list)):
    answer -= list[i]

print(answer)



