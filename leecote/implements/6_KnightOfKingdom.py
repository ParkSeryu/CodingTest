knights = input()
rows = [i for i in range(1, 9)]
columns = [chr(i) for i in range(ord('a'), ord('i'))]
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

answer = 0

for i in range(len(steps)):
    if chr(ord(knights[0]) + steps[i][0]) in columns:
        if int(knights[1]) + steps[i][1] in rows:
            answer += 1

print(answer)
