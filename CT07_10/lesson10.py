#hi the funny text guy quit
# def addition(n1,n2):
#     return n1 + n2
# ad=addition(5,2)
# def multiply(n1,n2):
#     return n1 * n2
# a=multiply(5,7)
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# kirk=is_even(4)
# print(kirk)

# age=input("enter age here ")
# def sortage(a):
#     if int(a) <= 13:
#         return "child"
#     elif int(a) <= 20:
#         return "teenager"
#     elif int(a) <= 64:
#         return "adult"
#     elif int(a) >= 65:
#         return "senior"
# b=sortage(age)
# print(b)
# def quad(n):
#     return n*4
# d=quad(594)
# print(d)
# def sq(n):
#     return n*n
# def tasques(n1,n2):
#     e=sq(n1)
#     f=sq(n2)
#     g=e+f
#     return g
# h=tasques(2,5)
# print(h)
wide=300
high=600
randomlistofcolor=["pink","orange","lime","cyan","brown","navy","red"]
import turtle
import random
def start(sw,sh):
    window = turtle.Screen()
    window.setup(width=sw,height=sh)
    return window
s=start(wide,high)
def makegooby():
    nam=turtle.Turtle()
    nam.shape("square")
    nam.color("cyan")
    return nam
g = makegooby()
# g.penup()

x = 5
y = 4

def moving(n,vex,vey):
    n.setx(n.xcor()+vex)
    n.sety(n.ycor()+vey)
def detectx(n,wide):
    if n.xcor() > wide/2 or n.xcor() < -wide/2:
        return True
def detecty(n,high):
    if n.ycor() > high/2 or n.ycor() < -high/2:
        return True
while True:
    moving(g,x,y)
    if detectx(g,wide) == True:
        #x=random.randint(1,10)
        x*= -1
        g.color(random.choice(randomlistofcolor))
    if detecty(g,high) == True:
        #y=random.randint(1,10)
        y*= -1
        g.color(random.choice(randomlistofcolor))
s.mainloop()