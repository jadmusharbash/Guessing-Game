import random

def guess_number(target): # If statements (is it Increase or Decrease)
    while True:
        guess = int(input("Guess a number: "))
        if guess < target:
            print("Increase")
        elif guess > target:
            print("Decrease")
        else:
            print("Congrats! You found the number.")
            break

if __name__ == "__main__":
    target_number = random.randint(1, 50)  # Number range
    print("The Number Guessing Game!")
    guess_number(target_number)