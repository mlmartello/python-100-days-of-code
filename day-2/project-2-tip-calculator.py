print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

percentual_tip = (tip / 100 + 1)
amount = (bill / people) * percentual_tip
final_amount = round(amount, 2)

print(f"Each person should pay: ${final_amount}")
