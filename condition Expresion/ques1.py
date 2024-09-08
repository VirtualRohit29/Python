#write a program to find greatest of four no. entered by the user 
a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=int(input("enter the number: "))
d=int(input("enter the number: "))

if(a>b and a>c and a>d):
  print(f" greates no. is  :{a} ")

if(b>a and b>c and b>d):
  print(f" greates no. is  :{b} ")

if(c>d and c>a and c>b):
  print(f" greates no. is  :{c} ")

else:
  print( f" Greatest number is {d}")