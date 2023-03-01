from random import randint
from random import choice
from math import ceil

''' TODOS:
- leveling sys
- stats
- items
- skills
- classes/types?
'''

# Create Player/Enemy Object
class Creator(object):
    alive = True

    def __init__(self, name, hp, mp, xp, xpneed, lvl):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.maxhp = hp
        self.maxmp = mp
        self.xp = xp
        self.xpneed = xpneed
        self.lvl = lvl

player = Creator("swan", 500, 50, 0, 50, 1)

# Bring a new Mob to life
def spawn(plvl):
    type = ["Grobian", "Dieb", "Wolf"]
    ehp = (plvl*(plvl-1)+randint(8,12))
    emp = (plvl*(plvl-1)+randint(8,12))
    exp = ceil(ehp + emp / 2)
    elvl = 1

    mob = Creator(choice(type), ehp, emp, exp, 0, elvl)
    return mob

def PlayLoop(enemy):
    print("dr spiler: {}, mit {}/{}hp, {}/{}mp und {}/{}xp, lvl {}".format(player.name, player.hp, player.maxhp, player.mp, player.maxmp, player.xp, player.xpneed, player.lvl))
    print("gäge: {} mit {}hp, {}mp wo {}xp git".format(enemy.name, enemy.hp, enemy.mp, enemy.xp))

    while enemy.alive:
        patk = randint(2,5)
        eatk = randint(1,3)

        print("dr spiler hout mit {} und dr gägner mit {}".format(patk,eatk))
        player.hp = player.hp - eatk 
        enemy.hp = enemy.hp - patk 

        # Gägner dod - neue gägner
        if enemy.hp <= 0:
            enemy.alive = False
        # Player dod - sense RIP
        if player.hp <= 0:
            player.alive = False
            break

    if enemy.alive == False:
        print("##########\ngägner tot\n##########")
        player.xp = player.xp + enemy.xp
        if player.xp >= player.xpneed:
            print("##########\nLEVEL UP!\n##########")
            player.lvl += 1
            player.xp = 0
            player.hp = player.maxhp
            player.mp = player.maxmp
            player.xpneed = (player.lvl*(player.lvl-1)*50)

        # Spawn a new enemy - scaled to player lvl
        spawn(player.lvl)
    
while player.alive:
    enemy = spawn(player.lvl)
    PlayLoop(enemy)

print("\n###########\nswan tot :(\n###########")
