#BMI Calculator


def calculate_BMI(weight_kg,height_feet):
    user_height_meter = height_feet * 0.3048 #converting height from feet to meter
    BMI_Value = weight_kg / (user_height_meter**2) #BMI formula: Weight / height **
    return BMI_Value

def classify_BMI(BMI_Value):
    if BMI_Value < 18.5:
        return "Underweight!"
    elif 18.5 <= BMI_Value <= 24.9:
        return "Normal Weight"
    elif 25 <= BMI_Value <= 29.9:
        return "Overweight!"
    else:
        return "Obses!!"
           
def main():
    try:
        user_weight = float(input("What is your weight in kg: "))
        user_height = float(input("What is your height in feet: "))
        BMI = calculate_BMI(user_weight,user_height)
        category = classify_BMI(BMI)
        print (f"\n Your BMI is: {BMI:.2f}")
        print(f"Category:{category}")
    except ValueError:
        print("Please enter valid numeric values.")
if __name__ == "__main__":
    main()