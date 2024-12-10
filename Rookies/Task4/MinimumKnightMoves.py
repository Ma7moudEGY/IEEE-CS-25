NumOfMoves = int(input(""))

def MinimumMoves(num):
    knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    Starts = []
    Ends = []

    for i in range(num):
        startPos, endPos = input("").split()
        xStart = ord(startPos[0]) - ord('a')
        yStart = int(startPos[1]) - 1
        Starts.append([xStart, yStart])

        xEnd = ord(endPos[0]) - ord('a')
        yEnd = int(endPos[1]) - 1
        Ends.append([xEnd, yEnd])

    for j in range(len(Starts)):
        if Starts[j] == Ends[j]:
            print(0)
            continue
            
        queue = [(Starts[j][0], Starts[j][1], 0)]
        visited = set()
        visited.add((Starts[j][0], Starts[j][1]))

        while queue:  
            xCurrent, yCurrent, steps = queue.pop(0)

            for xMove, yMove in knight_moves:
                xNew = xCurrent + xMove
                yNew = yCurrent + yMove

                if 0 <= xNew < 8 and 0 <= yNew < 8:
                    if (xNew, yNew) == (Ends[j][0], Ends[j][1]):
                        print(steps + 1)
                        queue = []
                        break

                    if (xNew, yNew) not in visited:
                        queue.append((xNew, yNew, steps + 1))
                        visited.add((xNew, yNew))


MinimumMoves(NumOfMoves)