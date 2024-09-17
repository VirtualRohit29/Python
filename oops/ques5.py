 #write a class train which has methods to booklmticket , gert status (no.of seats ) nand get afre information of training under indian railway
from random import randint
class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
     print(f"Ticket is booked in train no {self.trainNo} from {fro} to {to}")

    def getfare(self,fro,to):
     print(f"Ticket fare of   train no. {self.trainNo} from {fro} to {to} is {randint(300, 4000)}") 

    def getstatus(self):
     print(f"Ticket is running on time  in train no. {self.trainNo} ")  


t =train(290704)

t.book("delhi","bhopal")
t.getfare("delhi","bhopal")
t.getstatus()