print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_amount = tip / 100
total_tip_amount = bill * tip_amount
total_amount = bill + total_tip_amount
split_amount = total_amount / people
final_amount = round(split_amount, 2)
print(f"Each person should pay: ${final_amount}")
