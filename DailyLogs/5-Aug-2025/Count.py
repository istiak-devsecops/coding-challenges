# BMI calcilator

def BMI(weight, height):
    BMI_Value = weight / (height**2)
    return BMI_Value

def weight_class(BMI_Value):
    if BMI_Value < 18.5:
        return "underweight"
    elif 18.5 <= BMI_Value <= 29.9:
        return "Healthy Weight"
    else:
        return "Over weight"

def main():
    user_weight = float(input("Write your weights in kg: "))
    user_height = float(input("Write your height in feet: "))
    user_height_meter = user_height * 0.3034
    
    BMI_result = BMI(user_weight, user_height_meter)
    weight_class_result = weight_class(BMI_result)
    print(f"You BMI is: {BMI_result}")
    print(f"Your Weight class is: {weight_class_result}")

if __name__ == "__main__":
    main()