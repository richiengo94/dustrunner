class Enemy:
    """Class for enemy"""

    # Sets base stats of enemy depending on first or second card drawn
    def __init__(self, is_first: bool, base_health: list, health_modifier: int, n_attack: list, reward: list) -> None:
        if is_first:
            self.health = base_health[0] + health_modifier
            self.n_attack = n_attack[0]
        else:
            self.health = base_health[1] + health_modifier
            self.n_attack = n_attack[1]
        self.reward = reward

    def get_health(self) -> int:
        """Returns current enemy health"""
        return self.health
    
    def set_health(self, health: int) -> None:
        """Sets health of enemy"""
        self.health = health
    
    def get_n_attack(self) -> int:
        """Returns n_attack # of attacks for enemy during combat"""
        return self.n_attack
    
    def get_reward(self) -> str:
        """Returns reward received after defeating enemy"""
        return self.reward