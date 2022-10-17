
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###

count = 0
evencount = 0
prev_even = 0

for i in range(10):
  num = int(input("Enter number: "))
  if num % 2 == 0:
    if prev_even == 1 and evencount == 1:
      count += 1
    evencount += 1
    prev_even = 1

  if num % 2 == 1:
    evencount = 0

  i += 1


print(count)