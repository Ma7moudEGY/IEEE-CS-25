length = input("")
Events = input("").split()

def Untreatd_Crimes(events : list):
    recruits = 0
    untreated = 0

    res = list(map(int, events))

    for event in res:
        if event == -1:
            if recruits > 0:
                recruits -= 1
            else:
                untreated += 1
        else:
            recruits += event

    print(untreated)

    print(untreated)

Untreatd_Crimes(Events)