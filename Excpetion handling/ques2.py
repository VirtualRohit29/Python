# Write a programm to print third fifth and seventh element from alist using enumerant function 

l=[2,5,7,9,10,34,89,67]



for i, item in enumerate(l):
   if i == 2 or i == 4 or i == 6:
    print(i,item)
   