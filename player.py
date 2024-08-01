class Player:
    """Class for the player"""

    # Creates initial player stats
    def __init__(self, max_ammo: int, max_fuel: int, max_health:int, base_vp: int) -> None:
        self.max_ammo: int = max_ammo
        self.max_fuel: int = max_fuel
        self.max_health: int = max_health
        self.vp: int = base_vp
        self.current_ammo: int = self.max_ammo
        self.current_fuel: int = self.max_fuel
        self.current_health: int = self.max_health

    def get_vp(self) -> int:
        """Returns current victory points"""
        return self.vp

    def set_vp(self, vp: int) -> None:
        """Sets current victory points"""
        self.vp = vp

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

    def get_current_health(self) -> int:
        """Returns current player health"""
        return self.current_health
    
    def set_current_health(self, health: int) -> None:
        """Sets current player health"""
        self.current_health = health