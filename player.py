class Player:
    """Class for player"""

    # Creates initial player stats from vehicle card selection
    def __init__(self, card_data: dict, rear: str, chassis: str, front: str) -> None:
        vehicle_data = card_data["vehicle_cards"][0]

        self.max_ammo: int = vehicle_data["rear"][rear]["max_ammo"]
        self.max_fuel: int = vehicle_data["chassis"][chassis]["max_fuel"]
        self.base_damage: int = vehicle_data["chassis"][chassis]["base_dmg"]
        self.max_health: int = vehicle_data["front"][front]["max_health"]
        self.vp: int = vehicle_data["rear"][rear]["base_vp"] +\
            vehicle_data["chassis"][chassis]["base_vp"] +\
            vehicle_data["front"][front]["base_vp"]

        self.current_ammo: int = self.max_ammo
        self.current_fuel: int = self.max_fuel
        self.current_health: int = self.max_health

    def get_vp(self) -> int:
        """Returns current victory points"""
        return self.vp

    def set_vp(self, vp: int) -> None:
        """Sets current victory points"""
        self.vp = vp

    def defeat_enemy_vp(self) -> None:
        """Increases victory points from defeating enemy"""
        self.set_vp(self.get_vp() + 2)

    def redraw_res_card_vp(self) -> None:
        """Decreases victory points from redrawing resolution card"""
        self.set_vp(self.get_vp() - 2)

    def get_current_ammo(self) -> int:
        """Returns current player ammo"""
        return self.current_ammo
    
    def set_current_ammo(self, ammo: int) -> None:
        """Sets current player ammo"""
        self.current_ammo = ammo

    def get_current_fuel(self) -> int:
        """Returns current player fuel"""
        return self.current_fuel
    
    def set_current_fuel(self, fuel: int) -> None:
        """Sets current player fuel"""
        self.current_fuel = fuel

    def refill_tank(self) -> None:
        """Uses 1 fuel to refill tank at end of round"""
        self.set_current_fuel(self.get_current_fuel() - 1)

    def get_current_health(self) -> int:
        """Returns current player health"""
        return self.current_health
    
    def set_current_health(self, health: int) -> None:
        """Sets current player health"""
        self.current_health = health