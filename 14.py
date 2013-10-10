# largest collatz sequence

def size(n):
	nums = [n]
	while n > 1:
		if n % 2 == 0:
			n /= 2
		else:
			n = (3 * n) + 1
		nums.append(n)
	return len(nums)

longest = 0
longest_size = 0

for i in range(1, 1000000):
	size_i = size(i)
	if size_i > longest_size:
		longest_size = size_i
		longest = i

print longest
print longest_size
