from random import shuffle

class Deck:
    """Class for deck of cards"""

    # Creates initial deck and shuffles
    def __init__(self, n_cards: int) -> None:
        self.max_n_cards: int = n_cards
        self.card_order: list = []
        self.shuffle_deck()

    def shuffle_deck(self) -> None:
        """Shuffles the deck of cards"""
        self.card_order = [i for i in range(0, self.max_n_cards - 1)]
        shuffle(self.card_order)

    def draw_card(self, n_cards) -> list[int] | bool:
        """Draws n_cards # of cards and returns a list of the ids of the drawn cards"""
        drawn_card_ids: list = []
        shuffled_deck: bool = False

        for i in range(n_cards):
            if not(self.card_order):
                self.shuffle_deck()
                shuffled_deck = True
            drawn_card_ids.append(self.card_order.pop(0))

        return drawn_card_ids, shuffled_deck