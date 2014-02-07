# projecteuler.net/problem=7
# What is the 10,001st prime number?

# Function to figure out prime or not.
def is_prime(n):
  if n < 2:
    return False

  # Eliminate even numbers.
  if not n & 1:
    return False

  # Check for each odd number up to sqrt of n.
  for x in range(3, int(n**0.5)+1, 2):
    if n % x == 0:
      return False
  return True

prime = 1
number_to_test = 1
while prime < 10001:
  next_prime = False
  while next_prime == False:
    number_to_test += 1
    if is_prime(number_to_test):
      prime += 1
      next_prime = True

print(number_to_test)