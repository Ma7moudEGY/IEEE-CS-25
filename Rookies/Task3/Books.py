Parameters = input("").split()
Times = input("").split()


def MaxBooks(parameters, time):
    Params = list(map(int, parameters))
    times = list(map(int, time))
    counter = 0
    sum = 0

    left = 0

    for right in range(Params[0]):
        sum += times[right]

        while sum > Params[1]:
            sum -= times[left]
            left += 1

        counter = max(counter, right - left + 1)

    print(counter)

MaxBooks(Parameters, Times)