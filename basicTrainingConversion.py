import os
import h5py

dataFile = os.path.join('train', 'digitStruct.mat')
file = h5py.File(dataFile, 'r')

#Similar to a python dictionary, find the name and bounding boxes:
name = file['digitStruct/name']
boundingBox = file['digitStruct/bbox']

#Function to get the file name of specific image by index:
def getImageName(file, idx = 0):
    imageName = ''.join(map(chr, file[name[idx][0]][()].flatten()))
    return imageName

boxProperty = ['height', 'left', 'top', 'width', 'label']
def getImageBox(file, idx = 0):
    """
    file: h5py file
    idx: index of image
    return: dictionary
    """
    metaData = {key : [] for key in boxProperty}

    box = file[boundingBox[idx][0]]
    for key in box.keys():
        if box[key].shape[0] == 1:
            metaData[key].append(int(box[key][0][0]))
        else:
            for i in range(box[key].shape[0]):
                metaData[key].append(int(file[box[key][i][0]][()].item()))
    
    return metaData

#print(getImageName(file, 4458), getImageBox(file, 4458))