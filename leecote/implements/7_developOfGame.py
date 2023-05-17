def turn_left(direct):
    direct -= 1
    if direct == -1:
        direct = 3
    return direct


N, M = map(int, input().split())
x, y, direction = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

maps = list()
for _ in range(N):
    maps.append(list(map(int, input().split())))

maps[x][y] = 2
turn_cnt = 0
answer = 1

while True:
    direction = turn_left(direction)
    nx = x + dx[direction]
    ny = y + dy[direction]
    if maps[nx][ny] == 0:
        x = nx
        y = ny
        maps[x][y] = 2
        answer += 1
        turn_cnt = 0
    else:
        turn_cnt += 1
    if turn_cnt == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        if maps[nx][ny] != 0:
            break
        else:
            x = nx
            y = ny
        turn_cnt = 0
print(answer)
