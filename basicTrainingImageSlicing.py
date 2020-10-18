import numpy as np
import basicTrainingConversion
import os
import h5py
import matplotlib.pyplot as plt
from PIL import Image 

dataFile = os.path.join('train', 'digitStruct.mat')
file = h5py.File(dataFile, 'r')

#Function that plots and displays images with bounding boxes
def displayBoundingBox(img, dict):
    """
    Dictionary keys:
    - height
    - left
    - top
    - width
    - label
    """
    length = len(dict['label'])
    #fig, ax = plt.subplots(length + 1, 1, sharey=True)
    plt.imshow(img)
    plt.show()

    """
    1.png 
    {
        'height': [219, 219], 
        'left': [246, 323], 
        'top': [77, 81], 
        'width': [81, 96], 
        'label': [1, 9]
    }
    """
    for i in range(length):
        left = dict['left'][i]
        top = dict['top'][i]
        right = left + dict['width'][i]
        bottom = top + dict['height'][i]
        cropped = img.crop((left, top, right, bottom)) 
        plt.imshow(cropped)
        plt.show()


dict = basicTrainingConversion.getImageBox(file, 0)
img = Image.open('train/1.png')
displayBoundingBox(img, dict)