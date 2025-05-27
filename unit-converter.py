# Print a welcome message
print("Welcome to the Unit Converter")

# Method for the unit conversion
def conversion_function():
    # Ask the user which conversion they would like to make
    conversion = input("Which of the following equations would you like to use: \n1 - Kilometres to Miles \n2 - Miles to Kilometres \n3 - Celsius to Farenheit \n4 - Farenheit to Celsius \n")
    # If the input is 1, then the conversion is for km to m
    if conversion == "1":
        # While loop to run until valid condition is met
        while True:
            # Store the user input for Kilometres
            km = input("Kilometres: ")
            try:
                # Try to store the input as a float
                km = float(km)
                # Calculate the conversion from kilometres to miles
                m = km * 0.621371
                # Print the result rounded to 2 decimal places
                print("Miles: ", round(m, 2))
                # Break out of the loop
                break
            # For any exceptions, print invalid message
            except ValueError:
                print("Invalid value! Please try again.")
    # If the input is 2, then the conversion is for m to km
    elif conversion == "2":
        # While loop to run until valid condition is met
        while True:
            # Store the user input for Miles
            m = input("Miles: ")
            try:
                # Try to store the input as a float
                m = float(m)
                # Calculate the conversion from miles to kilometres
                km = m * 1.60934
                # Print the result rounded to 2 decimal places
                print("Kilometres: ", round(km, 2))
                # Break out of the loop
                break
            # For any exceptions, print invalid message
            except ValueError:
                print("Invalid value! Please try again.")
    # If the input is 3, then the conversion is for C to F
    elif conversion == "3":
        # While loop to run until valid condition is met
        while True:
            # Store the user input for Celsius
            c = input("Celsius: ")
            try:
                # Try to store the input as an integer
                c = int(c)
                # Calculate the conversion from celsius to fahrenheit
                f = (c * 9/5) + 32
                # Print the result rounded to the nearest whole number
                print("Fahrenheit: ", round(f))
                break
            # For any exceptions, print invalid message
            except ValueError:
                print("Invalid value! Please try again.")
    # If the input is 4 then the conversion is for F to C
    elif conversion == "4":
        # While loop to run until valid condition is met
        while True:
            # Store the user input for the Fahrenheit
            f = input("Fahrenheit: ")
            try:
                # Try to store the input as an integer
                f = int(f)
                # Calculate the conversion from fahrenheit to celsius
                c = (f - 32) * 5/9
                # Print the result rounded to the nearest whole number
                print("Celsius: ", round(c))
                # Break out of the loop
                break
            # For any exceptions, print invalid message
            except ValueError:
                print("Invalid value! Please try again.")
    # Else, print the input is invalid and to try again
    else:
        print("Invalid input! Please try again.")
    # Call the restart function after the conversion has been made
    restart_function()

# Method to ask the user if they would like to make more conversions
def restart_function():
    # While loop to continously run until a condition is met
    while True:
        # Ask the user if they would like to make another conversion and store the input
        restart = input("Would you like to make another unit conversion? Yes/No: ")
        # If the input is yes, then call the conversion function
        if restart.lower() == "yes":
            conversion_function()
        # If the user input no, then exit the program
        elif restart.lower() == "no":
            exit()
        # Else, print the input is invalid and try again
        else:
            print("Invalid choice! Please try again.")
# Call the conversion function for the program to run
conversion_function()