from models.playable_character import PlayableCharacter 
from models.character import Character

class Mage(PlayableCharacter):
    def ___init__(self):
        super().__init__(health = 60, armor = 3, damage = 5, spell = 25)

class Ranger(PlayableCharacter):
    def __init__(self):
        super().__init__(health = 80, armor = 7, damage = 18, spell = 5)

class Warrior(PlayableCharacter):
    def __init__(self):
        super().__init__(health = 150, armor = 10, damage = 20, spell = 0)

class Swordsman(PlayableCharacter):
    def __init__(self):
        super().__init__(health = 100, armor = 10, damage = 15, spell = 0)

class Golem(Character):
    def __init__(self):
        super().__init__(health = 200, armor = 0, damage = 15, spell = 0)

class Rogue(Character):
    def __init__(self):
        super().__init__(health = 100, armor = 20, damage = 20, spell = 0)