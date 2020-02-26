#!/usr/bin/python3.7

# Calcs the BMI from given user input
# Formula: weight in kg / heigt in meters^2

def gather_info():
    """
    Gathers the needed Info - system is optional
    """
    height=float(input("Your height: (inches or meters) "))
    weight=float(input("Your weight: (pounds or kilograms) "))
    system=input("Are your measurements in metric or imperial units? ").lower().strip()
    return (height, weight, system)

def calc_bmi(height,weight,system='metric'):
    """
    Returns the Body Mass Index (BMI) for
    the given weight, height and system.
    """
    bmi = (weight / (height ** 2 ))

    if system != 'metric':
        bmi = bmi * 703
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calc_bmi(height,weight,system)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calc_bmi(height,weight)
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Check input")
