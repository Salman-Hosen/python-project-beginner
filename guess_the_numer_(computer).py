import random

print("Please think of a number in your mind that you want the computer to guess.")
low = int(input("Now set a lower range for the computer to guess: "))
high = int(input("Now set an upper range for the computer to guess: "))

def guess_by_pc(low, high):
    while True:
        guess_num = random.randint(low, high)
        judge = input(f"The computer guesses {guess_num}. Please type 'H' if the guess is too high, 'L' if it's too low, or 'C' if it's correct: ").lower()

        if judge == 'c':  # Exit the loop if the guess is correct
            print(f"The computer guessed the number correctly! The number is {guess_num}.")
            break
        elif judge == 'h': 
            high = guess_num - 1
        elif judge == 'l':  
            low = guess_num + 1


guess_by_pc(low, high)
