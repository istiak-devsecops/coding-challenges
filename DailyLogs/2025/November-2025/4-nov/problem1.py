# inheritance 

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def running(self):
        return f"A {self.color} {self.name} is running on the street"
    

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Mouse(Animal):
    def sound(self):
        return "Sques!"


dog1 = Dog("scoobyDo", "grey")
cat1 = Cat("Tom", "blue")
mouse1 = Mouse("jerry", "red")

print(f"{dog1.running()} and making {dog1.sound()} sound")
        