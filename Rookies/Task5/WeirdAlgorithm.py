N = int(input(""))

def WeirdAlg(n):
    print(n, end = " ")
    if n == 1:
        return
    
    if (n % 2 == 1):
        WeirdAlg(n*3 + 1)

    else:
        WeirdAlg(n // 2)
    
WeirdAlg(N)