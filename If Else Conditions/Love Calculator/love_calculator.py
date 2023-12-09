'''Love Calculator'''

from art import logo

print(logo)

print("The Love Calculator is calculating your score...\n")

name1 = input("What is your name? ")
name2 = input("What is their name? ")
combined_name = (name1 + name2).upper()

t_count = combined_name.count('T')
r_count = combined_name.count('R')
u_count = combined_name.count('U')
e_count = combined_name.count('E')
score_true = str(t_count + r_count + u_count + e_count)

l_count = combined_name.count('L')
o_count = combined_name.count('O')
v_count = combined_name.count('V')
e_count2 = combined_name.count('E')
score_love = str(l_count + o_count + v_count + e_count2)

score = int(score_true + score_love)

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
