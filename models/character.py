class Character:
    def __init__(self, health, armor, damage, spell):
        self.health = health
        self.armor = armor
        self.damage = damage
        self.spell = spell

    def is_dead(self):
        return self.health <= 0
    
    def taken_damage(self, damage):
        if damage <= self.armor:
            self.armor -= damage
        else:
            damage -= self.armor
            self.armor = 0
            self.health -= damage
        return self.is_dead()

    def give_damage(character, target):
        return target.taken_damage(character.damage)
    
    def give_spell_damage(character, target):
        return target.taken_damage(character.spell)