# Write a python program to Delete a file
import os
def delete_file(file_name):
    try:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"Successfully deleted {file_name}")
        else:
            print(f"The file {file_name} does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")
 #(Created a file called dlt.txt ) 
file_name = 'dlt.txt' 
delete_file(file_name)
