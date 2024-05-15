print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? Rs "))
tip = int(input("How much tip would you like to give? 10,12, or 15? "))
bill_split = int(input("How many people to split the bill? "))
tip_percent = total_bill * (tip/100)
bill_with_tip = total_bill + tip_percent
bill_share = bill_with_tip / bill_split
print(f"Each person should pay: Rs {round(bill_share,2)}")