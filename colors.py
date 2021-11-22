import numpy as np
from tsp import *

def hex_to_rgb(hex):
    hexVal = hex.lstrip('#')
    rgbVal = tuple(int(hexVal[i:i+2],16) for i in (0,2,4))
    return rgbVal

def rgb_to_hex(rgb):
    hexVal = '#%02x%02x%02x' % rgb
    return hexVal

def numSpread(startNum,endNum,stepCount):
    nums = np.linspace(startNum,endNum,stepCount,endpoint=False,dtype=int)
    return nums

def colorSpread(startColor,endColor,stepCount):
    colors = list(zip(*[numSpread(startColor[i],endColor[i],stepCount) for i in (0,1,2)]))
    return colors

def colorDistance(color1,color2):
    distance = int(np.sqrt(np.sum([(color1[i] - color2[i])**2 for i in (0,1,2)])))
    return distance

def colorDistanceArray(colorList):
    numColors = len(colorList)
    distanceArray = np.zeros((numColors,numColors))
    i = 0
    while i < numColors - 1:
        j = i + 1
        while j < numColors:
            distanceArray[i][j] = colorDistance(colorList[i],colorList[j])
            # val = colorList
            j += 1
        # print(colorList[i])
        i += 1
    return distanceArray + distanceArray.T

def sortColors(colorList):
    distanceArray = colorDistanceArray(colorList)
    sortedColorList = [colorList[i] for i in solveTSP(distanceArray,0)]
    return sortedColorList

def fullSpectrum(colorList,stepCount):
    sortedColorList = sortColors(colorList)
    sortedColorList.append(sortedColorList[0])
    spectrumColorList = []
    for i in range(len(sortedColorList)-1):
        spectrumColorList.extend(colorSpread(sortedColorList[i],sortedColorList[i+1],stepCount))
    return spectrumColorList

def whiteish(color,threshold):
    colorRGB = hex_to_rgb(color)
    if colorDistance(colorRGB,(255,255,255)) <= threshold:
        return True
    else:
        return False

# print(whiteish("#fdfdfd",5))

# colorList = [(1,2,3),(50,30,20),(100,120,40),(240,200,50),(240,203,56),(120,120,230)]
# arr = colorDistanceArray(colorList)
# print(arr)
# print(colorTSP(arr))
