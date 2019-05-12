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

def carre1(pixelColor):
    if pixelColor == white:
        carre(black)
    penup()
    fd(5)
    left(90)
    fd(5)
    right(90)
    pendown()
    littleCarre(pixelColor)
    penup()
    left(90)
    fd(13)
    right(90)
    fd(13)
    pendown()
    littleCarre(pixelColor)
    penup()
    fd(12)
    right(90)
    fd(18)
    left(90)
    pendown()

def carre2(pixelColor):
    if pixelColor == white:
        carre(black)
    penup()
    fd(5)
    left(90)
    fd(5)
    right(90)
    pendown()
    littleCarre(pixelColor)
    penup()
    fd(13)
    pendown()
    littleCarre(pixelColor)
    penup()
    fd(12)
    right(90)
    fd(5)
    left(90)
    pendown()

def carre3(pixelColor):
    if pixelColor == white:
        carre(black)
    penup()
    fd(10)
    left(90)
    fd(18)
    pendown()
    littleCarre(pixelColor)
    penup()
    right(90)
    fd(10)
    right(90)
    fd(13)
    left(90)
    pendown()
    littleCarre(pixelColor)
    penup()
    fd(10)
    right(90)
    fd(5)
    left(90)
    pendown()

def carre4(pixelColor):
    if pixelColor == white:
        carre(black)
    penup()
    fd(18)
    left(90)
    fd(6)
    right(90)
    pendown()
    littleCarre(pixelColor)
    penup()
    left(90)
    fd(12)
    right(90)
    pendown()
    littleCarre(pixelColor)
    penup()
    fd(12)
    right(90)
    fd(18)
    left(90)
    pendown()

def carre5(pixelColor):
    if pixelColor == white:
        carre(black)
    penup()
    fd(6)
    left(90)
    fd(6)
    right(90)
    pendown()
    littleCarre(pixelColor)
    penup()
    left(90)
    fd(12)
    right(90)
    pendown()
    littleCarre(pixelColor)
    penup()
    fd(24)
    right(90)
    fd(18)
    left(90)
    pendown()

def carre6(pixelColor):
    if pixelColor == white:
        carre(black)
    penup()
    fd(5)
    left(90)
    fd(18)
    right(90)
    pendown()
    littleCarre(pixelColor)
    penup()
    fd(13)
    pendown()
    littleCarre(pixelColor)
    penup()
    fd(12)
    right(90)
    fd(18)
    left(90)
    pendown()

def illusion():
    for i in range(8):
        carre(black)
        fd(30)
        penup()
        fd(30)
        pendown()
    backLine(15)

#line1
    bk(30)
    for i in range(3):
        fd(30)
        carre(black)
        fd(30)
    carre1(black)
    carre2(white)
    carre3(black)
    for i in range(3):
        carre(black)
        fd(30)
        fd(30)
    backLine(15)

#line2
    for i in range(2):
        carre(black)
        fd(30)
        fd(30)
    carre1(white)
    carre1(black)
    carre1(white)
    carre2(black)
    carre3(white)
    carre3(black)
    carre3(white)
    for i in range(2):
        fd(30)
        carre(black)
        fd(30)
    backLine(15)

#line3
    fd(30)
    carre(black)
    fd(30)
    fd(30)
    carre1(white)
    carre1(black)
    carre1(white)
    carre1(black)
    carre2(white)
    for i in range(2) :
        carre3(black)
        carre3(white)
    carre(white)
    fd(30)
    carre(black)
    fd(30)
    backLine(14)

#line4
    carre(black)
    fd(30)
    fd(30)
    for i in range (2) :
        carre1(white)
        carre1(black)
    carre1(white)
    carre2(black)
    for i in range (2) :
        carre3(white)
        carre3(black)
    carre3(white)
    fd(30)
    carre(black)
    fd(30)
    backLine(15)

#line5

    fd(30)
    carre(black)
    fd(30)
    for i in range (2) :
        carre1(black)
        carre1(white)
    carre1(black)
    carre2(white)
    for i in range(2):
        carre3(black)
        carre3(white)
    carre3(black)
    carre(black)
    fd(30)
    backLine(14)
#line6

    carre(black)
    fd(30)
    for i in range(3):
        carre1(black)
        carre1(white)
    carre2(black)
    for i in range(3):
        carre3(white)
        carre3(black)
    carre(black)
    fd(30)
    backLine(15)
#line7
    fd(30)
    for i in range(3):
        carre4(white)
        carre4(black)
    carre(black)
    fd(30)
    for i in range(3):
        carre5(black)
        carre5(white)
    fd(30)
    backLine(15)
#line8
    carre(black)
    fd(30)
    for i in range(3):
        carre3(black)
        carre3(white)
    carre6(black)
    for i in range(3):
        carre1(white)
        carre1(black)
    carre(black)
    fd(30)
    backLine(15)
#line9
    fd(30)
    carre(black)
    fd(30)
    for i in range (2) :
        carre1(black)
        carre1(white)
    carre1(black)
    carre6(white)
    for i in range(2):
        carre3(black)
        carre3(white)
    carre3(black)
    carre(black)
    fd(30)
    backLine(14)
#line10
    carre(black)
    fd(30)
    fd(30)
    for i in range (2) :
        carre3(white)
        carre3(black)
    carre3(white)
    carre6(black)
    for i in range (2) :
        carre1(white)
        carre1(black)
    carre3(white)
    fd(30)
    carre(black)
    fd(30)
    backLine(15)


#line11
    fd(30)
    carre(black)
    fd(30)
    fd(30)
    carre3(white)
    carre3(black)
    carre3(white)
    carre3(black)
    carre6(white)
    for i in range(2) :
        carre1(black)
        carre1(white)
    carre(white)
    fd(30)
    carre(black)
    fd(30)
    backLine(14)

#line12
    for i in range(2):
        carre(black)
        fd(30)
        fd(30)
    carre3(white)
    carre3(black)
    carre3(white)
    carre6(black)
    carre1(white)
    carre1(black)
    carre1(white)
    for i in range(2):
        fd(30)
        carre(black)
        fd(30)
    backLine(14)

#line13
    bk(30)
    for i in range(3):
        fd(30)
        carre(black)
        fd(30)
    carre3(black)
    carre6(white)
    carre1(black)
    for i in range(3):
        carre(black)
        fd(30)
        fd(30)
    backLine(15)

    for i in range(8):
        carre(black)
        fd(30)
        penup()
        fd(30)
        pendown()
    backLine(15)


penup()
goto(-500,200)
pendown()
illusion()

































































