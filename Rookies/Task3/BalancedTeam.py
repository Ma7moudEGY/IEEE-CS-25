NumberOfStuendts = int(input(""))
Skills = input("").split()

def MaxTeam(s):
    skills = sorted(list(map(int, s)))
    left = 0
    mt = 0

    for right in range(len(skills)):
        while skills[right] - skills[left] > 5:
            left += 1

        mt = max(mt, right - left + 1)

    print(mt)


MaxTeam(Skills)