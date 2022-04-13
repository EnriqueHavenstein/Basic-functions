# This function checks which number is greater

def greater(a, b):
    if a > b:
        r = "The first number is greater"
    elif a < b:
        r = "The second number is greater"
    else:
        r = "Numbers are equal"
    return r


a = int(input("Insert the first number: "))
b = int(input("Insert the second number: "))
result = greater(a, b)
print(result)
