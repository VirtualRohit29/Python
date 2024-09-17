# write a class "calculator" capable of finding sqi=uare , cube , and square root of a number 

class calculator:
    def __init__(self,n) :
       self.n=n
    def square(self):
        print(f"the square of {self.n} is : {self.n*self.n}")

    def cube(self):
        print(f"the cube of {self.n} is : {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"the square root of {self.n} is : {self.n**1/2}")  
    @staticmethod 
    def hello():
        print(" hello! user ")

a =calculator(3);
a.hello()
a.square()
a.cube()
a.squareroot()                  