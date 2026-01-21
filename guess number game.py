import random  #Importing the module to generate random number

#Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Can you guess it?")

while True:
    #Take user input
    guess = input("Enter your guess: ")

    #Check if input is a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)  #Convert to integer

    if guess == secret_number:
        print("Unbelievable! Congrats, you guessed the right number.")
        break 
    elif guess < secret_number:
        print("\/Too low. Try again.")
    else:
        print("/\Too high! Try again.")
