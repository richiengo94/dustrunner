from random import shuffle, randint
import cards

class Deck:
    # Creates initial deck and shuffles
    def __init__(self, n_cards):
        self.max_n_cards = n_cards
        self.card_order = list(range(0, n_cards))
        self.shuffle_deck()

    # Shuffles the deck when deck runs out
    def shuffle_deck(self):
        self.card_order = list(range(0, self.max_n_cards))
        shuffle(self.card_order)

    # Draws top card and returns drawn card
    def draw_card(self):
        if(len(self.card_order) == 0):
            self.shuffle_deck()
        last_drawn_card = self.card_order.pop(0)
        return last_drawn_card