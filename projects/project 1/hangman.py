import functions as fc
import random

fc.clear_screen()

no_of_tries = 6
guess = False
letters_guessed = []
letters_failed = []
played_letters = []
tries = 0

# Create list of available words and pick a random word.
# For now this is stored in a .txt file. but can be improved in the future
try:
    words_file = open('words.txt', 'r')
except:
    print("Word file not found. Please place words.txt with words in the root of the game.")
    exit()

words = [line.strip() for line in words_file]

if len(words) == 0:
    raise ValueError("No words to choose from")

word = list(random.choice(words).lower())

# Keep asking user for input until guess or excedeed number of tries
while tries < no_of_tries and not guess:
    fc.clear_screen()
    print("========== H A N G M A N ==========\n")
    missing, word_so_far = fc.word_so_far(word, letters_guessed)
    print("Word to guess:", word_so_far, "\n")
    fc.draw_hangman(tries)
    if len(letters_failed) > 0:
        print("You already missed: ", ' '.join(letters_failed).upper())
    letter = fc.ask_letter_user(played_letters)
    if letter in word:
        letters_guessed.append(letter)
    else:
        letters_failed.append(letter)
        tries += 1
    played_letters.append(letter)
    missing, word_so_far = fc.word_so_far(word, letters_guessed)

    if missing:
        guess = False
    else:
        guess = True

fc.clear_screen()
print("========== H A N G M A N ==========\n")
missing, word_so_far = fc.word_so_far(word, letters_guessed)
print("Word to guess:", word_so_far, "\n")
fc.draw_hangman(tries)
if guess:
    print("YOU WIN!")
else:
    print("YOU LOSE")
    print("The word was:", ''.join(word))
