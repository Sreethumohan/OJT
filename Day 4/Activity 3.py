#Write a Python program that renames a file named ‘old_name.txt to’ ‘new_name.txt’.
import os
def rename_file(old_name, new_name):
    try:
        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print(f"Successfully renamed {old_name} to {new_name}")
        else:
            print(f"The file {old_name} does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")
old_name = 'mytext.docx'  
new_name = 'welcome.docx'  
rename_file(old_name, new_name)
