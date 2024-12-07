Parameters = input("").split()
Numbers = input("").split()

def MaxPairs(parameters, nummbers):
    Params = list(map(int, parameters))
    nums = sorted(list(map(int, nummbers)))
    pairs = 0
    left = 0
    right = 0

    while right < len(nums):
        diff = nums[right] - nums[left]

        if diff == Params[1]:
            pairs += 1
            left += 1
            right += 1

        elif diff < Params[1]:
            right += 1

        else:
            left += 1

        if left == right:
            right += 1


    print(pairs)

MaxPairs(Parameters, Numbers)