a = input()

parsing = list(map(int, a.split(':')))


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


gc = gcd(parsing[0], parsing[1])

st = str(parsing[0] // gc) + ':' + str(parsing[1] // gc)

print(st)
