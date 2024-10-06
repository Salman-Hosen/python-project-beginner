import random

def play():
    you = input("Please make your choice. 'R' for Rock, 'P' for paper and 'S' for scissor").lower()
    if you not in ['r','p','s']:
        return "Invalid input!! Please choose R, P or S"
    computer = random.choice(["r","p","s"]);
    print(f"Your choice is {you}")
    print(f"Computer choice is {computer}")    
    if(you == computer):
        return "Your game is TIE"
    elif is_win(you,computer):
        return "Congrats!! You Won the game"
    return "You lost the game"

def is_win(you,computer):
    # p>r, r>s, s>p
    return (you == "p" and computer == "r") or (you == "r" and computer == "s") or (you == "s" and computer == "p") 

print(play())
