# Importing the random library to use for generating random numbers for the dice rolls.
import random
# Print the welcome message
print("Welcome to the Dice Simulator!")

# Intro function to ask if the user would like to roll the dice
def intro_function():
    # While loop to constantly run until conditions are met
    while True:
        roll = input("Would you like to roll a six-sided dice? Yes/No: ")
        # If the user inputs "yes", then redirect to the roll function
        if roll.lower() == "yes":
            roll_function()
        # If the user inputs "no", then output a goodbye message and exit the program
        elif roll.lower() == "no":
            print("Goodbye!")
            exit()
        # Else, output a message that says the input is invalid
        else:
            print("Invalid input! Please try again.")

# Roll function to randomly pick a number from 1 to 6, print the number generated and call the restart function
def roll_function(): 
    roll = random.randint(1, 6)
    print(f"The dice has landed on number {roll}") 
    restart()

# Restart function to ask the user if they would like to play again
def restart():
    # While loop to run continously until the conditions are met
    while True:
        roll_again = input("Would you like to play again? Yes/No: ")
        # If the user inputs "yes", then redirect to the roll function
        if roll_again.lower() == "yes":
            roll_function()
        # If the user inputs "no", then exit the program
        elif roll_again.lower() == "no":
            exit()
        # Otherwise, output a message that the input is invalid
        else:
            print("Invalid input! Please try again.")

# Call the intro function to start the program from the beginning.
intro_function()