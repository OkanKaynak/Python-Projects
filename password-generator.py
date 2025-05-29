# Import library for random to be able to randomly chose from a range of letters, numbers and symbols
import random
# Import the string library to be able to ensure the password contains letters, numbers and symbols
import string

# Print a welcome message about the program
print("\nWelcome to the Password Generator!")
# Print a message about the password that will be generated and its features
print("\nThe password generated will contain the following features: \n - Uppercase letters (A-Z) \n - Lowercase letters (a-z) \n - Numbers (0-9) \n - Symbols (!\"#$&\'()*+,-./:;<=>?[\]^_`{|}~)\n")
# Method for asking and generating a password
def password_function():
    # While condition to loop through until conditions are met (for error handling)
    while True:
        # Ask the user if they would like to generate a password
        user_input = input("Generate a password? Yes/No: ")
        # If the user input yes, then generate a password with the required features
        if user_input.lower() == "yes":
            # Set the letters, numbers and symbols to the approriate values using the string library functions
            letters = string.ascii_letters
            numbers = string.digits
            symbols = string.punctuation
            # Set conditions to be true to ensure there are all 3 types of characters within the password
            contain_letters = True
            contain_numbers = True
            contain_symbols = True
            # Set the has conditions to false by default
            has_letter = False
            has_number = False
            has_symbol = False
            # All the possible characters are combined within one variable
            characters = string.ascii_letters + string.digits + string.punctuation
            # Password is set to an empty string
            password = ""
            # Meets criteria is set false until the password is confirmed to have all 3 types of characters and meets the length of 12 characters
            meets_criteria = False
            # While the meets criteria variables is false and the length of the password is less than 12, randomly select values from the characters variable
            while meets_criteria == False or len(password) < 12:
                # Randomly select a value in characters and store in the new characters variable
                new_character = random.choice(characters)
                # Increment the new character onto the password string
                password += new_character
                # If the new character that was added meets either a letter, number of symbol, then set the "has_..." condition to true based on the character
                if new_character in letters:
                    has_letter = True
                elif new_character in numbers:
                    has_number = True
                elif new_character in symbols:
                    has_symbol = True
                # Set the meet criteria to true to check if the password meets the criteria overall
                meets_criteria = True
                # If there is a letter, meets criteria is set to the value of has letter
                if contain_letters == True:
                    meets_criteria = has_letter
                # If there is a number, meets criteria is set to the value of has number
                if contain_numbers == True:
                    meets_criteria = meets_criteria and has_number
                # If there is a symbol, meet criteria is set to meet criteria and has symbol values. Will be truth if there is a letter, number and symbol
                if contain_symbols == True:
                    meets_criteria = meets_criteria and has_number and has_symbol
            print("\nPassword Generated: ", password)
            break
        # If the user input no, the print a goodbye message and exit the program
        elif user_input.lower() == "no":
            print("\nGoodbye!")
            exit()
        # Else, the user input an invalid choice and print an invalid message to to try again
        else:
            print("\nInvalid choice! Please try again.")
    # Call the restart function
    restart_function()
# Method to ask the user if they would like to generate another password or exit the program
def restart_function():
    # Ask the user if the would like to generate another password and store the input
    restart_choice = input("\nWould you like to generate another password? Yes/No: ")
    # If the input is yes, then call the password function
    if restart_choice.lower() == "yes":
        password_function()
    # If the input is no, then print a goodbye message and exit the program
    elif restart_choice.lower() == "no":
        print("\nGoodbye!")
        exit()
    # Else, the input is invalid and print out a message to tell the user the input is invalid and to try again.
    else:
        print("\nInvalid choice! Please try again.")
# Call the password function to begin the program
password_function()