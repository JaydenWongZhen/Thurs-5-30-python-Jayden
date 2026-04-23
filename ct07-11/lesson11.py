# def divisible7(num):
#     if num%7==0:
#         return True
#     else:
#         return False
# a=divisible7(56)
# b=divisible7(42)
# print(a)
# print(b)
import turtle
import random
finx=-200
def prepare(xlel,ylel):
    d= turtle.Screen()
    d.setup(width=xlel,height=ylel)
    d.bgcolor("forest green")
    return d
p=prepare(400,600)

def releaseturty(col):
    hi=turtle.Turtle()
    hi.color(col)
    hi.shape("turtle")
    return hi
cyn=releaseturty("cyan")
cyn.penup()
cyn.seth(90)
cyn.goto(0,-250)
jovi=releaseturty("orange")
jovi.penup()
jovi.seth(90)
jovi.goto(-150,-250)
eldrichhoror=releaseturty("turquoise")
eldrichhoror.penup()
eldrichhoror.seth(90)
eldrichhoror.goto(150,-250)
finisher=releaseturty("black")
finisher.penup()
finisher.hideturtle()
finisher.shape("square")
finisher.setx(finx)
finisher.sety(250)
for smth in range(20):
    finisher.pendown()
    finisher.stamp()
    finisher.penup()
    finx+=25
    finisher.setx(finx)
finisher.penup()
finisher.color("yellow")
finisher.setx(-200)
finisher.sety(-250)
finisher.pendown()
finisher.forward(500)
p.mainloop()