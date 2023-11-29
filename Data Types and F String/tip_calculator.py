'''Tip Calculator to calulate bill share per person including the desired tip'''

print("Welcome to the Tip Calculator!")
total_bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? Eg. 10, 15, etc")
total_people = input("How many people are going to split the bill? ")
per_person_share = float(total_bill) / float(total_people)
percent_increase = 1 + (float(tip_percent)/100)
per_person_tip = per_person_share * percent_increase
final_share = format(per_person_tip, ".2f")
print(f"Each person should pay: ${final_share}")
