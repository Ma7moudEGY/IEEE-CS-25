Shops = int(input(""))
Prices = input("").split()
Days = int(input(""))

def max_num_of_shops(prices, days):
    coins = []
    for i in range(days):
        i = int(input(""))
        coins.append(i)

    res = sorted(list(map(int, prices)))

    for coin in coins:
        print(binary_search(res, coin)) 


def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if array[mid] <= target:
            left = mid + 1

        else:
            right = mid - 1

    return right + 1

max_num_of_shops(Prices, Days)
