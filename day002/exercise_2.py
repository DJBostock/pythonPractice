# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

hgt = float(height)
wgt = float(weight)
bmi = wgt / (hgt * hgt)
bmi = int(bmi)

print(bmi)
