print(""" _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|\n""")

# Define operations
def add(n1, n2): return n1 + n2
def sub(n1, n2): return n1 - n2
def mul(n1, n2): return n1 * n2
def div(n1, n2): return n1 / n2 if n2 != 0 else "Error: Divide by zero"

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

# Calculator function
def calc():
    n1 = float(input("What's the first number: "))
    should_continue = True

    while should_continue:
        op = input("Pick an operation (+, -, *, /): ")
        n2 = float(input("What's the next number: "))
        
        if op in operations:
            result = operations[op](n1, n2)
            print(f"{n1} {op} {n2} = {result}")
        else:
            print("Invalid operation. Try again.")
            continue

        choice = input(f"Type 'y' to continue with {result}, or 'n' to start a new calculation: ")

        if choice.lower() == 'y':
            n1 = result
        else:
            should_continue = False
            print("\n" * 20)
            calc()  
calc()
