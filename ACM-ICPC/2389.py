def isPali(n, base):
    s = ""
    t = ""
    while n:
        r = n % base
        n //= base
        if r <= 9:
            s = s + "0" + str(r)
            t = "0" + str(r) + t
        else:
            r -= 10
            s = s + "a" + str(r)
            t = "a" + str(r) + t
    return s == t

num = int(input())
while num != 0:
    bases = []
    for i in range(2, 17):
        if isPali(num, i):
            bases.append(str(i))
    if bases:
        print(
            "Number {0} is palindrom in basis {1}".format(str(num), " ".join(bases)))
    else:
        print("Number {} is not palindrom".format(str(num)))
    num = int(input())
