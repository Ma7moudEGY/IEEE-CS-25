Parameters = input("").split()
Points = input("").split()

def Solution(parameters, point):
    Params = list(map(int, parameters))
    points = list(map(int, point))

    counter = 0
    j = 0

    for i in range(len(points)):
        while points[i] - points[j] > Params[1]:
            j += 1

        counter += ((i - j - 1) * (i - j)) // 2
        

    print(counter)


Solution(Parameters, Points)