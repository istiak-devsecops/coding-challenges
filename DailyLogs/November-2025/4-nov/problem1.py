# inheritance 

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def running(self):
        return f"A {self.color} {self.name} is running on the street"
    

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

class Mouse(Animal):
    def sound(self):
        print("Sques!")


dog1 = Dog("scoobyDo", "grey")
cat1 = Cat("Tom", "blue")
mouse1 = Mouse("jerry", "red")

print(f"{dog1.running()} and making {dog1.sound()} sound")
        