def format_name(first_name,last_name):
    if first_name == "" and last_name == "":
        return "No value provided." 
    formated_f_name=first_name.title()
    formated_l_name=last_name.title()
    print(f"Result: {formated_f_name} {formated_l_name}")

format_name(input("Enter your first name: "),input("Enter your last name: "))