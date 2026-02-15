from models.playable_character import PlayableCharacter 
from models.character import Character

class Mage(PlayableCharacter):
    def __init__(self):
        super().__init__(health = 60, armor = 3, damage = 5, spell = 25,hp_gain=10 , dmg_gain=10 , spell_gain= 10 ,armor_gain= 10)

class Ranger(PlayableCharacter):
    def __init__(self):
        super().__init__(health = 80, armor = 7, damage = 18, spell = 5,hp_gain=10 , dmg_gain=10 , spell_gain= 10 ,armor_gain= 10)

class Warrior(PlayableCharacter):
    def __init__(self):
        super().__init__(health = 150, armor = 10, damage = 20, spell = 0,hp_gain=10 , dmg_gain=10 , spell_gain= 10 ,armor_gain= 10)

class Swordsman(PlayableCharacter):
    def __init__(self):
        super().__init__(health = 100, armor = 10, damage = 15, spell = 0,hp_gain=10 , dmg_gain=10 , spell_gain= 10 ,armor_gain= 10)

class Golem(Character):
    def __init__(self):
        super().__init__(health = 200, armor = 0, damage = 15, spell = 0)

class Rogue(Character):
    def __init__(self):
        super().__init__(health = 100, armor = 20, damage = 20, spell = 0)