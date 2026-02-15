from models.models import Mage, Warrior, Ranger, Swordsman, Golem, Rogue
import numpy as np
from os import system

# Renk ve ekran temizleme ayarları
def clear_screen():
    system("cls")

def combat_logic(hero, enemy, exp_per_hit=20):
    clear_screen()
    print(f"--- {enemy.__class__.__name__} ile savaş başlıyor! ---")
    
    while hero.health > 0 and enemy.health > 0:
        dice = np.random.randint(1, 11)
        print(f"\nAtılan zar: {dice}")
        
        if dice <= 2:
            print(f"Saldırı başarısız! {enemy.__class__.__name__} size vurdu.")
            # Senin modellerindeki zırh mantığını kullanması için taken_damage çağırdık
            hero.taken_damage(enemy.damage) 
        else:
            # Zar sonucuna göre hasar çarpanı ekliyoruz
            # Karakterinin temel hasarını (damage + spell) alıp zarla çarpıyoruz
            raw_damage = hero.damage + hero.spell
            calculated_damage = int(raw_damage * (dice / 5))
            
            print(f"Saldırı başarılı! Verilen hasar: {calculated_damage}")
            enemy.taken_damage(calculated_damage)
            
            # İSTEDİĞİN ÖZELLİK: Her hasar verişte EXP kazanma
            hero.gain_exp(exp_per_hit)
            print(f"+{exp_per_hit} EXP kazanıldı! Mevcut Seviye: {hero.level}")
            
        print(f"Kalan Canın: {hero.health} | {enemy.__class__.__name__} Canı: {enemy.health}")
        system("pause")

    if hero.is_dead():
        system("color 4")
        print("\nÖldün... Oyun Bitti.")
    else:
        system("color a")
        print(f"\n{enemy.__class__.__name__} yenildi! Zafer senin.")
        system("pause")

# --- ANA EKRAN ---
clear_screen()
system("color 07")
print("Hoşgeldin!!!")
print("Bir sınıf seç\n1-Mage(Büyücü)\n2-Swordsman(Kılıçcı)\n3-Ranger(Okçu)\n4-Warrior(Tank)\n")
choice = int(input("Seciminiz: "))

hero_map = {1: Mage, 2: Swordsman, 3: Ranger, 4: Warrior}
hero = hero_map.get(choice, Warrior)() # Hatalı seçimde varsayılan Warrior

clear_screen()
print("Orta Şehrine Hoşgeldiniz Ne yapmak istersiniz\n1-Ormana git\n2-Şehir merkezine git")
location_choice = int(input("Seçiminiz: "))

if location_choice == 1:
    clear_screen()
    print("Ormanda bir Golemle karşılaştınız!\n1-Saldır\n2-Kaç")
    action = int(input("Seçiminiz: "))
    if action == 1:
        combat_logic(hero, Golem())
    else:
        # Kaçış şansı
        if np.random.randint(1, 11) > 6:
            print("Kaçtın!")
        else:
            print("Kaçamadın! Golem arkadan vurdu.")
            hero.taken_damage(30)
            combat_logic(hero, Golem())

elif location_choice == 2:
    clear_screen()
    print("Şehir yolunda bir Haydut önünü kesti!\n1-Saldır\n2-Kaç")
    action = int(input("Seçiminiz: "))
    if action == 1:
        combat_logic(hero, Rogue())
    else:
        combat_logic(hero, Rogue()) # Kaçamazsan savaş başlar