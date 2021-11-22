import os
import re
import numpy as np
from colors import *
import xml.etree.ElementTree as ET
from cairosvg import svg2png
import imageio
from PIL import Image

photo_path = os.path.join(os.getcwd(),'doge-tripping-ballz-copy.svg')

def replaceChars(s,i0,l,r):
    return s[:i0] + r + s[i0+l:]

def readColors(path):    
    tree = ET.ElementTree()
    root = tree.parse(path)
    colorDict = {}
    for child in root:
        label = '{http://www.inkscape.org/namespaces/inkscape}label'
        if label in child.attrib and child.attrib[label] == 'Image':
            for gc in child:
                id = gc.attrib['id']
                color = gc.attrib['style'].split(';')[0][5:]
                colorDict[id] = {"startColor":color}
    
    colorDict = {k:v for k,v in colorDict.items() if whiteish(v["startColor"],5) == False}
    return colorDict

def createSpectrumDictionary(path,stepNum):
    colorDict = readColors(path)
    colors = [hex_to_rgb(colorDict[i]["startColor"]) for i in colorDict]
    spectrumColorsRGB = fullSpectrum(colors,stepNum)
    spectrumColorsHEX = [rgb_to_hex(x) for x in spectrumColorsRGB]

    for c in colorDict:
        index = [i for i,v in enumerate(spectrumColorsHEX) if v == colorDict[c]["startColor"]][0]
        colorDict[c]["spectrumStartIndex"] = index
    return spectrumColorsHEX,colorDict

def writeAnimationString(id,colorList,startIndex):
    numSteps = len(colorList) + 1
    stepPercentages = np.linspace(0,100,numSteps,endpoint=True,dtype=int)
    stepColors = [colorList[(startIndex+i)%len(colorList)] for i in range(numSteps)]
    stepDict = dict(zip(stepPercentages,stepColors))
    percentageString = ""
    for i in stepDict:
        percentageString = percentageString + f'\t\t{i}% {{fill:{stepDict[i]}}}\n'
    animationStr = f"""

        #{id} {{animation: col{id} 8s linear infinite;}}

        @keyframes col{id} {{
        {percentageString}
        }}
    """
    return animationStr

def animateSVG(path):
    spectrumColors,spectrumDict = createSpectrumDictionary(path,1)
    print(spectrumColors)
    outPath = path.split('.')[0] + "-ANIMATED.svg"
    tree = ET.ElementTree()
    ET.register_namespace("","http://www.w3.org/2000/svg")
    root = tree.parse(path)
    for child in root:
        label = '{http://www.inkscape.org/namespaces/inkscape}label'
        if label in child.attrib and child.attrib[label] == 'Image':
            for gc in child:
                id = gc.attrib['id']
                if id in spectrumDict:
                    styleAnimation = ET.SubElement(gc,'style')
                    styleAnimation.text = writeAnimationString(id,spectrumColors,spectrumDict[id]["spectrumStartIndex"])
    tree.write(outPath)

# test_photo_path = os.path.join(os.getcwd(),'doge-tripping-ballz-update.svg')
animateSVG(photo_path)


# tree = ET.ElementTree()
# 
# root = tree.parse(test_photo_path)
# namespace = root.tag[1:-4]
# ET.register_namespace('',namespace)
# for child in root:
#     if child.attrib['label'] == 'Image':
#         for gc in child:
#             if gc.attrib['id'] == 'path1109':
#                 # gcStyle = gc.attrib.pop('style')
#                 # print(gcStyle)
#                 styleAnimation = ET.SubElement(gc,'style')
#                 styleAnimation.text = animationStr

# tree.write(test_photo_path)
# p = root.findall("g[@id='g15']")
# print(p)
# print(doc.toprettyxml())
# for p in path_strings:
#     if p.getAttribute('id') == "path1109":
#         s = p.getElementsByTagName('style')[0]
#         print(s.text)
# print(e.getAttribute('style'))
# with open(test_photo_path,'w') as fs:
    # fs.write(doc.toxml())
    # fs.close()

def svgStuff():
    doc = minidom.parse(photo_path)
    path_strings = [path for path in doc.getElementsByTagName('path')]
    pattern = r'(?<=fill:).{7}'
    for p in path_strings:
        s = p.getAttribute('style')
        sSplits = s.split(';')
        sFill = sSplits[0]
        sFillColor = sFill.split(':')[1]
        newColor = "#ffddcc"
        newSplits = ['fill:'+newColor] + sSplits[1:]
        newStyle = ';'.join(newSplits)
        p.setAttribute("style",newStyle)
    for p in path_strings:
        print(p.getAttribute('style'))
