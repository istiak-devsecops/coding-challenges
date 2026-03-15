products = {
    "Laptop": 750,
    "Mouse": 25,
    "Keyboard": 50,
    "Monitor": 200,
    "Phone": 600,
    "Headphones": 120
}

maxinp = int(input("What will be the max range: "))
mininp = int(input("What will be the min range: "))


pro_list = {}

for name, price in products.items():
    if mininp <= price <= maxinp:
        pro_list[name] = price

print(pro_list)
        


