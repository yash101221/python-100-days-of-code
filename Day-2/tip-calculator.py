print("Tip Calculator")

billAmount = float(input("Enter the amount of bill:\n"))
tipPercentage = float(input("Enter the Percentage you want to tip of bill amount:\n"))
totalMembers = int(input("Enter the total members : \n"))

tip_amount = billAmount * (tipPercentage / 100)
total_bill_amount = billAmount + tip_amount

amount_per_person = total_bill_amount / totalMembers

print(f"Total bill amount (including tip): {total_bill_amount:}")
print(f"Each person should pay: {amount_per_person:}")
