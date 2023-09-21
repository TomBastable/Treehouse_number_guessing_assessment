import random

#The below contains the high and low values for the game
#Changing these applies globally, no magic numbers are used.
LOW_VALUE = 1
HIGH_VALUE = 10

#A ten percent constant for readability
TEN_PERCENT = 0.1

#All of the messages used through the game

#The welcome and goodbye messages
WELCOME_MESSAGE = "Welcome to the number guessing game!"
GOODBYE_MESSAGE = "Thanks for playing, live long and prosper. \\//_"

#The messages used for guessing / handling guesses
GUESS_INPUT_MESSAGE = "Guess a number between {} and {}: "
OUT_OF_RANGE_MESSAGE = "Your guess is out of the specified range. Please try again."
WINNING_MESSAGE = "You guessed the number correctly in {} guesses!"
GUESS_ERROR_MESSAGE = "Please enter a * NUMBER * between {} and {}"
LOWER_MESSAGE = "It's lower"
HIGHER_MESSAGE = "It's higher"

#The messages used for the high score
HIGH_SCORE_MESSAGE = "The current high score is: {} - try and beat it!"
NEW_HIGH_SCORE_MESSAGE = "** You have a new high score of {}! **"

#The messages used for playing again
PLAY_AGAIN_MESSAGE = "Would you like to play again? (Y/N):   "
PLAY_AGAIN_ERROR_MESSAGE = "Please enter Y or N"
YES = "Y"
NO = "N"

#The file used to store the high score
HIGH_SCORE_FILE = "high_score.txt"

#Function to start the game
def start_game():

    #setup the key initial values
    high_score = load_high_score()
    current_guess_count = 0
    guessed_number = 0

    #print the current high score to give the user more energy..more passion
    print(HIGH_SCORE_MESSAGE.format(high_score))

    #generate the winning number
    winning_number = generate_winning_number(LOW_VALUE, HIGH_VALUE)

    #loop until the user guesses the number
    while guessed_number != winning_number:

        #ask for the user's guess
        guessed_number = get_guess(LOW_VALUE, HIGH_VALUE)

        #increment the guess count
        current_guess_count += 1

        #check if the user guessed the number
        if guessed_number == winning_number:

            #print the winning message, displaying the guess count
            print(WINNING_MESSAGE.format(current_guess_count))

            #check if the user has a new high score
            high_score = manage_high_score(current_guess_count, high_score)
            save_high_score(high_score)

            #ask the user if they want to play again
            if play_again():
                return
        
        else:
            #Indiana Jones style - You have chosen...poorly
            higher_or_lower_message = LOWER_MESSAGE if guessed_number > winning_number else HIGHER_MESSAGE
            print(higher_or_lower_message)

#Function to ask the user if they want to play again
def play_again():

    #loop until the user enters a valid choice
    while True:
        play_again_choice = input(PLAY_AGAIN_MESSAGE).strip().upper()
        if play_again_choice == YES:
            #restart the game
            start_game()
            return True
        elif play_again_choice == NO:
            #end the game
            print(GOODBYE_MESSAGE)
            return False
        else:
            #the user entered an invalid choice
            print(PLAY_AGAIN_ERROR_MESSAGE)

#Function to generate the winning number
def generate_winning_number(low, high):
    """
        This function generates a random number between the low and high values.

        I've made LOW_VALUE and HIGH_VALUE global constants, so that they can be changed easily.

    """
    return random.randint(low, high)

#Function to get the user's guess and handle any errors
def get_guess(low, high):

    #loop until the user enters a valid guess
    while True:
        try:
            #ask the user for their guess
            guessed_number = int(input(GUESS_INPUT_MESSAGE.format(low, high)))

            #check if the user's guess is within the range
            if low <= guessed_number <= high:
                #the user's guess is within the range
                return guessed_number
            else:
                #the user's guess is out of range
                print(OUT_OF_RANGE_MESSAGE)
        except ValueError:
            #the user entered something that wasn't a number
            print(GUESS_ERROR_MESSAGE.format(low, high))

#Function to load the high score from the file
def load_high_score():
    #check if the file exists
    try:
        #the file exists, so read the high score from it
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    except FileNotFoundError:
        #the file doesn't exist, so return the default high score
        return HIGH_VALUE - int(HIGH_VALUE * TEN_PERCENT)

#Function to save the high score to the file
def save_high_score(high_score):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(high_score))

#Function to manage the high score
def manage_high_score(current_score, high_score):
    #check if the user has a new high score
    if current_score < high_score:
        #the user has a new high score
        high_score = current_score
        #print the new high score message
        print(NEW_HIGH_SCORE_MESSAGE.format(high_score))
    return high_score

#And finally, start the game!
print(WELCOME_MESSAGE)
start_game()