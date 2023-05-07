import re
import math

# function to add a word to a dictionary for a specific author
def add_word_in_dict(word, author_dict):
    # get list of all authors
    all_authors = list(author_dict.keys())

    # iterate over all authors
    for author in all_authors:
        # if the word is not already in the author's dictionary, add it with a value of 0
        if word not in author_dict[author]:
            author_dict[author][word] = 0

    # return the updated author dictionary
    return author_dict

# function to calculate cosine similarity between two dictionaries
def cos_similarity(dict_A, dict_B):
    # get list of all keys (words) in the dictionaries
    all_keys = list(dict_A.keys())
    ab_sum = 0

    # iterate over all keys and add the product of the values for that key in both dictionaries to ab_sum
    for k in all_keys:
        ab_sum += dict_A[k] * dict_B[k]

    a_sqr, b_sqr = 0, 0

    # iterate over all keys and add the squares of the values for that key in each dictionary to a_sqr and b_sqr, respectively
    for k in all_keys:
        a_sqr += dict_A[k] * dict_A[k]
        b_sqr += dict_B[k] * dict_B[k]

    # calculate the square root of a_sqr and b_sqr
    a_mod = math.sqrt(a_sqr)
    b_mod = math.sqrt(b_sqr)

    # calculate the cosine similarity using the formula and return the result
    cos_similarity = ab_sum / (a_mod * b_mod)
    return cos_similarity

# function to organize the data by author and poem
def organise_data():
    # iterate over all poems in the poems list
    for poem in poems:
        # split the poem by the author and the poem data
        poem_structure = poem.split(':')
        poem_author, poem_data = poem_structure[0], poem_structure[1]
        # split the poem data by /
        poem_lines = poem_data.split('/')

        # add the poem data to the original_dict dictionary using the author as the key
        original_dict[poem_author] = poem_data
        # create a new dictionary for the author in the author_dict dictionary
        author_dict[poem_author] = {}

        # add the author and poem lines as a list to the temp list
        temp.append([poem_author, poem_lines])

# A function to create word frequency dictionaries for all authors
def create_dict_vectors():
    for data in temp:
        poem_author, poem_lines = data[0], data[1]

        for line in poem_lines:
            cleaned_line = re.sub(r'[^a-zA-Z ]', '', line) # Remove all non-alphabetic characters
            words = cleaned_line.split() # Split the line into words
            for word in words:
                word_lower = word.lower() # Convert the word to lowercase
                if word_lower not in author_dict[poem_author]:
                    add_word_in_dict(word_lower, author_dict) # Add the word to the author's dictionary
                author_dict[poem_author][word_lower] += 1 # Increment the count for the word

# A function to find the poem with the closest cosine similarity to the input poem
def find_closest_poem():
    authors = list(author_dict.keys())
    cos_max = 0
    max_similar_author = ''

    # Iterate over all authors
    for author in authors:
        if author != your_author_name:
            # Calculate the cosine similarity between the input poem and the current author's poems
            cos_similarity_val = cos_similarity(author_dict[author], author_dict[your_author_name])
            print(author + ':' + str(cos_similarity_val))
            # Update the maximum cosine similarity and the most similar author
            if cos_similarity_val > cos_max:
                cos_max = cos_similarity_val
                max_similar_author = author

    # Print the most similar poem
    print('The closest poem is:')
    print(max_similar_author + ':' + original_dict[max_similar_author])

# Ask the user to input the name of the file that contains all the poems
input_filename = input('Give the name of the poetry file: ')

# Ask the user to input their poem, with each line separated by "/"
your_poem = input('Input your poem delineated by “/” for each line: ')

# Open the file that contains all the poems
with open(input_filename, 'r') as file:
    data = file.read()
    file.close()

# Split the data into individual poems using newline as the delimiter
poems = data.split('\n')

# Set the author name for the user's poem
your_author_name = 'Me'

# Initialize the author dictionary with the user's poem
author_dict = {your_author_name: {}}

# Initialize a temporary list to store each poem's author and lines
temp = [[your_author_name, your_poem.split('/')]]

# Initialize an empty dictionary to store the original poem data for each author
original_dict = {}

# Organize the data into the appropriate data structures
organise_data()

# Create the dictionary vectors for each author
create_dict_vectors()

# Find the closest poem to the user's poem
find_closest_poem()