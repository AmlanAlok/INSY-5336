# Prompts the user to enter the filename of a text file to be analyzed
input_filename = input('What is the filename: ')

# Open the file specified by input_filename in read-only mode and assign the file object to the variable file.
# Using the 'with' statement ensures that the file is properly closed after the block of code is executed
with open(input_filename, 'r') as file:
    # Read the contents of the file into the string variable data
    data = file.read()

    # Split the contents of the file into a list of lines using the newline character '\n',
    # and count the number of lines using the len() function
    line_count = len(data.split('\n'))

    # Split the contents of the file into a list of words using whitespace characters (including spaces, tabs, and newlines),
    # and count the number of words using the len() function
    word_count = len(data.split())

    # Count the number of characters in the file by applying the len() function directly to the string variable data
    char_count = len(data)

    # Split the contents of the file into a list of words using whitespace characters, create a list of the lengths of each word using a list comprehension,
    # and calculate the average length of a word by dividing the total length by the number of words
    total_length = sum([len(word) for word in data.split()])
    average_word_length = total_length / word_count

    # Print the results of the analysis to the console
    print('Number of lines:', line_count)
    print('Number of words:', word_count)
    print('Number of characters:', char_count)
    print(f'Average length of a word: {average_word_length:,.1f}')