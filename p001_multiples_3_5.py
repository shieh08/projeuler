# projecteuler.net/problem=1
# Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0;

for x in range(1,1000):
  if x%3 == 0:
    sum += x;
  elif x%5 == 0:
    sum += x;

print(sum);