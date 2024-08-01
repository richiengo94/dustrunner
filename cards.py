from json import load

class Cards:
    """Class for cards"""
    def __init__(self) -> None:
        with open("cards.json") as read_file:
            self.card_data = load(read_file)

    def get_card_data(self) -> dict:
        """Returns data from all cards"""
        return self.card_data
    
    def get_value(self, card_type: str, id: int, key: str):
        """Returns value of key on card #id"""
        return self.card_data[card_type][id][key]
    
    def get_cards(self, card_type: str) -> tuple:
        """Returns tuple of data from all cards of certain type"""
        return self.card_data[card_type]
    
class ResolutionCards(Cards):
    """Class for resolution cards"""

    # Stores resolution card data
    def __init__(self) -> None:
        Cards.__init__(self)
        self.res_cards = tuple(card for card in self.card_data["resolution_cards"])
    
    def get_damage(self, drawn_cards: list) -> int:
        """Returns total damage from drawn_cards data using ids"""
        total_dmg: str = 0
        for id in drawn_cards:
            total_dmg += self.get_value("resolution_cards", id, "dmg")
            
        return total_dmg
    
class ExplorationCards(Cards):
    """Class for exploration cards"""

    # Stores exploration card data
    def __init__(self) -> None:
        Cards.__init__(self)
        self.exp_cards = tuple(card for card in self.card_data["exploration_cards"])