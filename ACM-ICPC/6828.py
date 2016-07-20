import sys
cont = 0
for line in sys.stdin:
    if cont == 0:
        N = int(line)
        cont += 1
    elif cont == 1:
        ans = 0
        cont = 0
        T = sorted([int(i) for i in line.strip().split(" ")])
        i = 0
        j = 0
        while i < N / 2:
            j += min(T[2 * i + 1] - T[2 * i], 24 - T[2 * i + 1] + T[2 * i])
            i += 1
        ans = j
        j = min(T[N - 1] - T[0], 24 - T[N - 1] + T[0])
        i = 1
        while i < N / 2:
            j += min(T[2 * i] - T[2 * i - 1], 24 - T[2 * i] + T[2 * i - 1])
            i += 1
        ans = min(j, ans)
        print(ans)
