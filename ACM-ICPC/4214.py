def isleap(y):
    if y % 400 == 0 or(y % 4 == 0 and y % 100 != 0):
        return True
    else:
        return False


def damedias(d, m, y):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isleap(y):
        days[1] += 1
    m -= 1
    suma = 0
    i = 0
    while i < m:
        suma += days[i]
        i += 1
    i = 1899
    while i < y:
        suma += 365 + isleap(i)
        i += 1
    suma += d
    return suma


while True:
    n = int(input())
    if n == 0:
        break
    else:
        days = []
        for i in range(n):
            line = input().strip().split()
            days.append(
                [damedias(int(line[0]), int(line[1]),
                          int(line[2])), int(line[3])])
        cnt = 0
        suma = 0
        for i in range(1, n):
            if days[i - 1][0] == days[i][0] - 1:
                cnt += 1
                suma += days[i][1] - days[i - 1][1]
        print("{0} {1}".format(cnt, suma))
