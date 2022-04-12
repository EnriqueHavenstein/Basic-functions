# Factorial function


number = int(input("Round number to calculate factorial: "))


def factorial(number):
    fac = 1
    for number in range(1, number + 1):
        fac *= number
    return(fac)


factorial_result = factorial(number)

print(f"The result is: {factorial_result}")