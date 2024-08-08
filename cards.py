from json import load
from typing import Any

class Cards:
    """Class for cards"""
    def __init__(self) -> None:
        with open("cards.json") as read_file:
            self.card_data = load(read_file)

    def get_card_data(self) -> dict[Any]:
        """Returns data from all cards"""
        return self.card_data
    
    def get_value(self, card_type: str, id: int, key: str) -> Any:
        """Returns value of key on card #id"""
        return self.card_data[card_type][id][key]
    
    def get_card(self, card_type: str, id: int) -> dict:
        """Returns dictionary info of card type using id"""
        return self.card_data[card_type][id]
    
class ResolutionCards(Cards):
    """Class for resolution cards"""

    # Stores resolution card data
    def __init__(self) -> None:
        Cards.__init__(self)
        self.res_cards: list = [card for card in self.card_data["resolution_cards"]]
    
    def get_damage(self, drawn_cards: list[int]) -> int:
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
        self.exp_cards: list = [card for card in self.card_data["exploration_cards"]]