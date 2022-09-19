# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 00:59:24 2022

@author: Gazel
"""

import os
import pyautogui
import time

#Allows locating of screenshot on both monitors
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

#Use to find mouse postion
#while True:
#    print(pyautogui.position())
#    time.sleep(2)

#Use to find size of gui, doesn't appear to respect multiple monitors in output
#print(pyautogui.size())

#Save Original mouse Pos to return to after actions
originalMousePos = pyautogui.position()

#Open something with cmd
os.system("cmd /c explorer.exe shell:appsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.mail")

#Wait for program to open
time.sleep(1)

#Right-click in middle of image
#pyautogui.click(2667, 331, button='right') #Hard Coded coordinates
#pyautogui.click(pyautogui.locateCenterOnScreen('img1.jpg', confidence=0.9, region=(2560, 0, 4479, 1079)), button='right') #Only check specific region
pyautogui.click(pyautogui.locateCenterOnScreen('img1.jpg', confidence=0.8), button='right')

#Left-click in middle of second image
#pyautogui.click(2696, 268, button='left') #Hard Coded coordinates
#pyautogui.click(pyautogui.locateCenterOnScreen('img2.jpg', confidence=0.9, region=(2560, 0, 4479, 1079)), button='left') #Only check specific region
pyautogui.click(pyautogui.locateCenterOnScreen('img2.jpg', confidence=0.8), button='left')

#Close the opened program
os.system("cmd /c taskkill /IM HxOutlook.exe /F")

#Return Mouse to Original Postion
pyautogui.moveTo(originalMousePos)