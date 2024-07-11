
# Write a Python program that removes and prints every third number from a list of numbers until the list is empty.


def remove_every_third(numbers):
    index = 2  
    while len(numbers) > 0:
        print(numbers.pop(index))
        if len(numbers) == 0:
            break
        index = (index + 2) % len(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_every_third(numbers)
