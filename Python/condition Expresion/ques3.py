#  A spam comment is defined as a text containg followinf KEywords 
# "Make a lot of money"
# "Subscibe this "
# " Click this "

# write a program to detect these spams 

message = input("Enter your comment ")

p1="Make a lot of money"
p2= "Subscirbe this"
p3="Click this"

if((p1.lower() in message.lower()) or (p2.lower() in message.lower()) or (p3.lower() in message.lower())):
    print("This comment is Spam ")
else:
    print("this comment is not a spam ")     