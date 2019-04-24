from turtle import*

black = "#000000"
white = "#FFFFFF"

setup(1000,1000)
speed(2000)
hideturtle()

def carre(pixelColor):
    color(pixelColor, pixelColor)
    begin_fill()
    for i in range(4):
      forward(30)
      left(90)
    end_fill()

def littleCarre(pixelColor):
    color(pixelColor, pixelColor)
    begin_fill()
    for i in range(4):
      forward(6)
      left(90)
    end_fill()

def backLine(number):
    penup()
    bk(number*30)
    right(90)
    fd(30)
    left(90)
    pendown()

def carre1W():
    penup()
    fd(5)
    left(90)
    fd(5)
    right(90)
    pendown()
    littleCarre(black)
    penup()
    left(90)
    fd(13)
    right(90)
    fd(13)
    pendown()
    littleCarre(black)
    penup()
    fd(12)
    right(90)
    fd(18)
    left(90)
    pendown()

def carre1B():
    carre(black)
    penup()
    fd(5)
    left(90)
    fd(5)
    right(90)
    pendown()
    littleCarre(white)
    penup()
    left(90)
    fd(13)
    right(90)
    fd(13)
    pendown()
    littleCarre(white)
    penup()
    fd(12)
    right(90)
    fd(18)
    left(90)
    pendown()

def carre2B():
    carre(black)
    penup()
    fd(5)
    left(90)
    fd(5)
    right(90)
    pendown()
    littleCarre(white)
    penup()
    fd(13)
    pendown()
    littleCarre(white)
    penup()
    fd(13)
    right(90)
    fd(5)
    left(90)
    pendown()

def carre2W():
    penup()
    fd(5)
    left(90)
    fd(5)
    right(90)
    pendown()
    littleCarre(black)
    penup()
    fd(13)
    pendown()
    littleCarre(black)
    penup()
    fd(13)
    right(90)
    fd(5)
    left(90)
    pendown()

def carre3B():
    carre(black)
    penup()
    fd(10)
    left(90)
    fd(18)
    pendown()
    littleCarre(white)
    penup()
    right(90)
    fd(10)
    right(90)
    fd(13)
    left(90)
    pendown()
    littleCarre(white)
    penup()
    fd(9)
    right(90)
    fd(4)
    left(90)
    pendown()

def carre3W():
    penup()
    fd(10)
    left(90)
    fd(18)
    pendown()
    littleCarre(black)
    penup()
    right(90)
    fd(10)
    right(90)
    fd(13)
    left(90)
    pendown()
    littleCarre(black)
    penup()
    fd(9)
    right(90)
    fd(5)
    left(90)
    pendown()

penup()
goto(-500,200)
pendown()
for i in range(8):
    carre(black)
    fd(30)
    carre(white)
    fd(30)
backLine(15)
bk(30)
for i in range(3):
    carre(white)
    fd(30)
    carre(black)
    fd(30)
carre1W()
carre2B()
carre3W()
for i in range(3):
    carre(black)
    fd(30)
    carre(white)
    fd(30)
backLine(15)
for i in range(2):
    carre(black)
    fd(30)
    carre(white)
    fd(30)
carre1B()
carre1W()
carre1B()
carre2W()
carre3B()
carre3W()
carre3B()
for i in range(2):
    carre(white)
    fd(30)
    carre(black)
    fd(30)
backLine(15)
carre(white)
fd(30)
carre(black)
fd(30)
carre(white)
fd(30)
carre1B()
carre1W()
carre1B()
carre1W()
carre2B()
for i in range(2) :
    carre3W()
    carre3B()
carre(white)
fd(30)
carre(black)
fd(30)
backLine(14)

carre(black)
fd(30)
carre(white)
fd(30)
for i in range (2) :
    carre1B()
    carre1W()
carre1B()
carre2W()
for i in range (2) :
    carre3B()
    carre3W()
carre3B()
for i in range (2) :
    carre(black)
    carre(white)
backLine(15)
for i in range (2) :
    carre(white)
    carre(black)
for i in range (2) :
    carre1W()
    carre1B()
carre1W()
carre2B()
for i in range(2):
    carre3W()
    carre3B()
carre3W()


































































