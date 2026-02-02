import random

colors: list = ['red', 'blue', 'yellow', 'green', 'purple', 'brown', 'black', 'white', 'orange']


def select_random_color():
    """Select a random color from the list 'colors' and return it."""
    random_color = colors[random.randint(0, len(colors)) - 1]
    return random_color


if __name__ == "__main__":
    select_random_color()
