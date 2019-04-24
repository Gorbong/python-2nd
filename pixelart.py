from turtle import *


grey = "#BBBBBB"
red = "#E51522"
black = "#000000"
white = "#FFFFFF"
darkRed = "#A01916"
lightRed = "#ED7074"
pixelLength = 10
setup(1000,1000)

def drawPixel(pixelColor):
    color(pixelColor, pixelColor)
    begin_fill()
    for i in range(4):
      forward(pixelLength)
      left(90)
    end_fill()
    advance()

def advance():
    penup()
    fd(pixelLength)
    pendown()

def backLine(number):
    penup()
    bk(number*pixelLength)
    right(90)
    advance()
    left(90)
    pendown()

def drawPixels(number, pixelColor):
    for i in range(number):
        drawPixel(pixelColor)
speed(100000)

drawPixels(4,black)
backLine(6)
drawPixels(2,black)
drawPixels(1,red)
drawPixels(3,darkRed)
drawPixels(2,black)
backLine(9)
drawPixels(1,black)
drawPixels(2,red)
drawPixels(1,lightRed)
drawPixels(1,red)
drawPixels(4,darkRed)
drawPixels(1,black)
backLine(10)
drawPixels(1,black)
drawPixels(1,red)
drawPixels(1,lightRed)
drawPixels(1,white)
drawPixels(1,lightRed)
drawPixels(2,red)
drawPixels(2,darkRed)
drawPixels(1,black)
backLine(11)
drawPixels(1,black)
drawPixels(3,red)
drawPixels(1,lightRed)
drawPixels(1,darkRed)
drawPixels(2,red)
drawPixels(3,darkRed)
drawPixels(1,black)
backLine(12)
drawPixels(1,black)
drawPixels(4,red)
drawPixels(2,black)
drawPixels(4,darkRed)
drawPixels(1,black)
backLine(12)
drawPixels(2,black)
drawPixels(2,red)
drawPixels(1,black)
drawPixels(1,white)
drawPixels(1,grey)
drawPixels(1,black)
drawPixels(2,darkRed)
drawPixels(2,black)
backLine(12)
drawPixels(1,black)
drawPixels(1,white)
drawPixels(3,black)
drawPixels(2,grey)
drawPixels(3,black)
drawPixels(1,grey)
drawPixels(1,black)
backLine(12)
drawPixels(1,black)
drawPixels(3,white)
drawPixels(2,black)
drawPixels(2,black)
drawPixels(3,grey)
drawPixels(1,black)
backLine(11)
drawPixels(1,black)
drawPixels(5,white)
drawPixels(3,grey)
drawPixels(1,black)
backLine(9)
drawPixels(2,black)
drawPixels(4,grey)
drawPixels(2,black)
backLine(6)
drawPixels(4,black)






























































































