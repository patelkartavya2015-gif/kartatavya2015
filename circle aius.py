class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self, pi=3.14):
        return pi * (self.radius ** 2)
        

    def perimeter(self, pi=3.14):
        return 2 * pi * self.radius
    
c = circle(int(input("Enter radius of circle: ")))

print("Area of circle:", c.area())