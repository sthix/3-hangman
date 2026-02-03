import random

colors: list = ['red', 'blue', 'yellow', 'green', 'purple', 'brown', 'black', 'white', 'orange']
correct_letters: set = set()
answered: bool = False

def select_random_color():
    """Select a random color from the list 'colors' and return it."""
    random_color: str = random.choice(colors)
    return random_color

def save_color(word):
    [correct_letters.add(letter) for letter in word]
    print(correct_letters)

def guess_word(word):
    guess: str = str(input("Guess a letter from a color name!\n"))
    print(correct_letters)

    if guess in word:
        print(guess)
    else:
        print("– ")


def show_guess(word, guess):
    # Show the word with the currently correctly guessed letters
    display_list = []
    for letter in word:
        if letter in word:
            print(letter)
        else:
            print("_")


    print(*display_list)

if __name__ == "__main__":
    word = select_random_color()
    save_color(word)
