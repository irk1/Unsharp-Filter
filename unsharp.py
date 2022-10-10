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
gaussX = 0
gaussY = 0
gaussZ = 0
wt1 = 0
wt2 = 0
gammaValue = 0

val = 0
layout = [
    [sg.Text("Gaussian kernel size")],
    [sg.Slider(range=(0, 10), default_value=gaussX, size=(50, 10), orientation="h",
                enable_events=True, key="slider0",resolution = 0.1)],
    [sg.Spin(values=[i for i in range(10)], initial_value=gaussX, size=(8, 4),
              enable_events=True, key="spin",)],
    [sg.Text("Σx")],
    [sg.Slider(range=(0, 10), default_value=val, size=(50, 10), orientation="h",
                enable_events=True, key="slider1",resolution = 0.1)],
    [sg.Spin(values=[i for i in range(10)], initial_value=val, size=(8, 4),
              enable_events=True, key="spin")],
    [sg.Text("Σy")],
    [sg.Slider(range=(0, 10), default_value=val, size=(50, 10), orientation="h",
                enable_events=True, key="slider2",resolution = 0.1)],
    [sg.Spin(values=[i for i in range(10)], initial_value=val, size=(8, 4),
              enable_events=True, key="spin")],
    [sg.Text("Weight 1")],
    [sg.Slider(range=(0, 10), default_value=val, size=(50, 10), orientation="h",
                enable_events=True, key="slider3",resolution = 0.1)],
    [sg.Spin(values=[i for i in range(10)], initial_value=val, size=(8, 4),
              enable_events=True, key="spin")],
    [sg.Text("Weight 2")],
    [sg.Slider(range=(0, 10), default_value=val, size=(50, 10), orientation="h",
                enable_events=True, key="slider4",resolution = 0.1)],
    [sg.Spin(values=[i for i in range(10)], initial_value=val, size=(8, 4),
              enable_events=True, key="spin")],
    [sg.Text("Gamma value")],
    [sg.Slider(range=(0, 10), default_value=val, size=(50, 10), orientation="h",
                enable_events=True, key="slider5",resolution = 0.1)],
    [sg.Spin(values=[i for i in range(10)], initial_value=val, size=(8, 4),
              enable_events=True, key="spin")],
    [sg.Button("Submit",enable_events = True, key ="submit")]
]


def Unsharp():

    #import original and duplicate
    img = cv2.imread(file)
    os.chdir(directory)
    cv2.imwrite(file1, img)
    #apply guassiun blur to copy of original
    img1 = cv2.imread(file1)
    Gaussian = cv2.GaussianBlur(img1 , (gaussX, gaussY), gaussZ)
    #cv2.imshow('Gaussian Blurring', Gaussian)
    #invert the blurred copy
    img_not = cv2.bitwise_not(Gaussian)
    #cv2.imshow('blurred/inverted', img_not)
    #overlay onto the original
    weightedSum = cv2.addWeighted(img1, wt1, img_not, wt2, gammaValue)
    '''
    Syntax: cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)
    Parameters:
    img1: First Input Image array(Single-channel, 8-bit or floating-point)
    wt1: Weight of the first input image elements to be applied to the final image
    img2: Second Input Image array(Single-channel, 8-bit or floating-point)
    wt2: Weight of the second input image elements to be applied to the final image
    gammaValue: Measurement of light
    '''
    cv2.imshow('subtracted', weightedSum)
    cv2.imshow('original', img)
    cv2.imwrite("weightedSum.png", weightedSum)
    return weightedSum
    return img
window = sg.Window("slider test", layout)
window.Finalize()
while True:
    event, values = window.Read()
    gaussX = values["slider0"]
    gaussY = values["slider1"]
    gaussZ = values["slider2"]
    wt1 = values["slider3"]
    wt2 = values["slider4"]
    gammaValue = values["slider5"]
    print(gaussX)
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
        gaussX = values["slider0"]
        gaussY = values["slider1"]
        gaussZ = values["slider2"]
        wt1 = values["slider3"]
        wt2 = values["slider4"]
        gammaValue = values["slider5"]
        Unsharp()



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
