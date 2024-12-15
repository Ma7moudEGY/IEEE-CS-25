def Solution():
    n, m = list(map(int, input("").split()))
    cows = []
    acs = []

    for _ in range(n):
        si, ti, ci = list(map(int, input("").split()))
        cows.append((si, ti, ci))

    for _ in range(m):
        ai, bi, pi, mi = list(map(int, input("").split()))
        acs.append((ai, bi, pi, mi))

    best_cost = [float('inf')]
    coverage = [0 for _ in range(101)]

    def BackTrack(index, current_cost, current_coverage):
        if CowsSatisfied(cows, current_coverage):
            best_cost[0] = min(best_cost[0], current_cost)
            return
        
        if index == m or current_cost >= best_cost[0]:
            return

        BackTrack(index + 1, current_cost, current_coverage)

        temp_coverage = current_coverage.copy()

        ai, bi, pi, mi = acs[index]

        for i in range(ai, bi + 1):
            temp_coverage[i] += pi

        BackTrack(index + 1, current_cost + mi, temp_coverage)

    def CowsSatisfied(cows, coverage):
        for si, ti, ci in cows:
            for i in range(si, ti + 1):
                if coverage[i] < ci:
                    return False
        return True
    
    BackTrack(0, 0, coverage)

    print(best_cost[0])

Solution()