'''Title Casing'''
from art import logo
def format_name(first_name, last_name):
    '''Take a first and last name and format it to return 
    the title case version of the name.'''
    if first_name == "" or last_name == "":
        return "Invalid entry!"
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"{formatted_first_name} {formatted_last_name}"

print(logo)
given_name = input("What is your first name?\n")
family_name = input("Also, please provide me your last name:\n")

formatted_name = format_name(first_name=given_name, last_name=family_name)

print(formatted_name)
