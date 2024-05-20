#Write a Python program to reverse a list using a function.
def reverse_list(lst):
    return lst[::-1]
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(f"Original list: {original_list}")
print(f"Reversed list: {reversed_list}")