# A basic program which uses knowledge of Functions with Outputs and Docstrings.

def format_name(first_name, last_name):
    """Take a first and last name and format it to return 
    the title case version of the name."""
    if first_name == "" or last_name == "":
        return "Invalid entry!"
    else:
        formatted_first_name = first_name.title()
        formatted_last_name = last_name.title()
        return f"{formatted_first_name} {formatted_last_name}"

print("""
`... `......     `..   `..               `..                              
     `..     `.  `..   `..            `..   `..                           
     `..       `.`. `. `..   `..     `..          `..     `....    `..    
     `..    `..  `..   `.. `.   `..  `..        `..  `.. `..     `.   `.. 
     `..    `..  `..   `..`..... `.. `..       `..   `..   `... `..... `..
     `..    `..  `..   `..`.          `..   `..`..   `..     `..`.        
     `..    `..   `.. `...  `....       `....    `.. `...`.. `..  `....   
""")
given_name = input("What is your first name?\n")
family_name = input("Please provide me your last name as well:\n")

formatted_name = format_name(first_name=given_name, last_name=family_name)

print(formatted_name)