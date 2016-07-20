n = int(input())
for i in range(n):
    listo = False
    f = input()
    line = input().strip().split(" ")
    for i in range(len(line)):
        if "#" not in line[i]:
            antes = line[:i]
            despues = line[i+1:]
            new = despues + [line[i]] + antes
            print(" ".join(new))
            listo = True
            break
    if not listo:
        print(" ".join(line))

