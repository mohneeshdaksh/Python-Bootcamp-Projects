'''Love Calculator'''

from art import logo

print(logo)

print("The Love Calculator is calculating your score...\n")

name1 = input("What is your name? ")
name2 = input("What is their name? ")
combined_name = (name1 + name2).upper()

total_t = combined_name.count('T')
total_r = combined_name.count('R')
total_u = combined_name.count('U')
total_e = combined_name.count('E')
score_true = str(total_t + total_r + total_u + total_e)

total_l = combined_name.count('L')
total_o = combined_name.count('O')
total_v = combined_name.count('V')
total_e2 = combined_name.count('E')
score_love = str(total_l + total_o + total_v +total_e2)

score = int(score_true + score_love)

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
