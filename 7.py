#10001 prime

def is_prime(x):
    if x < 2:
        return False
    #elif x % 2 == 0:
    #    return False
    else:
        for i in range(2, int((x ** 0.5) + 1)): # check odd numbers upto sqrt(x)
            if x % i == 0:
		        return False
    return True

primes = []

num = 2

while len(primes) != 10001:
    if is_prime(num):
        primes.append(num)
    num += 1

print primes[:10]
print primes[-1]
