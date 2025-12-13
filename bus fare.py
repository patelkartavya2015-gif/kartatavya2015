class vehicle:
    def __init__ (self, vehicleName , fare):
        self.vehicleName = vehicleName
        self.fare = fare
    
    def displayFare(self):
        return f"The fare for {self.vehicleName} is {self.fare}."
    
class bus(vehicle):
    def __init__ (self, vehicleName, fare, routeNumber):
        super().__init__(vehicleName, fare)
        self.routeNumber = routeNumber
    
    def displayRoute(self):
        return f"The route number for {self.vehicleName} is {self.routeNumber}."
    
bus1 = bus("City Bus", 2.5, "22B")
print(bus1.displayFare())
print(bus1.displayRoute())