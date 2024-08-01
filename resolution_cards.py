from json import load

class ResolutionCards:
    """Class for the resolution cards"""

    # Loads and stores resolution card data from .json
    def __init__(self) -> None:
        self.res_cards = []

        with open("resolution_cards.json") as read_file:
            card_data = load(read_file)

        self.res_cards = tuple(card for card in card_data["cards"])
            
    def get_value(self, id: int, key: str):
        """Returns value of resolution card #id using key"""
        return self.res_cards[id][key]
    
    def get_cards(self) -> tuple:
        """Returns tuple of data from all resolution cards"""
        return self.res_cards