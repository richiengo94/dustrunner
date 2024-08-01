from random import shuffle
import resolution_cards

class Deck:
    """Class for deck of cards"""

    # Creates initial deck and shuffles
    def __init__(self, n_cards: int) -> None:
        self.max_n_cards = n_cards
        self.card_order = []
        self.shuffle_deck()

    def shuffle_deck(self) -> None:
        """Shuffles the deck of cards"""
        self.card_order = [i for i in range(0, self.max_n_cards)]
        shuffle(self.card_order)

    def draw_card(self) -> int:
        """Draws the top card and returns the id of the drawn card"""
        if not(self.card_order):
            self.shuffle_deck()
        drawn_card_id = self.card_order.pop(0)
        return drawn_card_id