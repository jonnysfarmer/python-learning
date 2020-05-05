from classes.game import Person, bcolors

magic = [{
    'name': 'Fire',
    'cost': '10',
    'dmg': '60'
    },
    {
    'name': 'Thunder',
    'cost': '12',
    'dmg': '68'
    },
    {
    'name': 'Blizard',
    'cost': '8',
    'dmg': '50'
    },
]
player = Person(460, 65, 60, 30, magic)

print(player.generate_damge())
print(player.generate_damge())
print(player.generate_damge())

