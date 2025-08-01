def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n <= 3:
        return True   # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # eliminate multiples of 2 and 3

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
