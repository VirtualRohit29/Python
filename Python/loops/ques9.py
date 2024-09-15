#write a program to print the following star pattern

#   ****
#   *  *
#   *  *
#   ****

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)  # Print the full line of stars on the first and last row
    else:
        print("*" + " " * (n - 2) + "*")  # Print stars with spaces in between for the middle rows

