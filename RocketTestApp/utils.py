def closePrimeNumber(num: int) -> int:
    num += 1
    if num < 2:
        return 1
    elif num == 2:
        return 2
    else:
        if isPrime(num):
            return num
        else:
            return closePrimeNumber(num)

def isPrime(num:int) -> bool:
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    return True