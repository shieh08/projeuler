# projecteuler.net/problem=6
# Find the difference between the sum of the squares 
# of the first one hundred natural numbers 
# and the square of the sum.

def sum_of_squares(n):
  sum = 0
  for x in range(1, n+1):
    sum += x**2
  return sum

def square_of_sums(n):
  sum = 0
  for x in range(1, n+1):
    sum += x
  return sum**2

n = 100
difference = abs(sum_of_squares(n) - square_of_sums(n))
print(difference)
