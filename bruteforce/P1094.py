X = int(input())
stack = list()
answer = 0
while X > 0:
    remain = X % 2
    X = X // 2
    stack.append(remain)

for i in stack:
    if i == 1:
        answer += 1

print(answer)