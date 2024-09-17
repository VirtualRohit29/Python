# create a class programmer for storing information of few programmers working at microsoft 

class programmer:
    company="microsoft"
    def  __init__(self, name ,salary,pin):
       self.name=name
       self.salary=salary
       self.pin=pin 

p = programmer("rohit",120000,290704)
print(p.name,p.salary,p.company,p.pin )