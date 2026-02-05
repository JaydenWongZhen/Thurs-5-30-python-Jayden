import random
# number=0
# winga=[]
# while len(winga) < 100:
#     number=random.randint(1000,9999)
#     if number not in winga:
#         winga.append(number)
# print("te winnah r..." , winga)
stduns=[]
# while len(stduns) < 12:
#      number=random.randint(0,100)
#      if number not in stduns:
#          stduns.append(number)
# print("avg of students mark is " , round(sum(stduns)/len(stduns)))
# print("most makrs trohphy go to someone with the marks: " , max(stduns))
# print("the most outrageous loser goes to someone with the cringe marks: " , min(stduns))

namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
            "Sophia", "Lucas", "Mia", "Aiden"
            ]
heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]
tal=max(heightlist)
conn=heightlist.index(tal)
print(namelist[conn] , " is ze tallest student at ", tal , " cm")