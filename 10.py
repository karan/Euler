# summation of primes

def is_prime(x):
    if x == 2:
        return True
    else:
        for i in range(2, int((x ** 0.5)) + 1):
            if x % i == 0:
                return False
    return True

sum_2_mil = 0

for i in range(2, 2000000):
    if is_prime(i):
        sum_2_mil += i

print sum_2_mil
