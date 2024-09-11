# write a recursive function to calculate the sum of first natural number

def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n


print("the sum of given number is ",sum(100))
    