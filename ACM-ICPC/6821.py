import sys
lines = []
cont = 0
done = False
for line in sys.stdin:
    cont += 1
    lines.append(line.strip().split(" "))
    if cont == 2:
        cont = 0
        for i in range(len(lines[0])):
            if (lines[0][i] == "0" and lines[1][i] != "1") or (lines[0][i] == "1" and lines[1][i] != "0"):
                print("N")
                done = True
                break
        if not done:
            print("Y")
        lines = []
        done = False