N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    flag = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            flag = 1
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if flag == 1 :
        print(1)
    else:
        print(0)

A.sort()

for i in range(len(B)):
    binary_search(A, B[i])
