# 4. Check if a key exists in a dictionary
kdict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
key_to_check = 'city'
if key_to_check in kdict:
    print(f"{key_to_check} exists in the dictionary.")
else:
    print(f"{key_to_check} does not exist in the dictionary.")