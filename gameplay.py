from deck import Deck
from player import Player
from cards import Cards, ResolutionCards, ExplorationCards
from enemy import Enemy
from random import randint

def choose_car_parts() -> list:
    """Returns list of difficulty for each car part"""
    vehicle_parts_list = []
    random_vehicle = input("Random vehicle?: ")
    vehicle_parts_difficulty = ("easy", "hard")
    
    if(random_vehicle == "y"):
        vehicle_parts_list = [vehicle_parts_difficulty[randint(0, 1)] for i in range(3)]
    else:
        vehicle_parts_list.append(input("Vehicle rear: "))
        vehicle_parts_list.append(input("Vehicle chassis: "))
        vehicle_parts_list.append(input("Vehicle front: "))

    return vehicle_parts_list[0], vehicle_parts_list[1], vehicle_parts_list[2]

def is_enemy_card(is_first: bool, exp: str, exp_cards: ExplorationCards, drawn_exp_cards: int) -> bool:
    """Checks is exploartion card selected is an enemy"""
    if(is_first):
        if(exp_cards.get_value(exp, drawn_exp_cards[0], "effect") == "raider" or exp_cards.get_value(exp, drawn_exp_cards[0],"effect") == "spybot"):
            return True
    else:
        if(exp_cards.get_value(exp, drawn_exp_cards[1], "effect") == "raider" or exp_cards.get_value(exp, drawn_exp_cards[1],"effect") == "spybot"):
            return True
    
    return False

def generate_enemy(is_first: bool, res: str, exp: str, drawn_res_cards: int,
                    drawn_exp_cards: int, res_cards: ResolutionCards, exp_cards: ExplorationCards) -> Enemy:
    """Generates enemy object"""
    if(is_first):
        base_health = exp_cards.get_value(exp, drawn_exp_cards[0], "base_health")
        n_attack = exp_cards.get_value(exp, drawn_exp_cards[0], "n_attack")
        reward = exp_cards.get_value(exp, drawn_exp_cards[0], "reward")
    else:
        base_health = exp_cards.get_value(exp, drawn_exp_cards[1], "base_health")
        n_attack = exp_cards.get_value(exp, drawn_exp_cards[1], "n_attack")
        reward = exp_cards.get_value(exp, drawn_exp_cards[1], "reward")

    dice_val = res_cards.get_value(res, drawn_res_cards[0], "dice_val")

    return Enemy(is_first, base_health, dice_val, n_attack, reward)

player_location: int = 2
enemy_location: int = 0

res_deck = Deck(10)
exp_deck = Deck(12)
card_data = Cards()
res_cards = ResolutionCards()
exp_cards = ExplorationCards()

is_first: bool = True
in_combat: bool = False

res: str = "resolution_cards"
exp: str = "exploration_cards"

rear, chassis, front = choose_car_parts()
player = Player(card_data.get_card_data(), rear, chassis, front)

drawn_exp_cards = exp_deck.draw_card(2)
print(exp_cards.get_card(exp, drawn_exp_cards[0]))
select_first_card = input("Select first card?: ")

if(select_first_card == "y"):
    is_first = True
elif(select_first_card == "n"):
    print(exp_cards.get_card(exp, drawn_exp_cards[1]))
    is_first = False

if(is_enemy_card(is_first, exp, exp_cards, drawn_exp_cards)):
        drawn_res_cards = res_deck.draw_card(1)
        enemy = generate_enemy(is_first, res, exp, drawn_res_cards, drawn_exp_cards, res_cards, exp_cards)
        in_combat = True