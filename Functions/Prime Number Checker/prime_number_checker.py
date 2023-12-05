'''Prime Number Checker'''
def prime_checker(number):
    '''Main function that checks whether the number (input) is prime.'''
    if number > 1:
        count = 0
        for divisor in range(2,number):
            modulo = number % divisor
            if modulo == 0:
                count += 1
        if count > 0:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")
    else:
        print("It's not a prime number.")

print("Welcome to the Prime Number Checker!")
n = int(input("Enter a number: "))
prime_checker(number=n)
