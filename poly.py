class ferrari():
    def fuelType(self, fuel):
        self.fuel = fuel
        return f"The Ferrari runs on {self.fuel}."
    
    def maxSpeed(self, speed):
        self.speed = speed
        return f"The maximum speed of the Ferrari is {self.speed} km/h."
    
class lamborghini():
    def fuelType(self, fuel):
        self.fuel = fuel
        return f"The Lamborghini runs on {self.fuel}."
    
    def maxSpeed(self, speed):
        self.speed = speed
        return f"The maximum speed of the Lamborghini is {self.speed} km/h."
    

obj1 = ferrari()
obj2 = lamborghini()

for car in (obj1, obj2):
    print(car.fuelType("petrol"))
    print(car.maxSpeed(350))