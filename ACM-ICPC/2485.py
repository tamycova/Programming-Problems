pos = {"a":1,"e":2,"i":3,"o":4,"u":5}
while True:
    l = input().strip().lower()
    if l == "#":
        break
    else:
        cont = {"a":0,"e":0,"i":0,"o":0,"u":0}
        for i in l:
            if i in cont:
                cont[i] -= 1
        a = sorted(cont.items(), key=lambda x:(x[1],x[0]))
        s = ""
        for i in a:
            s += "{0}:{1} ".format(i[0],abs(i[1]))
        print(s[:len(s)-1]+".")
