n = int(input("Enter the number: "))

if n < 2:
    print("The number is not a prime number")
else:
    for i in range(2, n):
        if (n % i) == 0:
            print("The number is not a prime number")
            break
    else:
        # This else is aligned with the for loop, not the if statement
        print(f"{n} is a prime number")
