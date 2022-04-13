# The following function checks if a given number is even or odd.

def even_odd(n):
    if n % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    return result


n = int(input("Insert number to check if it is Even or Odd: "))

r = (even_odd(n))

print(r)