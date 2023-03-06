import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
arrayLength = len(names)
randNum = random.randint(0, arrayLength - 1)
choice = names[randNum]
print(f"{choice} is going to buy the meal today!")
