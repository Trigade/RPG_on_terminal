class Character:
    def __init__(self, health, armor, damage, spell):
        self.health = health
        self.armor = armor
        self.damage = damage
        self.spell = spell

    def is_dead(self):
        return self.health <= 0
    
    def taken_damage(self, damage):
        if damage < self.armor:
            return self.is_dead()
        damage -= self.armor
        self.armor = 0
        self.health -= damage
        return self.is_dead()

    def give_damage( character, target):
        damage = character.damage
        if target.armor > damage:
            target.armor -= damage
            return target.is_dead()
        damage -= target.armor
        target.armor = 0
        target.health -= damage
        return target.is_dead()
    
    def give_spell_damage(character, target):
        spell_damage = character.spell
        if target.armor > spell_damage:
            target.armor -= spell_damage
            return target.is_dead()
        spell_damage -= target.armor
        target.armor = 0
        target.health -= spell_damage
        return target.is_dead()