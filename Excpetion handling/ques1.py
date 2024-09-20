try:
     with open("file1.txt","r") as f1:
         print(f"Contents of file1.txt:\n{f1.read()}\n")
except Exception as e:
    print(f"An unexpected error occurred: {e}")         
try:         
      with open("file2.txt","r") as f2:
         print(f"Contents of file1.txt:\n{f1.read()}\n")
except Exception as e:
    print(f"An unexpected error occurred: {e}")         
try:         
    with open("file3.txt","r") as f3:
         print(f"Contents of file3.txt:\n{f3.read()}\n")
except Exception as e:
    print(f"An unexpected error occurred: {e}")        
        

# except FileNotFoundError as e:
    # print(f"Error: {e}")


print("Thank you!")
