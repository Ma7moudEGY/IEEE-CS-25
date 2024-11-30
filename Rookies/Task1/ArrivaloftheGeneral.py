length = int(input(""))
Heights = input("").split()


def minimum_time(heights : list):
    
    res = list(map(int, heights))

    min_indices = [i for i, x in enumerate(res) if x == min(res)]
    max_indices = [i for i, x in enumerate(res) if x == max(res)]

    min_index = max(min_indices)
    max_index = min(max_indices)

    if max_index > min_index:
        min_steps = max_index + (len(res) - min_index - 1)
    else:
        min_steps = max_index + (len(res) - min_index)

    print(min_steps - 1)


minimum_time(Heights)