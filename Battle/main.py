from classes.game import Person, bcolors
from classes.magic import Spell

# Create Black Magic
fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('thunder', 10, 100, 'black')
blizard = Spell('blizard', 10, 100, 'black')
meteor = Spell('metepr', 8, 80, 'black')
quake = Spell('quake', 12, 120, 'black')

# Create White Magic
cure = Spell('Cure', 12, 120, 'white')
cura = Spell('Cura', 20, 220, 'white')

# Instigate People
player = Person(460, 65, 60, 30, [fire, thunder, blizard, meteor, quake, cure, cura])
enemy = Person(1200, 65, 45, 24, [])

running = True

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTAKS!' + bcolors.ENDC)

while running:
    # Basic Player Attack
    print('====================')
    player.choose_action()
    choice = input('Choose action:')
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damge()
        enemy.take_damage(dmg)
        print('You attacked for ', dmg, 'points of damage.  Enemy HP: ', enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input('Choose Magic:')) - 1
        
        spell = player.magic[magic_choice]
        magic_damage = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + '\n Not enough MP \n' + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_damage)
        print('You cast ', spell.name, 'for', magic_damage, 'points of damage.  Enemy HP: ', enemy.get_hp())
        print('Your MP is', player.get_mp(), '/', player.get_maxmp())
    
    
    # Basic Enemy attack
    enemy_choice = 1

    enemy_dmg = enemy.generate_damge()
    player.take_damage(enemy_dmg)
    print('Enemy attacks for', enemy_dmg, 'Player HP: ', player.get_hp())

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + 'You Win' + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + 'Your enemy has deated you' + bcolors.ENDC)
        running = False

    # running = False