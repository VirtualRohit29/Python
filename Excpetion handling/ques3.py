# write a list comprehension to print alisrt which contains the multiplication table of a user entered a numbeer


n=5
table = [ n*i for i in range(1,11)]
# print (table)

with open("file.txt","a")as f:
    f.write(f"table of {n} is : {str(table)}\n")