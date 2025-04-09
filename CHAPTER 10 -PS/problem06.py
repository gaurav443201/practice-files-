from random import randint
class train:
    def __init__(harry,trainNo):
        harry.trainNo = trainNo

    def book(slf, FROM, TO):
        print(f"ticket is booked in train number: {slf.trainNo} from {FROM} to {TO}")

    def getStatus(mc):
        print(f"train number: {mc.trainNo} is running on time")

    def getFare(harry, FROM, TO ):
        print(f"Ticket is booked in train no:{harry.trainNo} from {FROM} to {TO} and sit number is {randint(222,5555)}")


t = train(1234)        
t.book("Jalna","Nashik" )
t.getStatus()
t.getFare("Jalna", "Nashik")