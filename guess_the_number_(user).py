import random

low = int(input("Select a lower range to set a random number that you want to guess: "))
high = int(input("Select a upper range to set a random number that you want to guess: "))
def guess(x,y):
    random_num = random.randint(x,y)
    guess = int(input("Guess the number now: "))
    while guess != random_num:
        if(guess<random_num):
            guess = int(input("Low!! please guess again"))
        elif(guess>random_num):
            guess = int(input("High!! please guess again"))
    print(f"Congrats!! Your guess is correct and it was {guess}")
    
guess(low,high)
