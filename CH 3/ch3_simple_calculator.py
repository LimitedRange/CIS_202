# This program is a simple calculator.

# Get two numbers from the user.
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Get the math operator from the user.
operator = input("Enter one of the following operators:\n"
"+ for addition\n"
"- for subtraction\n"
"* for multiplication\n"
"/ for division\n")

# Determine which calculation to perform.
if operator == "+":
    result = first_number + second_number

    print(f"\nYou entered the two numbers {first_number} and {second_number} "
         f"and the operator entered was {operator}.")
    print(f"\nThe result of {first_number} {operator} {second_number} is {result}.")
elif operator == "-":
    result = first_number - second_number

    print(f"\nYou entered the two numbers {first_number} and {second_number} "
         f"and the operator entered was {operator}.")
    print(f"\nThe result of {first_number} {operator} {second_number} is {result}.")
elif operator == "*":
    result = first_number * second_number

    print(f"\nYou entered the two numbers {first_number} and {second_number} "
         f"and the operator entered was {operator}.")
    print(f"\nThe result of {first_number} {operator} {second_number} is {result}.")
elif operator == "/":
    if second_number == 0:
        print("\nDivision by zero is not allowed.")
    else:
        result = first_number / second_number
        
        print(f"\nYou entered the two numbers {first_number} and {second_number} "
                 f"and the operator entered was {operator}.")
        print(f"\nThe result of {first_number} {operator} {second_number} is {result}.")   
else:
    print("\nInvalid operator.")