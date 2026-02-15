from models.character import Character

class PlayableCharacter(Character):
    def __init__(self, health , armor , damage ,spell):
        super().__init__(health, armor, damage, spell)
        self.exp = 0
        self.level = 0
        self.exp_to_next_level = 0

    def gain_exp(self,amount):
        self.exp += amount
        while self.exp >= self.exp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = self.exp_to_next_level
        self.exp_to_next_level = int(self.exp_to_next_level * 1.5)