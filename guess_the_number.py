import random

def guess_number(x):
    random_number = random.randint(1, x)
    guess = 0
    while random_number != guess:
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess < random_number:
            print("Guess was incorrect. Too low. Enter again.")
        elif guess > random_number:
            print("Guess was incorrect. Too high. Enter again.")
    
    print("Yay! You guessed the number correctly!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(H), too low(L) or correct(C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"The computer is right, the number is {guess} ")

computer_guess(25)

guess_number(25)