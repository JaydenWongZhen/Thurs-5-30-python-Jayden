"""
============================================================
Q2. Food Order System
============================================================
Write a PYTHON program that simulates a restaurant order
system using list and while loop.

Requirements:
- Use a while loop
- Ask: "What would you like to order?"
- Store each order into a list
- Stop when user enters "end"
- After ending, print all orders in numbered format

============================================================
"""
resterount=input("welcome to the shake shack what would you like to order? ")
food=[]
while resterount != "thats it":
    resterount=input("welcome to the shake shack what would you like to order? ")
    if resterount != "thats it":
        food.append(resterount)
count=1
for count in range(len(food)):
    print(str(count) , ". " , food[count])