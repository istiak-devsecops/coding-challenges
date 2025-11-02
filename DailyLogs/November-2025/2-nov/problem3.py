# creating a car class

class Car:
    def __init__(self, color, model, wheel_size, horse_power):
        self.color = color
        self.model = model
        self.wheel_size = wheel_size
        self.horse_power = horse_power

    def drive(self):
        return f"{self.color} {self.model} with {self.horse_power}hp engine is driving with its {self.wheel_size}inch tyre."
    
    def stop(self):
        return f"{self.color} {self.model} with {self.horse_power}hp engine has been stopped."

car1 = Car("red", "BMW", 18, 500)
print(car1.drive())
print(car1.stop())
