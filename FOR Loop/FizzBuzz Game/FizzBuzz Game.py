# This program gives you a solution of FizzBuzz Game upto your desired number.
print("\nComplete FizzBuzz Solution!")
desired_end_number = int(input("\nEnter the number upto which you want FizzBuzz Solution for: "))
for number in range(1, desired_end_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)