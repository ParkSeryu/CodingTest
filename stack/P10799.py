userInput = input()
stack = []
count = 0

# while i < (len(userInput) - 1):
#     if userInput[i] + userInput[i + 1] == "()":  # 레이저인지 판별
#         count += len(stack)
#         i += 2
#     elif userInput[i] == "(":
#         stack.append("(")
#         i += 1
#     else:
#         if stack:
#             stack.pop()
#             count += 1
#             i = i + 1
#
#
# if userInput[len(userInput) - 1] == ")" and userInput[len(userInput) - 2] != "(":
#     count += 1
#
# print(count)


# for i in range(len(userInput)):
#     if userInput[i] == ")":
#         if userInput[i-1] == "(":
#             count += len(stack)
#         else:
#             stack.pop()
#             count += 1
#     elif i + 1 != len(userInput):
#         if userInput[i+1] != ")":
#             stack.append("(")

for i in range(len(userInput)):
    if userInput[i] == "(":
        stack.append("(")
    else:
        if userInput[i-1] == "(":
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count+= 1
    print(stack)

print(count)