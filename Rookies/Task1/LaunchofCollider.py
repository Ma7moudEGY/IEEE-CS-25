number_of_particles = int(input(""))
Directions = input("")
Coordinates = input("").split()

def FirstCollision(directions, coords):
    direction = list(directions)
    coords = list(map(int, coords))
    times = []
    
    for i in range(len(coords) - 1):
        mid_point = int((coords[i] + coords[i+1]) /2)

        if direction[i] == "R" and direction[i+1] == "L":
            times.append(mid_point - coords[i])

    if times:
        print(min(times))
    else:
        print("-1")


FirstCollision(Directions, Coordinates)