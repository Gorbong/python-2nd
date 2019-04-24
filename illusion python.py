from turtle import*


black = "#000000"
white = "#FFFFFF"
setup(1000,1000)
speed(2000)
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
      forward(5)
      left(90)
    end_fill()
def backLine(number):
    penup()
    bk(number*30)
    right(90)
    fd(30)
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
for i in range(7):
    for i in range(7):
        carre(white)
        fd(30)
        carre(black)
        fd(30)
    backLine(15)
    bk(30)
    for i in range(9):
        carre(black)
        fd(30)
        carre(white)
        fd(30)
    backLine(15)
    bk(30)

penup()
goto(170,320)
pendown()
littleCarre(white)


























