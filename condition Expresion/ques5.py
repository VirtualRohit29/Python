#write a program to calculate a grade of a student from his marks from the following scheme 
# 90-100 ==>Ex
# 80-90 ==>A
# 70-80 ==>B
# 60-70 ==>C
# 50-60 ==>D
# less than 50 ==>FAIL

marks=int(input("enter the number"))

if(marks<=100 and marks>=90):
    print("Your grade is : Ex")
    
elif(marks<90 and marks>=80):
    print("Your grade is : A") 

elif(marks<80 and marks>=70):
    print("Your grade is : B") 

elif(marks<70 and marks>=60):
    print("Your grade is : C")

elif(marks<60 and marks>=50):
    print("Your grade is : D") 

else:
    print("you have Failed!")                 