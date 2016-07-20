while True:
    line1 = input().strip().split(" ")
    if line1 == ["0", "0"]:
        break
    else:
        n_songs = int(line1[0])
        n_queries = int(line1[1])
        song_names = input().strip().split(" ")
        queries = [int(i) for i in input().strip().split(" ")]
        for i in queries:
            if n_songs == 1:
                print(song_names[0])
                continue
            else:
                pot = 1
                for j in range(1, 100000000000000000000000):
                    if i > j * pot * n_songs:
                        i -= j * pot * n_songs
                    else:
                        pos = (i - 1) // j
                        i = (i - 1) % j
                        f = j - 1
                        for z in range(0, 1000000000000000000):
                            if f == i:
                                print(song_names[pos % n_songs])
                                break
                            else:
                                pos //= n_songs
                            f -= 1
                        break
                    pot *= n_songs
        print("")
