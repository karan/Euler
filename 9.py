# special pythagorean triplet

SUM = 1000
found = False
count = 0

for a in xrange(1, SUM):
    for b in xrange(a, SUM):
        if a + b < 1000:
            for c in xrange(b, SUM):
                count += 1
                if (a + b + c == SUM) and ((a ** 2 + b ** 2) == (c ** 2)):
                    found = True
                    print '%d + %d + %d = %d' % (a, b, c, a + b + c)
                    print 'Product is: %d' % (a * b * c)
                    break
        if found:
            break
    if found:
        break

print '%d steps made.' % count
