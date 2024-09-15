# write a recursive function to first n lines of the following pattern

def printstar(n):
    if(n==0):
        return
    print("*"*n)
    printstar(n-1)




print(printstar(5))    