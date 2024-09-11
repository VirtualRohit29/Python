#write a program to find the sum of first n natural numbers using while loop

n = int(input("enter the number : " ))
i=0
sum=0
while(i<=n):
    sum=sum+i
    i=i+1

print(f"the sum of first {n} natural no. is : {sum}")    