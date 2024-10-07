import words
import random
import string
words = words.words
from colorama import Fore, Style

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:  
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    i = 1;
    while  len(word_letter)!= 0:
        if len(word) > i:
            print(f"{Fore.GREEN}{len(word)*3 - i+1} tries left{Style.RESET_ALL}")
        elif  len(word)*2 > i:
            print(f"{Fore.YELLOW}{len(word)*3 - i+1} tries left{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}{len(word)*3 - i+1} tries left{Style.RESET_ALL}")
    
        i +=1
        print("You have used these letter: ",' '.join(used_letter))
        current_letter  = [letter if letter in used_letter else '_' for letter in word]
        print("Your current word is: ",' '.join(current_letter))
        input_letter = input("\n Guess a letter: ")
        if input_letter in used_letter:
            print("\nYou have already used this letter. Please try again.")
            continue
            
        if input_letter not in alphabet - used_letter:
            used_letter.add(input_letter)
    
            if input_letter in word_letter:
                word_letter.remove(input_letter)

        if i > len(word)*3:
            print(f"\n\nYou failed to guess the word. It was {Fore.RED}{word}{Style.RESET_ALL}")
            break

    if len(word_letter) == 0:
        print(f"\n\nCongrats!! you have succeeded in guessing the word {Fore.GREEN}{word}{Style.RESET_ALL}")


hangman()
