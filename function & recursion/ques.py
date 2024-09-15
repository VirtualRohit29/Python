# write a program to using function to find greatest of three numbers 


def greates(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    

a = 2 
b = 4
c = 1

print("greatest number is  ",greates(a,b,c))

  