# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
resultado = round(weight / height ** 2)
if resultado < 18.5:
    print(f"Underweight: {resultado}")
elif resultado < 25:
    print(f"Normal weight: {resultado}")
elif resultado < 30:
    print(f"Slightly overweight: {resultado}")
elif resultado < 35:
    print(f"Obese: {resultado}")
else:
    print(f"Clinically Obese: {resultado}")