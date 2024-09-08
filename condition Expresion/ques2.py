# write  program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass . Assume 3 subjects and take marks as an input from the user 

English = int(input(" Enter the marks of english : "))
Maths = int(input(" Enter the marks of english : "))
Science = int(input(" Enter the marks of english : "))

total=((English+Maths+Science)/300)*100
if(total>=40 and English>=33 and Maths>=33 and Science>=33):
    print("you have passed ")

else:
    print("you have failed ")    