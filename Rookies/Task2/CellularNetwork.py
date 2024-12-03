Numbers = input("").split()
CitysCoords = input("").split()
TowersCoords = input("").split()


def MinimalR(coords1, coords2):
    citycoords = list(map(int, coords1))
    towercoords = list(map(int, coords2))

    j = 0
    r = 0
    for i in range(len(citycoords)):
        while j < len(towercoords)- 1 and abs(towercoords[j + 1] - citycoords[i]) <= abs(towercoords[j] - citycoords[i]):
            j += 1

        r = max(r, abs(towercoords[j] - citycoords[i]))

    print(r)


MinimalR(CitysCoords, TowersCoords)