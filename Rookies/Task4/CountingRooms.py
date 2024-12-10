Height, Width = map(int, input("").split())

def RoomCount(width, height):
    Direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    building = [input().strip() for _ in range(height)]


    visited = [[False for _ in range(width)] for _ in range(height)]

    def BFS(x, y):
        queue = [(x, y)]
        visited[x][y] = True

        while queue:
            xCurrent, yCurrent = queue.pop(0)
            for xMove, yMove in Direction:
                xNew, yNew = xCurrent + xMove, yCurrent + yMove

                if 0 <= xNew < height and 0 <= yNew < width and not visited[xNew][yNew] and building[xNew][yNew] == ".":
                    visited[xNew][yNew] = True
                    queue.append((xNew, yNew))


    count = 0
    for i in range(height):
        for j in range(width):
            if building[i][j] == "." and not visited[i][j]:
                count += 1
                BFS(i, j)

    print(count)


RoomCount(Width, Height)