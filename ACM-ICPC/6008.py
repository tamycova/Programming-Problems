from itertools import product
n = int(input())
for i in range(n):
    # dif = 99999999999999999999
    # a = input() + "n"
    # al = []
    # num = ""
    # for i in a[2:]:
    #     if (i == " " or i=="n") and num:
    #         al.append(int(num))
    #     else:
    #         num += i
    # b = input() + "n"
    # num = ""
    # for j in b[2:]:
    #     if (j == " " or j=="n") and num:
    #         for i in al:
    #             delta = abs(int(num)-i)
    #             if delta < dif:
    #                 dif = delta
    #                 if dif == 0:
    #                     break
    #     else:
    #         num += j
    # print(dif)
    print(min(abs(int(a)-int(b)) for a,b in product(input().strip().split(" ")[1:],input().strip().split(" ")[1:]))


