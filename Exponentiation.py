# Exponentiation

# RESOLVER TODAS LAS POSIBILIDADES DIAGRAMA DE FLUJO
# Only positive powers.

b = int(input("Insert base: "))
n = int(input("Insert power: "))

def even_odd(n):
    if n % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    return result

c = (even_odd(n))
print(c, "Power")

def exp_1(b, n):
    result = b
    for i in range(1, n):
        result *= b
        i += 1
    return result

# Function de arriba y de abajo son iguales

def neg_base_even_power(b, n):
    result = b
    for i in range(1, n):
        result *= b
        i += 1
    return result


def neg_base_odd_power(b, n):
    result = b
    for i in range(1, n):
        result *= b
        i += 1
    return result


if b == 0:
    if n == 0:
        r = 1
    else:
        r = 0
else:
    if n == 0:
        r = 1
    else:
        if b > 0:
            r = exp_1(b, n)
        else:
            if c == "Even":
                r = neg_base_even_power(b, n)
            else:
                r = neg_base_odd_power(b, n)
print(r)
