# Import the random library to generate random numbers
import random

def intro_function():
    # Output a message about the game and the levels the user can play
    print("Welcome to Guess the Number Game")
    print("These are the following levels for the game:")
    print("Level 1 = 10 numbers \nLevel 2 = 20 numbers \nLevel 3 = 50 numbers \nLevel 4 = 100 numbers")
    # Set the level chosen to false so the while loop can be executed
    level_chosen = False
    # Set a while loop to let the user select a level
    while level_chosen == False:
        # Store the level number input by the user
        level_choice = input("Input the number for the level you would like to select: ")
        # Set the level variable
        level = 0
        # Set the level chosen as true to prevent repeating for each if statement when the level is chosen
        level_chosen = True

        # If the number input matches the level descriptions, then set the level variable to the number that random number generator can choose up to
        if level_choice == "1":
            level = 10
        elif level_choice == "2":
            level = 20
        elif level_choice == "3":
            level = 50
        elif level_choice == "4":
            level = 100
        # Else, output a message that the input is incorrect and to try again as well as setting the level chosen to false for the while loop to execute again
        else:
            print("Incorrect level. Please try again.")
            level_chosen = False
    return level

def main_function(level):
    # Set the random number to a global variable
    random_num = random.randint(1, level)
    # Store the number of attempts in a global variable
    attempts = 0
    # Set the number guessed variable to false for the while loop to run based on a condition for this variable
    number_guessed = False
    # While loop runs constantly until the variable number guessed is set to true
    while number_guessed == False:
        # Store the input based on the response to the task output to the user
        user_guess = input(f"Guess a number between 1 and {level}: ")
        # If the user input is not a digit, then ask the user to enter a valid number and continue on with the loop
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        # Convert the input from string to an integer to make calculations with
        user_guess = int(user_guess)
        # Increment the attempts variable by 1
        attempts += 1
        # If the user guess is less than the random number, then display that the guess is too low and to try again
        if user_guess < random_num:
            print("Too low. Try again.")
        # If the user guess is more than the random number, then display that the guess is too high and to try again
        elif user_guess > random_num:
            print("Too high. Try again.")
        # Else, the guess matches the random number and display a congratulations message with the number of attempts it took and breaks out of the loop
        else:
            print(f"Well Done! You guessed the number in {attempts} attempts.")
            number_guessed = True
            
# Set a variable to true while the game is running for the while loop to run continuously
game_active = True
while game_active == True:
    # Call the intro and main functions with the levels to chose and selected
    level = intro_function()
    main_function(level)
    # While the loop is true (until broken)
    while True:
        # Ask the user if they would like to play again and store the input
        play_again = input("Would you like to play again? Yes/No: ")
        # If the input is Yes, then break teh loop
        if play_again == "Yes":
            break
        # Else if the input is No, then print a thank you message, set the game_active variable to false and break out the loop
        elif play_again == "No":
            print("Thank you for playing!")
            game_active = False
            break
        # Else print invalid choice until the user enters a valid input
        else:
            print("Invalid choice. Please try again.")
        
        
