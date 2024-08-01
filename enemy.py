class Enemy:
    """Class for enemy"""

    def __init__(self, base_health: int, health_modifier: int, n_attack: int, reward: str) -> None:
        self.health = base_health + health_modifier
        self.n_attack = n_attack
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