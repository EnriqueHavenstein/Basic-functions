# Exponentiation

# RESOLVER TODAS LAS POSIBILIDADES DIAGRAMA DE FLUJO

b = int(input("Insert base: "))
n = int(input("Insert power: "))

# only powers bigger than 0


def exp_1(b, n):
    result = b
    for i in range(1, n):
        result *= b
        i += 1
    return result


def exp_0(b, n):
    result = 1
    return result


def exp_neg_even_power(b, n):
    result = b
    for i in range(n, 0):
        result *= b
        i += 1
    return result


def exp_neg_odd_power(b, n):
    result = b
    for i in range(1, n):
        result *= b
        i += 1
    return -result


if n == 0:
    r = exp_0(b, n)
    print(r)
if b < 0:
    c = int(n % 2)
    print(c)
    if c == 0:
        r = exp_neg_even_power(b, n)
        print(r)
if n >= 1:
    r = exp_1(b, n)
    print(r)


exponentiation_result_1 = exp_1(b, n)
exponentiation_result_0 = exp_0(b, n)
exponentiation_result_even = exp_neg_even_power(b, n)
exponentiation_result_odd = exp_neg_odd_power(b, n)

# print(f"The result is: {exponentiation_result_1}")

print(exponentiation_result_1, exponentiation_result_0, exponentiation_result_even, exponentiation_result_odd)