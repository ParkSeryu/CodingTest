N, M = map(int, input().split())
answer = []


def backTracking(depth):
    if depth == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N + 1):
        answer.append(i)
        backTracking(depth + 1)
        answer.pop()


backTracking(0)
