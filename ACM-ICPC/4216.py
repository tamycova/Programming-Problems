while True:
    f = False
    n = int(input())
    if n == 0:
        break
    else:
        autos = []
        deltas = []
        b = [-1 for i in range(n)]
        for i in range(n):
            line = [int(i) for i in input().strip().split(" ")]
            autos.append(line[0])
            deltas.append(line[1])
        for i in range(n):
            d = deltas[i]
            if i+d <= -1 or i+d >=n or b[i+d]!=-1:
                print("-1")
                f = True
                break
            b[i+d] = autos[i]
        if not f:
            print(b[0],end="")
            for i in range(1,n):
                if i==n-1:
                    print(" " + str(b[i]))
                else:
                    print(" " + str(b[i]), end="")
                

