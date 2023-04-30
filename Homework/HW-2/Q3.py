import re
import math



def add_word_in_dict(word, author_dict):
  all_authors = list(author_dict.keys())

  for author in all_authors:
    if word not in author_dict[author]:
      author_dict[author][word] = 0

  return author_dict


def cos_dist(dict_A, dict_B):

    all_keys = list(dict_A.keys())

    ab_sum = 0

    for k in all_keys:
        ab_sum += dict_A[k] * dict_B[k]

    a_sqr, b_sqr = 0, 0

    for k in all_keys:
        a_sqr += dict_A[k] * dict_A[k]
        b_sqr += dict_B[k] * dict_B[k]

    a_mod = math.sqrt(a_sqr)
    b_mod = math.sqrt(b_sqr)

    cost_distance = ab_sum/(a_mod*b_mod)

    return cost_distance


# input_filename = input('Give the name of the poetry file: ')
input_filename = 'poetry_lines.txt'

# your_poem = input('Input your poem delineated by “/” for each line: ')
your_poem = 'Whose forest are these I know./He lives in the village/He has no idea I am looking at his property/and seeing the forest fill up with snow.'


with open(input_filename, 'r') as file:
    data = file.read()

poems = data.split('\n')

your_author_name = 'Me'
author_dict = {your_author_name: {}}
temp = [[your_author_name, your_poem.split('/')]]

for poem in poems:
  poem_structure = poem.split(':')
  # print(poem_structure)
  poem_author, poem_data = poem_structure[0], poem_structure[1]
  poem_lines = poem_data.split('/')

  author_dict[poem_author] = {}

  temp.append([poem_author, poem_lines])
  # print(poem_author)
  # print(poem_lines)

for data in temp:
    poem_author, poem_lines = data[0], data[1]

    for line in poem_lines:
        cleaned_line = re.sub(r'[^a-zA-Z ]', '', line)
        # print(cleaned_line)
        words = cleaned_line.split()
        # print(words)
        for word in words:
            word_lower = word.lower()
            if word_lower not in author_dict[poem_author]:
                add_word_in_dict(word_lower, author_dict)
            author_dict[poem_author][word_lower] += 1

    # print('---')

# print(author_dict)

# all_authors = list(author_dict.keys())
# for author in all_authors:
#     print(len(author_dict[author]))

authors = list(author_dict.keys())

for author in authors:
    if author != your_author_name:
        cos_dist_val = cos_dist(author_dict[author], author_dict[your_author_name])
        print(author + ':' + str(cos_dist_val))


