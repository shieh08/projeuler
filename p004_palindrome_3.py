x_digits = 3
min = 10**(x_digits-1)
max = 10**x_digits
max_product = 0;

for x in range(min,max):
  for y in range(x,max):
    product = x * y
    list = [int(i) for i in str(product)]
    reverse = list[::-1]
    if list == reverse:
      if product > max_product:
        max_product = product
        print(max_product)