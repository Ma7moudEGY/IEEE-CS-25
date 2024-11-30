numeber = int(input(""))

def is_almost_lucky(num):
    lucky_nums = [4, 7, 47, 74, 444, 447, 474, 477, 744, 747, 774, 777]

    for lucky_num in lucky_nums:
        if (num % lucky_num) == 0:
            print("YES")
            return
        
    print("NO")


is_almost_lucky(numeber)