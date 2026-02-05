import random

colors: list = ['red', 'blue', 'yellow', 'green', 'purple', 'brown', 'black', 'white', 'orange']
correct_letters: set = set()
guessed_letters: set = set()
answered: bool = False
number_of_guesses: int = 0

def select_random_color():
    """Select a random color from the list 'colors' and return it."""
    random_color: str = random.choice(colors)
    return random_color


def save_color_set(color):
    return [correct_letters.add(letter) for letter in color]


def guess_word(answer: str):
    guess: str = str(input("\nGuess a letter from a color name!\n\n")).lower()
    guessed_letters.add(guess)

    display_list = []
    for letter in answer:
        if letter in guessed_letters.intersection(letter):
            display_list.append(letter)
        else:
            display_list.append("–")

    print(*display_list)
    if "–" not in display_list:
        print("YOU HAVE WON!")
        print(f"You needed {number_of_guesses} tries.")
        global answered
        answered = True

    else:
        print("""\nYou are close. Continue:\n----------------------------------""")



if __name__ == "__main__":
    word = select_random_color()
    save_color_set(word)
    while not answered:
        guess_word(word)
        number_of_guesses += 1
