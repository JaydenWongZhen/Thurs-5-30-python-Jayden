print("Good luck! :]")
"""
============================================================
Q1. Hero Quest
============================================================
A hero goes on an adventure, starting at Full Health.
He fights monsters and loses health randomly each round.

Requirements:
- Start with 100 health
- Print starting message
- Lose between 1 to 15 health each round (random)
- Use a while-loop
- Continue until health <= 0
- Print total number of battles fought

============================================================
"""

#improt

import random

#vars 

hp=100
rounds=0

#ready start

print("the hero starts his adventure through the cool forest")

#damage system

while hp >= 0:
    hp -= random.randint(1,15)
    if hp >= 0:
        rounds +=1
        print("the hero had to fight a goblin and lost some hp. he now has " , hp , " hp")

# dead system

if hp <= 0:
    print("the hero died becuase he fought too many goblins")
    print("he fought " , rounds , " goblins. what a brave man")