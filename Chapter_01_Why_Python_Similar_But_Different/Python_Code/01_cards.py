import random


suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

faces = ["Jack", "Queen", "King", "Ace"]

numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def draw():
    the_suit = random.choice(suits)
    the_card = random.choice(numbered + faces)
    return the_card, "of", the_suit


print(draw())
print(draw())
print(draw())
