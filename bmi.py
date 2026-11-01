def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/((height)**2)
    print("BMI = " + str(bmi))
    if (bmi < 18.5):
        return -1
    elif (18.5 <= bmi <= 25.0):
        return 0
    else:   
        return 1
    


bmi = calculate_bmi(weight=57, height=1.73)
if (bmi < 18.5):
    print("You are underweight")
elif (18.5 <= bmi <= 25.0):
    print("Your weight is normal")
else:   
    print("You are overweight")