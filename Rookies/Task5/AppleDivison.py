NumOfApples = int(input(""))
Weights = list(map(int, input("").split()))


def Divison(index, sum1, sum2):
    if index == len(Weights):
        return abs(sum1 - sum2)

    diff1 = Divison(index + 1, sum1 + Weights[index], sum2)

    diff2 = Divison(index + 1, sum1, sum2 + Weights[index])

    return min(diff1, diff2)

print(Divison(0, 0, 0))