#method 1:
'''
import random 
class train:
    
    def book(self,trainNo, FROM, TO):
        print(f"ticket is booked in train number: {trainNo} from {FROM} to {TO}")

    def getStatus(self,trainNo):
        print(f"train number: {trainNo} is running on time")

    def getFare(self,trainNo, FROM, TO ):
        print(f"Ticket is booked in train no:{trainNo} from {FROM} to {TO} is {random.randint(222,5555)}")
         
          
t = train()        
t.book("1234","Jalna","Nashik" )
t.getStatus("1234")
t.getFare("1234","Jalna", "Nashik")  '''          

#method 2:

import random #we can use here 'from random import randint' then we have to use 'randint(222,5555)' instead of 'random.randint(222,5555)'
class train:
    def __init__(self,trainNo): #we can use sel or anything instead of self no worries
        self.trainNo = trainNo

    def book(self, FROM, TO):
        print(f"ticket is booked in train number: {self.trainNo} from {FROM} to {TO}")

    def getStatus(self):
        print(f"train number: {self.trainNo} is running on time")

    def getFare(self, FROM, TO ):
        print(f"Ticket is booked in train no:{self.trainNo} from {FROM} to {TO} and sit number is {random.randint(222,5555)}")


t = train(1234)        
t.book("Jalna","Nashik" )
t.getStatus()
t.getFare("Jalna", "Nashik")
