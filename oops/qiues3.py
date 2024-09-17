# create a class with class attribute a ; create an object from it and set a directly using object.a =0 . does this changes the class attribute 

class object:
    a=4

o=object()
print(o.a)
o.a=5
print(o.a)
print(object.a) # it print 4 means instances attribute does not changes the class attribute 
