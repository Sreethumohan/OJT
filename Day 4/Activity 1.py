#Write a Python program to Read/Write to a File 
def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print(f"Content of {file_name}:\n{content}")
    except Exception as e:
        print(f"An error occurred: {e}")
file_name = 'mytext.docx'
content = 'Hello, Welcome to Advanced Diploma In IT Networking and Cloud Computing! ~By NSTI(W) Trivandrum'
write_to_file(file_name, content)
read_from_file(file_name)
