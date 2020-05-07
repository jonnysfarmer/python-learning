from classes.game import Person, bcolors

magic = [{
    'name': 'Fire',
    'cost': 10,
    'dmg': 100
    },
    {
    'name': 'Thunder',
    'cost': 12,
    'dmg': 124
    },
    {
    'name': 'Blizard',
    'cost': 8,
    'dmg': 82
    },
]
player = Person(460, 65, 60, 30, magic)
enemy = Person(1200, 65, 45, 24, magic)

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
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + '\n Not enough MP \n' + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print('You cast ', spell, 'for', magic_dmg, 'points of damage.  Enemy HP: ', enemy.get_hp())
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