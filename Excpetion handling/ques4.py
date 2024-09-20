# write a programm to display a/b where a nad b are integers . if b=0 display infinite by handling the "Zero Division error "


a = int(input("enter the number a : "))
b = int(input("enter the number b : "))

if(b==0):
    raise ZeroDivisionError("hey our program is not meant to divide numbers by zeros")
else:
    print(f"the division of and b is :  {a/b} ")