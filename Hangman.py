import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def making_a_guess(guess, chosen_word, blank_list):
    correct_guess = False
    x = 0
    for letter in chosen_word:
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()
            correct_guess = True
        x += 1
    return correct_guess

def hangman_game():
    word = random.choice(someWords)
    chosen_word = list(word)
    
    blank = "_" * len(chosen_word)
    blank_list = list(blank)
    
    update_display = 0
    letterGuessed = ''
    chances = len(chosen_word) + 2
    correct = 0
    
    print('Guess the word! HINT: word is a name of a fruit')
    print(HANGMANPICS[update_display])
    print(''.join(blank_list))

    while chances > 0 and blank_list != chosen_word:
        guess = input(f"\nMake a guess? (Chances left: {chances}): ")

        if not guess.isalpha():
            print('Enter only a LETTER')
            continue
        elif len(guess) > 1:
            print('Enter only a SINGLE letter')
            continue
        elif guess in letterGuessed:
            print('You have already guessed that letter')
            continue
        else:
            letterGuessed += guess

        if making_a_guess(guess, chosen_word, blank_list):
            print("Correct guess!")
        else:
            print(f"There is no {guess}, sorry.")
            update_display += 1

        print(HANGMANPICS[update_display])
        print(''.join(blank_list))

        if blank_list == chosen_word:
            print("YOU WIN!")
            break

        chances -= 1
        if update_display == 6:
            print("GAME OVER.")
            print(f"The word was: {''.join(chosen_word)}")
            break

if __name__ == "__main__":
    hangman_game()
