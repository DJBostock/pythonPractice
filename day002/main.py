print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

bill_per_person = ((tip_percentage/100) + 1) * total_bill / number_of_people

print(f"Each person should pay: ${bill_per_person:.2f}")
