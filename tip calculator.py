print("Welcome to tip calculator.")
bill = float (input("\nEnter the total bill: "))
tip = int (input ("\n Select your tip amount : 5%, 10%, 12% :"))
persons = int (input("\nHow many people would split the bill: "))

tipAmount= (tip/100)*bill

total_bill = bill + tipAmount
amount_per_person = total_bill / persons
rounded_bill=round(amount_per_person,2)

print("Each person should pay: " + str(rounded_bill))