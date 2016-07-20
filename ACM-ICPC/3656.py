while True:
    n = int(input())
    if n == 0:
        break
    else:
        a = [int(i) for i in input().strip().split(" ")]
        b = [int(i) for i in input().strip().split(" ")]
        mi = 0
        mp = 0
        ji = 0
        jp = 0
        # int j
        for j in a:
            mi += j%2
            mp += not(j%2)
        for j in b:
            ji += j%2
            jp += not(j%2)
        if mp-ji<0:
            mp = 0
        else:
            mp -= ji
        if mi - jp <0:
            mi = 0
        else:
            mi -= jp
        print(mi+mp)