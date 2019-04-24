﻿from turtle import *


brown = "#463525"
red = "#E51522"
black = "#000000"
white = "#FFFFFF"
darkSkin = "#E7AE38"
lightSkin = "#F8D898"
grey = "#BBBBBB"
red = "#E51522"
darkRed = "#A01916"
lightRed = "#ED7074"
pixelLength = 10
setup(600,1000)
speed(1000000000)
hideturtle()

def drawPixels(number, pixelColor):
    for i in range(number):
        drawPixel(pixelColor)

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

def drawPixel(pixelColor):
    color(pixelColor, pixelColor)
    begin_fill()
    for i in range(4):
      forward(pixelLength)
      left(90)
    end_fill()
    advance()

drawPixels(5,black)
backLine(7)
drawPixels(2,black)
drawPixels(5,red)
drawPixels(2,black)
backLine(10)
drawPixels(1,black)
drawPixels(5,red)
drawPixels(4,white)
drawPixels(1,black)
backLine(11)
drawPixels(1,black)
drawPixels(4,red)
drawPixels(2,white)
drawPixels(1,red)
drawPixels(1,white)
drawPixels(1,red)
drawPixels(1,white)
drawPixels(1,black)
backLine(13)
drawPixels(1,black)
drawPixels(5,red)
drawPixels(1,white)
drawPixels(4,red)
drawPixels(1,white)
drawPixels(1,black)
backLine(13)
drawPixels(1,black)
drawPixels(5,red)
drawPixels(1,white)
drawPixels(4,brown)
drawPixels(4,black)
backLine(16)
drawPixels(1,black)
drawPixels(5,red)
drawPixels(2,brown)
drawPixels(8,red)
drawPixels(1,black)
backLine(17)
drawPixels(1,black)
drawPixels(4,red)
drawPixels(1,brown)
drawPixels(3,red)
drawPixels(2,brown)
drawPixels(2,black)
drawPixels(3,red)
drawPixels(1,black)
backLine(18)
drawPixels(1,black)
drawPixels(4,red)
drawPixels(1,black)
drawPixels(2,red)
drawPixels(2,brown)
drawPixels(1,darkSkin)
drawPixels(1,brown)
drawPixels(1,darkSkin)
drawPixels(4,black)
backLine(18)
drawPixels(1,black)
drawPixels(4,red)
drawPixels(1,black)
drawPixels(1,red)
drawPixels(2,brown)
drawPixels(5,darkSkin)
drawPixels(1,black)
backLine(15)
drawPixels(1,black)
drawPixels(3,red)
drawPixels(3,black)
drawPixels(4,darkSkin)
drawPixels(1,black)
drawPixels(1,darkSkin)
drawPixels(3,black)
backLine(16)
drawPixels(1,black)
drawPixels(3,red)
drawPixels(2,black)
drawPixels(2,brown)
drawPixels(1,darkSkin)
drawPixels(2,lightSkin)
drawPixels(1,black)
drawPixels(1,darkSkin)
drawPixels(1,lightSkin)
drawPixels(2,darkSkin)
drawPixels(1,black)
backLine(17)
drawPixels(1,black)
drawPixels(2,red)
drawPixels(1,black)
drawPixels(2,lightSkin)
drawPixels(1,brown)
drawPixels(2,black)
drawPixels(6,lightSkin)
drawPixels(1,darkSkin)
drawPixels(1,black)
backLine(16)
drawPixels(1,black)
drawPixels(1,red)
drawPixels(1,black)
drawPixels(1,darkSkin)
drawPixels(1,lightSkin)
drawPixels(2,darkSkin)
drawPixels(4,lightSkin)
drawPixels(2,darkSkin)
drawPixels(1,lightSkin)
drawPixels(1,darkSkin)
drawPixels(1,black)
backLine(15)
drawPixels(3,black)
drawPixels(1,lightSkin)
drawPixels(4,darkSkin)
drawPixels(1,lightSkin)
drawPixels(3,darkSkin)
drawPixels(2,black)
backLine(12)
drawPixels(3,black)
drawPixels(5,darkSkin)
drawPixels(2,black)
backLine(7)
drawPixels(1,black)
drawPixels(1,brown)
drawPixels(1,darkSkin)
drawPixels(1,brown)
drawPixels(1,black)
backLine(5)
drawPixels(1,black)
drawPixels(1,darkSkin)
drawPixels(1,lightSkin)
drawPixels(2,darkSkin)
drawPixels(1,black)
backLine(6)
drawPixels(1,black)
drawPixels(1,lightSkin)
drawPixels(1,brown)
drawPixels(2,darkSkin)
drawPixels(2,black)
backLine(8)
drawPixels(1,black)
drawPixels(1,darkSkin)
drawPixels(1,lightSkin)
drawPixels(1,brown)
drawPixels(1,darkSkin)
drawPixels(1,brown)
drawPixels(2,white)
drawPixels(4,black)
backLine(12)
drawPixels(1,black)
drawPixels(1,darkSkin)
drawPixels(1,lightSkin)
drawPixels(1,darkSkin)
drawPixels(1,black)
drawPixels(3,white)
drawPixels(1,black)
drawPixels(2,lightSkin)
drawPixels(1,black)
backLine(11)
drawPixels(1,black)
drawPixels(2,darkSkin)
drawPixels(1,black)
drawPixels(2,white)
drawPixels(1,black)
drawPixels(2,darkSkin)
drawPixels(1,black)
backLine(9)
drawPixels(8,black)
backLine(7)
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
