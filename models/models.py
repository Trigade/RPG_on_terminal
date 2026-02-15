from models.playable_character import PlayableCharacter 
from models.character import Character

class Mage(PlayableCharacter):
    def __init__(self):
        super().__init__(health = 60, armor = 2, damage = 5, spell = 30,hp_gain=8 , dmg_gain=2 , spell_gain= 12 ,armor_gain= 1)

class Ranger(PlayableCharacter):
    def __init__(self):
        super().__init__(health = 90, armor = 6, damage = 22, spell = 4,hp_gain=12 , dmg_gain=8 , spell_gain= 2 ,armor_gain= 3)

class Warrior(PlayableCharacter):
    def __init__(self):
        super().__init__(health = 160, armor = 12, damage = 18, spell = 0,hp_gain=12 , dmg_gain=8 , spell_gain= 2 ,armor_gain= 3)

class Swordsman(PlayableCharacter):
    def __init__(self):
        super().__init__(health = 110, armor = 10, damage = 20, spell = 0,hp_gain=15 , dmg_gain=6 , spell_gain= 10 ,armor_gain= 4)

class Golem(Character):
    def __init__(self):
        super().__init__(health = 400, armor = 0, damage = 12, spell = 0)

class Rogue(Character):
    def __init__(self):
        super().__init__(health = 150, armor = 15, damage = 25, spell = 0)

class Witch(Character):
    def __init__(self):
        super().__init__(health = 120, armor = 0, damage = 4, spell = 25)