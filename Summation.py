# This summation function adds the consecutive round numbers from one number to the second one.
# Note that the first number should be smaller than the second.

number_1 = int(input("First number: "))
number_2 = int(input("Second number: "))

if number_1 >= number_2:
    print("Error: First number must be smaller than the second")
else:
    def summation(number_1, number_2):
        summation_result = number_1
        while number_2 > number_1:
            number_1 += 1
            summation_result += number_1
        return(summation_result)
    summation_result = summation(number_1, number_2)
    print(f"The summation result is: {summation_result}")