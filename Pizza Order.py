print("Welcome to Pizza Delivery")

size = input("Select pizza size: S M L : ")
pepperoni = input("Do you want pepperoni on your pizza: ")
cheese =  input("Do you want extra cheese on your pizza: ")

price = 0

if size == 'S':
    price = 15
elif size == 'S' and pepperoni == 'Y':
    price = price+2

if size == 'M':
    price = 20

if size == 'L': 
    price = 25
elif size == 'M' or size =="L" and pepperoni == 'Y':
    price = price+3    

if cheese == 'Y':
    price = price + 1

print("Your total amount is " + str(price))