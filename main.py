from models.models import Mage,Ranger,Warrior,Swordsman,Golem,Rogue,Witch
from numpy import random
from os import system

def clear():
    system("cls")

def pause():
    system("pause")

def combat_logic(hero,enemy,exp_per_hit = 10):
    clear()
    print(f"--- {enemy.__class__.__name__} ile savaş başlıyor! ---")

    

    while hero.health > 0 and enemy.health > 0:
        hero_dice = random.randint(1,11)
        enemy_dice = random.randint(1,10)
        print(f"\nAtılan zar: {hero_dice}")

        if hero_dice < enemy_dice:
            print(f"Saldırı Başarısız {enemy.__class__.__name__} size {enemy.damage + enemy.spell} hasar vurdu")
            hero.taken_damage(enemy.damage + enemy.spell)
        elif hero_dice > enemy_dice:
            raw_damage = hero.damage + hero.spell
            calculated_damage = int(raw_damage * (hero_dice / 5))

            print(f"Saldırı başarılı! Verilen hasar: {calculated_damage}")
            enemy.taken_damage(calculated_damage)

            hero.gain_exp(exp_per_hit)
            print(f"+{exp_per_hit} EXP kazanıldı! Mevcut Seviye: {hero.level}")
        else:
            print("Saldırınız başarısız ancak karşıdan gelen saldırıyı da engellediniz")

        print(f"Kalan Canın: {hero.health} | {enemy.__class__.__name__} Canı: {enemy.health}")
        pause()
        clear()

    if hero.is_dead():
        system("color 4")
        print("\nÖldün... Oyun Bitti.")
    else:
        system("color a")
        print(f"\n{enemy.__class__.__name__} yenildi! Zafer senin.")
        pause()

clear()
system("color 07")
print("Hoşgeldin!!!")
print("Bir sınıf seç\n1-Mage(Büyücü)\n2-Swordsman(Kılıçcı)\n3-Ranger(Okçu)\n4-Warrior(Tank)\n")
choice = int(input("Seciminiz: "))

hero_map = {1: Mage, 2: Swordsman, 3: Ranger, 4: Warrior}
hero = hero_map.get(choice, Warrior)()

clear()
print("Orta Şehrine Hoşgeldiniz Ne yapmak istersiniz\n1-Ormana git\n2-Şehir merkezine git\n3-Bataklığa git")
location_choice = int(input("Seçiminiz: "))

if location_choice == 1:
    clear()
    print("Ormanda bir Golemle karşılaştınız!\n1-Saldır\n2-Kaç")
    action = int(input("Seçiminiz: "))
    if action == 1:
        combat_logic(hero, Golem())
    else:
        if random.randint(1, 11) > 6:
            print("Kaçtın!")
        else:
            print("Kaçamadın! Golem arkadan vurdu.")
            hero.taken_damage(30)
            combat_logic(hero, Golem())

elif location_choice == 2:
    clear()
    print("Şehir yolunda bir Haydut önünü kesti!\n1-Saldır\n2-Kaç")
    action = int(input("Seçiminiz: "))
    if action == 1:
        combat_logic(hero, Rogue())
    else:
        combat_logic(hero, Rogue())

elif location_choice == 3:
    clear()
    print("Bataklıkta bir cadıyla karşılaştın!\n1-Saldır\n2-Kaç")
    action = int(input("Seçiminiz: "))
    if action == 1:
        combat_logic(hero, Witch())
    else:
        combat_logic(hero, Witch())