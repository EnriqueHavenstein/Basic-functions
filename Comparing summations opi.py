# Comparing summations opi.
# Prove that one summation is bigger by one than the other

summation_1 = 0
summation_2 = 0

c = 0
while c <= 9:
  summation_1 += 2**c
  c += 1
print(summation_1*2)

d = 0
while d <= 10:
  summation_2 += 2**d
  d += 1
print(summation_2)