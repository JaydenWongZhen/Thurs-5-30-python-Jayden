# list ig
num_list = [2944, -5490, 2357, -2619, 1177, 451, -8299, 2533, 4682, -6040, 0]
#the checker
def is_even(num):
    if num%2==0:
        return True
    elif num%2 != 0:
        return False
# the real deal
for c in range(0,len(num_list)):
    listval=num_list[c]
    trueorfalse=is_even(listval)
    if trueorfalse == True:
        print(listval , "is even")
    elif trueorfalse == False:
        print(listval , "is odd")