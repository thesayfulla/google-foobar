def decimal_to_base(n, b):
    if b == 10 or n == 0:
        return str(n)

    digits = ''
    while n:
        digits += str(n % b)
        n //= b

    return digits[::-1]


def lambda_algorithm(n, b):
    k = len(n)
    sorted_str = ''.join(sorted(n))
    
    x = int(sorted_str[::-1], b)
    y = int(sorted_str, b)
    z = abs(x - y)
    result = decimal_to_base(z, b)
    
    result = '0' * (k - len(result)) + result
    
    return result


def floyd(func, n, b):
    tortoise = func(n, b)
    hare = func(func(n, b), b)
    while tortoise != hare:
        tortoise = func(tortoise, b)
        hare = func(func(hare, b), b)

    lam = 1
    hare = func(tortoise, b)
    while tortoise != hare:
        hare = func(hare, b)
        lam += 1

    return lam


def solution(n, b):
    return floyd(lambda_algorithm, n, b)
