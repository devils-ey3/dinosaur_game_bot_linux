import pyscreenshot as ImageGrab
from PIL import ImageOps
import pyautogui
import numpy
import time

restart = 0
class Cordinates():
    replyButton = (342,420)
    dianasor = (172,425)


def restartGame():
    pyautogui.click(Cordinates.replyButton)
    global restart
    restart+=1
    

def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

def imageGrub():
    box = (Cordinates.dianasor[0]+68,Cordinates.dianasor[1],Cordinates.dianasor[0]+108,Cordinates.dianasor[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    colors = numpy.array(grayImage.getcolors())
    print(colors.sum())
    return colors.sum()

def main():
    restartGame()
    global restart
    while restart<2 :
        if (imageGrub()!=1447):
            jump()
            time.sleep(0.01)
main()
    