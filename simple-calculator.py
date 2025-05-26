# Output a welcome message
print("Welcome to the Simple Calculator!")
print("You can perform basic calculations like addition(+), subtraction(-), multiplication(*), and division(/).")

def main_function():
    # While loop for the input validation for the first number
    while True:
        # Try to convert the input to a float data type
        try:
            num1 = float(input("Please enter the first number: "))
            break
        # If the conversion fails, print an error message to ask the user to enter a valid number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Storing all possible valid operators in a list
    valid_operators = ["+", "-", "*", "/"]
    # While loop for the input validation for the operator
    while True:
        # Ask the user to input an operator and check if its valid
        operator = input(f"Please enter one of the following operators: '+', '-', '*', '/': ")
        if operator in valid_operators:
            break
        # If the operator is not valid, print an error message and ask the user to enter a valid operator
        else:
            print("Invalid operator. Please enter a valid operator.")
    # While loop for the input validation for the second number
    while True:
        # Try to convert the input to a float data type
        try:
            num2 = float(input("Please enter the second number: "))
            break
        # If the conversion fails, print an error message and ask teh user to enter a valid number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Method to add two numbers
    def addition(num1, num2):
        total = num1 + num2
        # If the result is a whole number, convert it into an integer
        if total % total == 0:
            total = int(total)
        return total
    # Method to subtract two numbers
    def subtraction(num1, num2):
        total = num1 - num2
        # If the result is a whole number, convert it into an integer
        if total % total == 0:
            total = int(total)
        return total
    # Method to multiply two numbers
    def multiplication(num1, num2):
        total = num1 * num2
        # If the result is a while number, convert it into an integer
        if total % total == 0:
            total = int(total)
        return total
    # Method to divide two numbers
    def division(num1, num2):
        # If the first or second number is divided by 0, return an error message
        if num1 == 0 or num2 == 0:
            return "Error: You can't divide by 0."
        # If the result is a whole number, convert it into an interger
        total = num1 / num2
        if total % total == 0:
            total = int(total)
        # Else, round the total to 2 decimal places
        else:
            total = round(total, 2)
        return total
        
    # If statements to determine which operation to perform based on the selected operator
    if operator == "+":
        result = addition(num1, num2)
    elif operator == "-":
        result = subtraction(num1, num2)
    elif operator == "*":
        result = multiplication(num1, num2)
    elif operator == "/":
        result = division(num1, num2)

    # Output the result of the operation
    print(f"The result of {num1} {operator} {num2} is: {result}")
    # Call the reset calculator method
    reset_calculator()

# Method to reset the calculator
def reset_calculator():
    # Ask the user if they would like to perform another calculation and store the input
    reset_question = input("Would you like to perform another calculation? Yes/No: ")
    # If the user inputs "yes", call the main function to reset the calculator
    if reset_question.lower() == "yes":
        main_function()
    # Else, if the user inputs "no", print a goodbye message and exit the program
    else:
        print("Goodbye!")
        exit()

# Call the main function to start the calculator
main_function()