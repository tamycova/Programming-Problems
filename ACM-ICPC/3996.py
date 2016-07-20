n = int(input())
for i in range(n):
    m = int(input())
    digits = [0 for i in range(10)]
    for i in range(1,m+1):
        d = str(i)
        for j in d:
            digits[int(j)] += 1
    print(" ".join((str(i) for i in digits)))