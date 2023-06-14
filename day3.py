# height = int(input("height: "))

# if height == 170:
#     print("You are taller")
# else:
#     print("You aren't taller")

# a = input("Nhập 1 số bất kỳ:  ")

# if int(a)%2 == 0:
#     print("Số chẵn")
# else:
#     print("Số lẻ")

# weight = float(input("weight: "))
# height = float(input("height: "))
# bmi = round(weight/height ** 2)

# if bmi < 18.5:
#     print(f"Your bmi is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"Your bmi is {bmi}, you have a normal weight")
# elif bmi < 35:
#     print(f"Your bmi is {bmi}, you are obese")
# else:
#     print(f"Your bmi is {bmi}, you are clinically obese.")

print("Welcome to Python Pizza:")
size = input("What size pizza do you want? S, M, or L  ")
add_pepperoni = input("Do you want pepperoni? Y or N  ")
extra_cheese = input("Do you want extra cheese? Y or N  ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")