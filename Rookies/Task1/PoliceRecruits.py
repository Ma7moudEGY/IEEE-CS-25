length = input("")
Events = input("").split()

recruits = 0
crimes = 0

def Untreatd_Crimes(events : list):
    recruits = 0
    crimes = 0
    untreated = 0

    res = list(map(int, events))

    for event in res:
        if recruits > 0 and event == -1:
            recruits -= 1
            continue

        if event == -1:
            crimes += 1
        else:
            recruits += event

        if crimes >= recruits:
            if untreated + 1 <= crimes:
                untreated += 1

    print(untreated)

Untreatd_Crimes(Events)