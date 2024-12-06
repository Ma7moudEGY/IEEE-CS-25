NumberOfCases = input("").split()

def Solution(number):
    num = int(number[0])
    count = 0
    pairs = []

    for o in range(num):
        count = 0
        Params = list(map(int, input("").split()))
        p = list(map(int, input("").split()))
        p.sort()

        for i in range(Params[0]):
            low = binary_left(p, i + 1, Params[0] - 1, Params[1] - p[i])
            high = binary_right(p, i + 1, Params[0] - 1, Params[2] - p[i])

            if low <= high:
                count += (high - low + 1)

        pairs.append(count)

    for i in pairs:
        print(i)


def binary_left(array, start, end, value):
    low = start
    high = end

    while high >= low:
        mid = (high + low) // 2

        if array[mid] >= value:
            high = mid -1

        else:
            low = mid + 1

    return low


def binary_right(array, start, end, value):
    low = start
    high = end

    while high >= low:
        mid = (high + low) // 2

        if array[mid] <= value:
            low = mid + 1

        else:
            high = mid -1

    return high



Solution(NumberOfCases)