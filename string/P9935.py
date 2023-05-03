str = input()
bomb = input()
stack = list()
index = 0
i = 0

while i != len(str) + 1:
    if len(stack) < len(bomb):
        stack.append(str[i])
        i += 1
    else:
        break_flag = 0
        for j in range(0, len(bomb)):
            if stack[index + j] != bomb[j]:
                break_flag = 1
                break
        if break_flag == 0:
            for k in range(len(bomb)):
                stack.pop()
            index -= len(bomb)
        else:
            if i != index:
                stack.append(str[i])
                i += 1
                index += 1
        print(stack)


if len(stack) == 0:
    print("FRULA")
else:
    print('end')
