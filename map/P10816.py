N = int(input())
card = list(map(int, input().split()))
M = int(input())
findCard = list(map(int, input().split()))
dic = dict()
answer = list()

for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in findCard:
    if i in dic:
        answer.append(dic[i])
    else:
        answer.append(0)

for i in answer:
    print(i, end=' ')
