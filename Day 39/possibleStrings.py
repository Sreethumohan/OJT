
#  Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.


import itertools

def generate_strings(letters):
    return [''.join(perm) for perm in itertools.permutations(letters)]

letters = ['a', 'e', 'i', 'o', 'I']
all_strings = generate_strings(letters)

for string in all_strings:
    print(string)
