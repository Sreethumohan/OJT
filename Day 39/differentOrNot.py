
#  Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def all_unique(sequence):
    return len(sequence) == len(set(sequence))

numbers = [1, 2, 3, 4, 5]
print(all_unique(numbers))  
numbers_with_duplicates = [1, 2, 3, 4, 5, 3]
print(all_unique(numbers_with_duplicates))  