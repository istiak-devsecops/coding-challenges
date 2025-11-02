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
    

class Road:
    def __init__(self, road_type, road_len, color, model, wheel_size, horse_power):
        self.road_type = road_type
        self.road_len = road_len
        self.car_obj = Car(color, model, wheel_size, horse_power)

    def road_open(self):
        return f"In the {self.road_type} raod in {self.road_len}len a {self.car_obj.drive()}"
        

car1 = Road("Highway", "6", "red", "BMW", 18, 500)
print(car1.road_open())
