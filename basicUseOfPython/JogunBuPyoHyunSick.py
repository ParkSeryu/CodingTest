a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
print(type(a), type(remove_set))

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

# 아래 코드는 위 코드와 완전히 같다.
a = {1, 2, 3, 4, 5, 5, 5}
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)
