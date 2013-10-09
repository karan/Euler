# Highly divisible triangular number

import math

def get_divisors(x):
    divisors = 0
    for i in xrange(1, int(math.sqrt(x)) + 1)   :
        if x % i == 0:
            # divisors.append(i)
            divisors += 2

    if math.sqrt(x) * math.sqrt(x) == x:
        divisors -= 1
    
    return divisors

x = 1
triangle = 0

while True:
    divisors = get_divisors(triangle)
    print '%d. %d  -->>  %d' % (x, triangle, divisors)
    if divisors >= 500:
        print '%d has over 500 divisors' % triangle
        break
    else:
        triangle += x
        x += 1
