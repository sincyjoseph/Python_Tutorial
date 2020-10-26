
class Car:
    def __init__(self,enginename):
        print("Car created")
        self.number_of_wheels = 4
        self.engine = str(enginename)
        self.registration_number = ""
    def setRegistrationNumber(self,registrationNumber):
        self.registration_number = str(registrationNumber)
    def getRegistrationNumber(self):
        return str(self.registration_number)
    def start(self):
        print("Car get started")
    def move(self):
        print("Car moving")
    def stop(self):
        print("Car stopped")



toyota = Car("Toyo")
print(toyota.number_of_wheels)
print(toyota.engine)
toyota.setRegistrationNumber("KL599699")
#print(toyota.registration_number)
print(toyota.getRegistrationNumber())

toyota.start()
toyota.move()
toyota.stop()
