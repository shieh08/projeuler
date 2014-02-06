def recurse_check(number, multiple):
  if multiple == 0:
    return True
  elif number%multiple == 0:
    return recurse_check(number, multiple-1)
  else:
    return False

x = True
number = 0
multiple = 20
while x == True:
  number += multiple*(multiple-1)
  if recurse_check(number, multiple):
    print(number)
    x = False
