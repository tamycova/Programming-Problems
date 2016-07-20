import sys
for line in sys.stdin:
    l = line.strip().split(" ")
    a = int(l[0])
    b = int(l[1])
    count = 0
    f = [-1,-2,-3,-3]
    for i in range(a,b+1):
        d = f
        temp = i
        j = 0
        while temp > 0:
            d[j+1] = temp%10
            temp //= 10
        if (d[0]==d[1]) or (d[1]==d[2]) or (d[2]==d[3])  or (d[3]==d[0]) or (d[0]==d[2]) or (d[0]==d[3]) or (d[1]==d[3]):
            pass
        else:
            count += 1
    print(count)