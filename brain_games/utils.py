def is_even(n):
    return 'yes' if n % 2 == 0 else 'no'


def find_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b