def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def bmi():
    try:
        name = (input("Enter your name: "))
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
        else:
            bmi = calculate_bmi(weight, height)
            print(f"Your BMI is: {bmi:.2f}")
            category = interpret_bmi(bmi)
            print(f"You are categorized as: {category}")

            print("Thankyou! for Using Our BMI Calculator")

    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

bmi()
