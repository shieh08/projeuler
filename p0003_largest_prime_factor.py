# Set the target number here.
target_number = 600851475143

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

for x in range(1,target_number):
  # Check to see if x is a factor of target_number.
  if target_number%x == 0:
    if target_number/x < x:
      break
    elif is_prime(x):
      print(x)