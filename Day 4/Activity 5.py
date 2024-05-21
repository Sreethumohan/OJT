#Write a Python program with a function that converts a string to an integer.
# Handle exceptions within the function and print appropriate error messages.
def string_to_integer(s):
    try:
        result = int(s)
        print(f"The integer value is: {result}")
    except ValueError:
        print(f"Error: '{s}' is not a valid integer.")
    except TypeError:
        print(f"Error: The input '{s}' is not a string.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
string_to_integer("123")        
string_to_integer("abc")        
string_to_integer(123)         
string_to_integer("123.45")    
