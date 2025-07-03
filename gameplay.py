from deck import Deck
from player import Player
from cards import Cards, ResolutionCards, ExplorationCards
from enemy import Enemy
from random import randint

def choose_car_parts() -> list:
    """Returns list of difficulty for each car part"""
    vehicle_parts_list: list = []
    random_vehicle = input("Random vehicle?: ")
    vehicle_parts_difficulty = ("easy", "hard")
    
    if(random_vehicle == "y"):
        vehicle_parts_list = [vehicle_parts_difficulty[randint(0, 1)] for i in range(3)]
    else:
        vehicle_parts_list.append(input("Vehicle rear: "))
        vehicle_parts_list.append(input("Vehicle chassis: "))
        vehicle_parts_list.append(input("Vehicle front: "))

    return vehicle_parts_list[0], vehicle_parts_list[1], vehicle_parts_list[2]

def get_card_effect(exp: str, exp_cards: ExplorationCards, selected_exp_card: int) -> str:
    """Gets exploration card effect"""

    effect = exp_cards.get_value(exp, selected_exp_card, "effect")
        
    return effect

def generate_enemy(is_first: bool, res: str, exp: str, drawn_res_cards: list[int],
                    selected_exp_card: int, res_cards: ResolutionCards, exp_cards: ExplorationCards) -> Enemy:
    """Generates enemy object"""

    base_health = exp_cards.get_value(exp, selected_exp_card, "base_health")
    n_attack = exp_cards.get_value(exp, selected_exp_card, "n_attack")
    reward = exp_cards.get_value(exp, selected_exp_card, "reward")

    dice_val = res_cards.get_value(res, drawn_res_cards[0], "dice_val")

    return Enemy(is_first, base_health, dice_val, n_attack, reward)

def check_player_fuel(player: Player) -> bool:
    """Checks remaining player fuel and returns boolean"""

    if(player.get_current_fuel() > 0):
        player.refill_tank()
        return True
    
    return False

player_location: int = 2
enemy_location: int = 0

def get_movement(player: Player, exp: str, selected_exp_card: int, exp_cards: ExplorationCards) -> int:
    """Gets number of spaces for player"""

    card_name : str = exp_cards.get_value(exp, selected_exp_card, "name")
    card_text : str = exp_cards.get_value(exp, selected_exp_card, "text")
    choice : str = ""
    player_movement = 0

    if(player.get_current_fuel()):
        while True:
            choice = input(card_text + ": ")
            if(choice == "y" or choice == "n"):
                break

        if(choice == "y"):
            if(card_name == "clear path"):
                player_movement = 2
            else:
                player_movement = 1

    return player_movement

def restock_player(player: Player, exp: str, selected_exp_card : int, exp_cards: ExplorationCards) -> None:
    """Restocks the player depending on selected card effect"""

    card_name : str = exp_cards.get_value(exp, selected_exp_card, "name")
    card_text : str = exp_cards.get_value(exp, selected_exp_card, "text")
    choice : str = ""

    if(card_name != "farm"):
        while True:
            choice = input(card_text + ": ")
            if choice == "1" or choice == "2":
                break

        if choice == "1":
            player.set_current_fuel(player.get_current_fuel() - 1)
            player_location += 1
        else:
            if(card_name == "ambulance"):
                player.set_current_health(player.get_current_health() + 3)
            elif(card_name == "gas station"):
                player.set_current_fuel(player.get_current_fuel() +  2)
            elif(card_name == "outpost"):
                player.set_current_ammo(player.get_current_ammo() + 2)
    else:
        player.set_current_health(player.get_current_health() + 1)
        player.set_current_fuel(player.get_current_fuel() +  1)
        player.set_current_ammo(player.get_current_ammo() + 1)

res_deck = Deck(10)
exp_deck = Deck(12)
card_data = Cards()
res_cards = ResolutionCards()
exp_cards = ExplorationCards()

is_first: bool = True
in_combat: bool = False
restock_type: str = ""
refilled: bool = False
game_over = False

res: str = "resolution_cards"
exp: str = "exploration_cards"

rear, chassis, front = choose_car_parts()
player = Player(card_data.get_card_data(), rear, chassis, front)

drawn_exp_cards, exp_deck_shuffled = exp_deck.draw_card(2)

print(exp_cards.get_card(exp, drawn_exp_cards[0]))
if(exp_cards.get_value(exp, drawn_exp_cards[0], "effect") == "dust worm"):
    select_first_card = "y"
else:
    select_first_card = input("Select first card?: ")

if(select_first_card == "y"):
    is_first = True
    selected_exp_card = drawn_exp_cards[0]
elif(select_first_card == "n"):
    print(exp_cards.get_card(exp, drawn_exp_cards[1]))
    is_first = False
    selected_exp_card = drawn_exp_cards[1]

effect : str = get_card_effect(exp, exp_cards, selected_exp_card)
player_movement : int = 0
enemy_movement : int = 0

if(effect == "enemy"):
    drawn_res_cards, _ = res_deck.draw_card(1)
    enemy = generate_enemy(is_first, res, exp, drawn_res_cards, selected_exp_card, res_cards, exp_cards)
    in_combat = True
elif(effect == "restock"):
    restock_player(player, exp, selected_exp_card, exp_cards)
elif(effect == "movement"):
    player_movement = get_movement(player, exp, selected_exp_card, exp_cards)

if(exp_deck_shuffled):
    refilled = check_player_fuel(player)

if(not refilled):
    enemy_movement = 2

player_location += player_movement
enemy_location += enemy_movement