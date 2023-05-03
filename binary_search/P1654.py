K, N = map(int, input().split())
a = list()

for i in range(K):
    a.append(int(input()))

a.sort()


def binary_search(arr, target):
    left, right = 0, arr[len(arr) - 1]

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for index in range(K):
            cnt += arr[index] // mid
        if cnt == target:
            print(mid)
        elif cnt > target:
            left = mid + 1
        else:
            right = mid - 1


binary_search(a, N)
