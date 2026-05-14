def title():
    print("""
     ██████╗  ██████╗  ██████╗███████╗  ██████╗ ██╗   ██╗███████╗███████╗████████╗
    ██╔════╝ ██╔═══██╗██╔══██╗██╔════╝ ██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝
    ██║      ██║   ██║██║  ██║█████╗   ██║   ██║██║   ██║█████╗  ███████╗   ██║   
    ██║      ██║   ██║██║  ██║██╔══╝   ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   
    ╚██████╗ ╚██████╔╝██████╔╝███████╗ ╚██████╔╝╚██████╔╝███████╗███████║   ██║   
     ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
""")
def seperator():
    print("=" * 45)
def rules():
    print("stuff and rules")
    print("1.aight, here's the rules. to select, choose a number.")
    print("2. if you try abusing glitches i will go kill you")
    print("3. speciffic choices end the game read carefully")
    print("4. just chillax, its okay if you make a mistake")
def menu():
    print("menu:")
    print("1] start saved game")
    print("2] rules")
    print("3] quit")
def gametro():
    title()
    seperator()
    print('welcome to this world!')
    print("this s a short text based game rpg")
    seperator()
    rules()
    seperator()
    menu()
def placeholder():
    print("placeholder")
def quest(questname,reward):
    print("----guild 108 quest board----")
    print(f"Quest: {questname}")
    print(f"Reward: {reward}")
    print("1] do quest 1")
    print("="*40)
def detailquest(loc,risk):
    print(f"location: {loc}")
    print(f"risk: {risk}")
    if risk.lower() =="minimal":
        print("Guild member analyzation / good beginner mission! minimal danger")
    elif risk.lower() == "median":
        print("Guild member analyzation / best for intermediates, there ez enemy")
    elif risk.lower() == "risky":
        print("Guild member analyzation / hard, the typa thing i like! be careful ")
    elif risk.lower() == "treacherous":
        print("Guild member analyzation / ello i am first person to beat this, no one has verified this yet except me")
    else:
        print("Guild member analyzation / all hope is lost it has HUGE difficulty spikes up to treacherous i got lucky and got no difficulty spikes")
gametro()
select = ""
while select != "1":
    select=input("select[ ")
    if select == "1":
        quest("find roky the iiird", "free D20 card,150 ogojs (guild currency)")
    elif select == "2":
        rules()
    elif select == "3":
        print("quit")
        break