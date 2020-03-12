import re
from os import system, name


def ask_letter_user(exclude_list):
    # ask user for input. Input should only be Letters. Either Upper or lower Case.
    # only returns lower case and after validation.
    # Validations: Letter, already played

    letter = False
    while not letter:
        hunch = input("Choose one letter: ")
        if re.search('[A-Za-z]', hunch) is not None:
            if hunch in exclude_list:
                print("You already tried that one.")
            else:
                letter = hunch
        else:
            print("Not quite right. Let's try that again.")
    return letter.lower()


def word_so_far(word, letters_guessed):
    # Iterate through the full word.
    # If letter is in the guessed list replace _ with letter.
    # If still missing letters return missing = true

    result = ""
    missing = False
    for w in word:
        if w in letters_guessed:
            result += w.upper()
        else:
            result += "_"
            missing = True
        result += " "
    return missing, result


def display_board(letters_guessed, letters_failed, word, no_tries):
    # Function Used for debugging.

    print("Guessed:", letters_guessed)
    print("Failed:", letters_failed)
    print("Word:", word)
    print("Tries:", no_tries)


def clear_screen():
    # Clears console output. Both Windows and Linux/MAC

    if name == 'nt':
        system('cls')
    else:
        system('clear')


def draw_hangman(tries):
    # Draw hangman depending on the number of tries

    if tries == 0:
        print("   _____        ")
        print("  |     |       ")
        print("  |             ")
        print("  |             ")
        print("  |             ")
        print("  |             ")
        print("  |             ")
        print("  |             ")
        print("================")
    elif tries == 1:
        print("   _____        ")
        print("  |     |       ")
        print("  |     O       ")
        print("  |             ")
        print("  |             ")
        print("  |             ")
        print("  |             ")
        print("  |             ")
        print("================")
    elif tries == 2:
        print("   _____        ")
        print("  |     |       ")
        print("  |     O       ")
        print("  |     |       ")
        print("  |     |       ")
        print("  |     |       ")
        print("  |             ")
        print("  |             ")
        print("================")
    elif tries == 3:
        print("   _____        ")
        print("  |     |       ")
        print("  |     O       ")
        print("  |     |       ")
        print("  |    /|       ")
        print("  |     |       ")
        print("  |             ")
        print("  |             ")
        print("================")
    elif tries == 4:
        print("   _____        ")
        print("  |     |       ")
        print("  |     O       ")
        print("  |     |       ")
        print("  |    /|\      ")
        print("  |     |       ")
        print("  |             ")
        print("  |             ")
        print("================")
    elif tries == 5:
        print("   _____        ")
        print("  |     |       ")
        print("  |     O       ")
        print("  |     |       ")
        print("  |    /|\      ")
        print("  |     |       ")
        print("  |    /       ")
        print("  |             ")
        print("================")
    elif tries == 6:
        print("   _____        ")
        print("  |     |       ")
        print("  |     O       ")
        print("  |     |       ")
        print("  |    /|\      ")
        print("  |     |       ")
        print("  |    / \      ")
        print("  |             ")
        print("================")
