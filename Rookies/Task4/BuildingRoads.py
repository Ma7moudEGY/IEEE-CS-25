from collections import deque

n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

def minimum_new_roads_bfs(n, m, roads):
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)

    def bfs(start):
        queue = deque([start])
        visited[start] = True
        component = []

        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return component

    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            components.append(bfs(i))

    new_roads = []
    for i in range(1, len(components)):
        new_roads.append((components[i - 1][0], components[i][0]))

    return len(new_roads), new_roads

k, new_roads = minimum_new_roads_bfs(n, m, roads)

print(k)
for a, b in new_roads:
    print(a, b)