words = []

for i in range(5):
    A = input()
    B = []
    for j in range(len(A)):
        B.append(A[j])
    words.append(B)

for i in range(5):
    for j in range(len(words[i])):
        print(words[j][i], end='')


