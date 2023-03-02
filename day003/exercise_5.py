# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

accumulator1 = 0
accumulator2 = 0

name1 = name1.lower()
name2 = name2.lower()

accumulator1 += name1.count("t")
accumulator1 += name2.count("t")
accumulator1 += name1.count("r")
accumulator1 += name2.count("r")
accumulator1 += name1.count("u")
accumulator1 += name2.count("u")
accumulator1 += name1.count("e")
accumulator1 += name2.count("e")

accumulator2 += name1.count("l")
accumulator2 += name2.count("l")
accumulator2 += name1.count("o")
accumulator2 += name2.count("o")
accumulator2 += name1.count("v")
accumulator2 += name2.count("v")
accumulator2 += name1.count("e")
accumulator2 += name2.count("e")

score = int(str(accumulator1) + str(accumulator2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
