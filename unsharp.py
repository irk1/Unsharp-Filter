#https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Unsharp_mask_principle.svg/330px-Unsharp_mask_principle.svg.png
#unsharp mask
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import PySimpleGUI as sg
file = r"C:\Users\izzyk\OneDrive\Documents\GitHub\Unsharp-Filter\unsharp test photo.png"
directory = r"C:\Users\izzyk\OneDrive\Documents\GitHub\Unsharp-Filter"
filename = 'savedImage.png'
file1 = 'fileCopyTemp.png'
ksizeW = 7
ksizeH = 7
sigmax = 7
sigmay = 0
wt1 = 0.1
wt2 = 0.1
gammaValue = 0.1

val = 0
layout = [
    [sg.Text("Gaussian kernel size X")],
    [sg.Slider(range=(0, 10), default_value=ksizeW, size=(50, 10), orientation="h",
                enable_events=True, key="slider0",resolution = 1)],
    [sg.Text("Gaussian kernel size Y")],
    [sg.Slider(range=(0, 10), default_value=ksizeH, size=(50, 10), orientation="h",
                enable_events=True, key="sliderA",resolution = 1)],
    [sg.Text("Σx")],
    [sg.Slider(range=(0, 10), default_value=sigmax, size=(50, 10), orientation="h",
                enable_events=True, key="slider1",resolution = 1)],
    [sg.Text("Σy")],
    [sg.Slider(range=(0, 10), default_value=sigmay, size=(50, 10), orientation="h",
                enable_events=True, key="slider2",resolution = 0.1)],
    [sg.Text("Weight 1")],
    [sg.Slider(range=(0, 10), default_value=wt1, size=(50, 10), orientation="h",
                enable_events=True, key="slider3",resolution = 0.1)],
    [sg.Text("Weight 2")],
    [sg.Slider(range=(0, 10), default_value=wt2, size=(50, 10), orientation="h",
                enable_events=True, key="slider4",resolution = 0.1)],
    [sg.Text("Gamma value")],
    [sg.Slider(range=(0, 10), default_value=gammaValue, size=(50, 10), orientation="h",
                enable_events=True, key="slider5",resolution = 0.1)],
    [sg.Button("Submit",enable_events = True, key ="submit")]+[sg.Button("Close Display Windows",enable_events = True, key ="cv2Close")]+[sg.Button("Exit",enable_events = True,k="Exit")]

]


def Unsharp():
        #import original and duplicate
        img = cv2.imread(file)
        os.chdir(directory)
        cv2.imwrite(file1, img)
        #apply guassiun blur to copy of original
        img1 = cv2.imread(file1)
        Gaussian = cv2.GaussianBlur(img1 ,(ksizeW,ksizeH), sigmax)
        #cv2.imshow('Gaussian Blurring', Gaussian)
        #invert the blurred copy
        img_not = cv2.bitwise_not(Gaussian)
        #cv2.imshow('blurred/inverted', img_not)
        #overlay onto the original
        weightedSum = cv2.addWeighted(img1, wt1, img_not, wt2, gammaValue)

        Syntax: cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)
        '''Parameters:
        img1: First Input Image array(Single-channel, 8-bit or floating-point)
        wt1: Weight of the first input image elements to be applied to the final image
        img2: Second Input Image array(Single-channel, 8-bit or floating-point)
        wt2: Weight of the second input image elements to be applied to the final image
        gammaValue: Measurement of light
        '''
        cv2.imshow('subtracted', weightedSum)
        cv2.imshow('original', img)
        cv2.imwrite("weightedSum.png", weightedSum)

window = sg.Window("slider test", layout)
window.Finalize()
while True:
    event, values = window.Read()
    ksizeW = int(values["slider0"])
    ksizeH = int(values["sliderA"])
    sigmax = int(values["slider1"])
    sigmay = int(values["slider2"])
    wt1 = int(values["slider3"])
    wt2 = int(values["slider4"])
    gammaValue = int(values["slider5"])
#    print("\n \n ksizeW",ksizeW,",",ksizeH) #kernel size
#    print("\n sigmax",sigmax)#sigma x
#    print("\n sigmay",sigmay)#sigma y
#    print("\n wt1",wt1)
#    print("\n wt2",wt2)
#    print("\n gamma",gammaValue)
    if event == "Exit" or event == sg.WIN_CLOSED:

        break
    if event is not None:
        if event == "slider":
            val = values["slider"]
            window.Element("spin").Update(val)
        elif event == "spin":
            val = values["spin"]
            window.Element("slider").Update(val)
    if event == "submit":
        print("did stuff")
        ksizeW = int(values["slider0"])
        ksizeH = int(values["sliderA"])

        sigmax = int(values["slider1"])
        sigmay = int(values["slider2"])
        wt1 = int(values["slider3"])
        wt2 = int(values["slider4"])
        gammaValue = int(values["slider5"])
        Unsharp()
        '''
        #import original and duplicate
        img = cv2.imread(file)
        os.chdir(directory)
        cv2.imwrite(file1, img)
        #apply guassiun blur to copy of original
        img1 = cv2.imread(file1)
        Gaussian = cv2.GaussianBlur(img1 ,(ksizeW,ksizeH), sigmax)
        #cv2.imshow('Gaussian Blurring', Gaussian)
        #invert the blurred copy
        img_not = cv2.bitwise_not(Gaussian)
        #cv2.imshow('blurred/inverted', img_not)
        #overlay onto the original
        weightedSum = cv2.addWeighted(img1, wt1, img_not, wt2, gammaValue)

        Syntax: cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)
        Parameters:
        img1: First Input Image array(Single-channel, 8-bit or floating-point)
        wt1: Weight of the first input image elements to be applied to the final image
        img2: Second Input Image array(Single-channel, 8-bit or floating-point)
        wt2: Weight of the second input image elements to be applied to the final image
        gammaValue: Measurement of light

        cv2.imshow('subtracted', weightedSum)
        cv2.imshow('original', img)
        cv2.imwrite("weightedSum.png", weightedSum)
        '''
    if event == "cv2Close":
        cv2.destroyWindow('subtracted')
        cv2.destroyWindow('original')



window.close()
'''
os.chdir(directory)#change current directory to specified
print("Before saving image:")
print(os.listdir(directory))  #list files in directory

cv2.imwrite(filename, img)
cv2.imshow("image",img)
print("After saving image:")
print(os.listdir(directory))

print('Successfully saved')
'''
cv2.destroyAllWindows()
