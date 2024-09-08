# write a program to calculate the factorial of a given number using while loop 


n = int(input("enter the number : " ))
i=1
product=1
while(i<=n):
    product=product*i
    i=i+1

print(f"the factorial of  {n}  is : {product}")    