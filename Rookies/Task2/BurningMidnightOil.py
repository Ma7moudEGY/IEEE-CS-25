Parameters = input("").split()

def MinimumValue(parameters):
    Params = list(map(int, parameters))

    v2 = Params[0] * (Params[1] - 1) // Params[1]
    v = v2

    while 1:
        sum = 0
        power = 1

        while v // power > 0:
            sum += v // power
            power *= Params[1]

        if sum >= Params[0]:
            break
        
        v += 1

    print(v)


MinimumValue(Parameters)