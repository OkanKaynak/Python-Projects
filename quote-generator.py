# Import random library to pick a random quote from the list
import random
# Print a welcome message about the program
print("Welcome to the Quote Generator!")

# Method to ask the user if they would like to retrieve a quote and randomly printing a quote to the user
def quote_generator():
    # While loop running constantly until a condition is met
    while True:
        # Ask the user if they would like to retrieve a quote and store the input
        user_input = input("Would you like to retrieve a random quote? Yes/No: ")
        # If the input is yes, then randomly pick a quote from the quote list, print out the quote and then break out of the list.
        if user_input.lower() == "yes":
            quotes = ['Comparison is the theif of joy', 'Take the risk', 'Consistency is key', 'You learn more from lessons that wins', 'If it was easy, everyone would do it', 'Giving up is called failure', 'The pain of regret is bigger than the pain of failing']
            random_quote = random.choice(quotes)
            print("\nQuote: ", random_quote)
            break
        # If the user input no, then print goodbye message and exit the program
        elif user_input.lower() == "no":
            print("Goodbye!")
            exit()
        # Else, print invalid message to the user and to try again
        else:
            print("Invalid choice! Please try again.")
    # Call the restart method after this current method has been executed
    restart()

# Method to restart or exit the program
def restart():
    # While loop running constantly until a condition is met
    while True:
        # Ask the user if they would like to try again and store the input
        restart = input("\nWould you like to try again? Yes/No: ")
        # If the input is yes, then call the quote generator method to run through the process again
        if restart.lower() == "yes":
            quote_generator()
        # If the input is no, then print goodbye message and exit the program.
        elif restart.lower() == "no":
            print("Goodbye!")
            exit()
        # Else, print an invalid message to the user and to try again
        else:
            print("Invalid choice! Please try again.")
            
# Call the quote generator method to run the program from the start
quote_generator()