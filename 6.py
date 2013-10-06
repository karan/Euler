# sum square difference

sum_of_square = sum([i**2 for i in range(101)])
sq_of_sum = sum([i for i in range(101)]) ** 2

print sq_of_sum - sum_of_square
