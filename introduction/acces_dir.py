# write a programm to print the contents of a directory using os module 
import os

def print_directory_contents(directory_path):
    try:
        # List all the files and directories in the given directory
        with os.scandir(directory_path) as entries:
            for entry in entries:
                # Check if it's a file or directory and print its name
                if entry.is_file():
                    print(f'File: {entry.name}')
                elif entry.is_dir():
                    print(f'Directory: {entry.name}')
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory_path}'.")

# Replace 'your_directory_path' with the path of the directory you want to list
directory_path = 'C:/Users/rohit/OneDrive/Desktop/python'
print_directory_contents(directory_path)







