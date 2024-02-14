import os
import sys
import random

def load_word_list(file_path):
    with open(file_path, 'r') as f:
        return [word.strip().lower() for word in f]

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def get_letter():
    while True:
        letter = input("\nGuess a letter: ").lower()
        if letter.isalpha() and len(letter) == 1:
            return letter
        print("Invalid input! Please enter a single letter.")

def play_game(word):
    guessed_letters = set()
    attempts = 6
    print(f"The word you need to guess has {len(word)} letters.")
    
    while attempts > 0:
        display = display_word(word, guessed_letters)
        print(display)
        
        if "_" not in display:
            print("You got it! Awesome.")
            return

        letter = get_letter()

        if letter in guessed_letters:
            print(f"You already guessed that letter. You still have {attempts} attempts left.")
        elif letter in word:
            guessed_letters.add(letter)
            print(f"Good guess! You still have {attempts} attempts left.")
        else:
            attempts -= 1
            guessed_letters.add(letter)
            print(f"Sorry, that letter is not in the word. You only have {attempts} attempts left")

    print(f"\nYou ran out of attempts. The correct answer is {word}.")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'Guess the Word'
    print(f'{"-" * 48}\n{" " * 12}{app_name}{" " * 12}\n{"-" * 48}')
    word_list = load_word_list('examples/09-guess-the-word/word_list.txt')
    word = choose_word(word_list)
    play_game(word)

    while True:
        response = input('\nDo you want to continue? (Y/N)')
        if response.lower() == 'y':
            word = choose_word(word_list)
            play_game(word)
        elif response.lower() == 'n':
            print('\nThank you and have a great day.\n')
            sys.exit()
        else:
            print('\nError: Please select Y or N.\n')

if __name__ == '__main__':
    main()
