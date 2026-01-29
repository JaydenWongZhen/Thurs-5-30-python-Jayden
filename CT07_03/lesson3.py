# print("peepeepoopoo")
# Piss=0
# while Piss<5:
#     print("Guthib")
#     Piss+=1
# riddl="what always comes but never reaches us? "
# thecorrect="tomorrow"
# inpuh=""
# while inpuh.lower()!=thecorrect:
#     inpuh=input(riddl)
#     if inpuh.lower()!=thecorrect:
#         print("wrong!!!!! try agaen.")
#     if inpuh.lower()==thecorrect:
#         print("wowza u did it!!!")
# import time
# # time.sleep(5)
# # print("piss man")
# timer = int(input("how many seconds "))

# while int(timer) >= 0:
#     print(timer)
#     time.sleep(1)
#     timer -= 1
#     if int(timer) == 0:
#         print("WAKE TF UP")

print("Hello! I am your ATM buddy that helps you to save!")
Feacher="How much did yiu save? "
sav= 10
while sav <= 100:
    sav=sav+int(input(Feacher))
    if sav <= 100:
        print("Good, you have " , sav , " dollars in the account! Keep saving ^_^")
    if sav >= 100:
        print("Congrats! You have now saved " , sav , " dollars!")
