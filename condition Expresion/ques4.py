# write  a program to find whether a ginen username contains less than 10 characters or not and also find whethere a given name in list or not 

l=["harry" , "rohit", "mukhesh", "suykesh"]
name=input(" enter your anme ")

if(len(name)<10):
    print("your name contains less than 10 character ")

else:
    print("aLL is good ")

if(name in l):
    print("your name is in the list")

else:
    print("your name is not is the list ")            