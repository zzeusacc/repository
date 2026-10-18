#task16
score = int(input("Enter your score: "))
print("Pass") if score >= 50 else print("Fail")
#task17
total = float(input("Enter your total: "))
print(delivery = 0 AZN) if total >= 50 else print(delivery = 5 AZN)
membership = input("do you have a membership? (yes/no)")
final total = total + delivery
#task18
number = int(input("enter a number"))
match number:
    case 1:
        print("monday/study day")
    case 2:
        print("tuesday/study day")
    case 3:
        print("wednesday/study day")
    case 4:
        print("thursday/study day")
    case 5:
        print("friday/study day")
    case 6:
        print("saturday/the weekend")
    case 7:
        print("sunday/the weekend")
    case _:
        print("invalid day")
#task19

order = input("enter your order(T(tea)/C(coffe)/J(juice))")
T = 2
C = 4
J = 3
quantity = int(input("enter the quantity(1-10)"))
if quantity<10:
    print("invalid quantity")
match order:
    case "T":
        total = T*quantity
        print(f"your order is {quantity} tea and total is {total} AZN")
    case "C":
        total = C*quantity
        print(f"your order is {quantity} coffe and total is {total} AZN")
    case "J":
        total = J*quantity
        print(f"your order is {quantity} juice and total is {total} AZN")
    case _:
        print("invalid order")

