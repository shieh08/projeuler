a = 1
b = 1
limit = 4000000
sum = 0

while a < limit:
  a, b = b, a+b
  if a%2 == 0:
    sum += a

print(sum)

