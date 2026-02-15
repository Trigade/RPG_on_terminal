from models.character import Character

class PlayableCharacter(Character):
    def __init__(self, health , armor , damage ,spell ,hp_gain , dmg_gain ,spell_gain , armor_gain):
        super().__init__(health, armor, damage, spell)
        self.exp = 0
        self.level = 1
        self.exp_to_next_level = 100

        self.hp_gain = hp_gain
        self.dmg_gain = dmg_gain
        self.spell_gain = spell_gain
        self.armor_gain = armor_gain

    def gain_exp(self,amount):
        self.exp += amount
        while self.exp >= self.exp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= self.exp_to_next_level
        self.exp_to_next_level = int(self.exp_to_next_level * 1.5)

        self.health += self.hp_gain
        self.damage += self.dmg_gain
        self.spell += self.spell_gain
        self.armor += self.armor_gain