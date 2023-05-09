# Import the 'random' module to shuffle words randomly
import random

# Ask the user to enter the name of the file containing words and their meanings
input_filename = input('Give the name of the “words and their meanings” file: ')


# Define a function 'word_meaning_dict' to create a dictionary of words and their meanings from a list of lines
def word_meaning_dict(lines):
    d = {}
    for line in lines:
        word_meanings = line.split(',')  # Split the line by comma to separate the word and its meaning
        k, v = word_meanings[0], word_meanings[1]  # Assign the word to k and its meaning to v
        d[k] = v  # Add the word and its meaning to the dictionary
    return d


# Define a function 'scramble_word' to shuffle the letters of a word randomly
def scramble_word(word):
    word_letters = list(word)
    random.shuffle(word_letters)  # Shuffle the letters randomly
    return ''.join(word_letters)  # Return the shuffled word as a string


# Ask the user if they want to play the game
user_choice = input('Do you want to play: ')

# Open the file containing words and their meanings, and split the data into lines
with open(input_filename, 'r') as file:
    data = file.read()
    lines = data.split('\n')
    file.close()

# Start the game while the user wants to play
while user_choice == 'Y':
    # Create a dictionary of words and their meanings from the lines of the file
    word_dict = word_meaning_dict(lines)
    # Create a list of words from the keys of the dictionary
    word_list = list(word_dict.keys())
    # Choose a random word from the list
    random_word = random.choice(word_list)
    # Scramble the letters of the random word
    display_word = scramble_word(random_word)

    # Ask the user to unscramble the shuffled word, and give them an option to ask for the meaning
    print('Unscramble the following letters to form a word. Type “?” for the meaning of the unscrambled word:',
          display_word)

    # Keep track of the number of times the user asks for the meaning of the word
    meaning_asked_count = 0

    # Keep track of the number of attempts the user makes to unscramble the word
    g = 0
    while g < len(display_word):
        # Ask the user to enter their answer or ask for the meaning of the word
        user_input = input('Enter the answer [or ? for the meaning]: ')

        # If the user asks for the meaning, give them the meaning and update the counter
        if user_input == '?':
            meaning_asked_count += 1
            if meaning_asked_count == 1:
                print('The word means: ', word_dict[random_word])
                continue
            elif meaning_asked_count == 2:
                print(
                    'You have been given the meaning before. Next time you ask for the meaning it will count as an attempt!')
                continue
            else:
                print('You ignored the warning. This will be counted as an attempt!')
        # If the user guesses the word correctly, congratulate them and end the game
        elif user_input == random_word:
            print('You got it!')
            break
        # If the user has exceeded the number of attempts, end the game
        elif g == len(display_word) - 1:
            print('Wrong, you have exceeded the number of attempts. Bye!')
            break
        else:
            # If the user's guess is wrong, prompt them to try again.
            print('Wrong, try again')

        # Increment the number of attempts.
        g += 1

    user_choice = input('\nDo you want to play: ')

print('Goodbye!')
