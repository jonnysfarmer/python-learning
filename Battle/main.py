from classes.game import Person, bcolors

magic = [{
    'name': 'Fire',
    'cost': 10,
    'dmg': 60
    },
    {
    'name': 'Thunder',
    'cost': 12,
    'dmg': 68
    },
    {
    'name': 'Blizard',
    'cost': 8,
    'dmg': 50
    },
]
player = Person(460, 65, 60, 30, magic)
enemy = Person(1200, 65, 45, 24, magic)

running = True

print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTAKS!' + bcolors.ENDC)

while running:
    print('====================')
    player.choose_action()
    choice = input('Choose action:')
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damge()
        enemy.take_damage(dmg)
        print('You attacked for ', dmg, 'points of damage.  Enemy HP: ', enemy.get_hp())



    # running = False