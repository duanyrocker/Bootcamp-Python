# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
print("Welcome, to the tip calculator")
totalBill = float(input("What was the total bill? "))
percentage = int(input("What porcentage tip would you like tip give? 10, 12 or 15 "))
people = int(input("How many people to split the bill? "))
percentage = totalBill * percentage / 100
total = percentage + totalBill
total /= people
totalPeople = round(total, 2)
print(f"Each person should pay:{totalPeople}")