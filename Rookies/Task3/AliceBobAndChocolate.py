NumberOfBars = int(input(""))
Bars = input("").split()

def BarsEaten(bars):
    Times = list(map(int, bars))
    left = 0
    right = len(Times) - 1
    left_sum = 0
    right_sum = 0
    alice = 0
    bob = 0

    while left <= right:

        if left_sum <= right_sum:
            left_sum += Times[left]
            left += 1
            alice += 1

        else:
            right_sum += Times[right]
            right -= 1
            bob += 1
            
    print(alice, bob)


BarsEaten(Bars)