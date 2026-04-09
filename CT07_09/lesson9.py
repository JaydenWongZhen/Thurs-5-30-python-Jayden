# correct=False
# ridel=input("what has to be broken beofre you can use it? ")
# ridelow=ridel.lower()
# if "egg" in ridelow:
#     correct = True
# if correct == True:
#     print("yes you correct it egg")
# else:
#     print("no u worng it eg")
import turtle
window = turtle.Screen()
window.setup(width=800,height=800)
artist=turtle.Turtle()
artist.pendown()
artist.color("teal")
# for i in range(4):
#     artist.left(90)
#     artist.forward(50)
# artist.seth(90)
# artist.forward(60)
# artist.right(90)
artist.penup()
artist.goto(0,0)
def circleart():
    artist.pendown()
    butt = 0
    while butt <= 360:
        artist.forward(1)
        artist.right(1)
        butt+=1
def squareart(size):
    artist.pendown()
    for i in range(4):
        artist.forward(size)
        artist.right(90)
# a = 200
# # b = 100
# for hi in range(6):
#     artist.penup()
#     artist.goto(a,100)
#     squareart(100)
#     a -= 125
#     # b -= 100
#     artist.penup()
# print(artist.pos())
c = 50
def polycreate(side,len):
    artist.pendown()
    for drw in range(side):
        artist.forward(len)
        artist.left(360/side)
    artist.penup()
# for bi in range(6):
#     artist.penup()
#     squareart(c)
#     c += 50
# polycreate(4,100)
# artist.goto(0,100)
# polycreate(3,100)
window.mainloop() # this should be last line