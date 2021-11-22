
# def writeImage(sourcePath,photo_text,writeFolder,spectrumDict,spectrumColorList,frameNum):
#     baseName = os.path.basename(sourcePath).split('.')[0]
#     writePath = os.path.join(writeFolder,f"{baseName}{frameNum}.png")
#     new_photo_text = photo_text
#     numLayers = len(spectrumColorList)
#     for i in spectrumDict:
#         s = spectrumDict[i]["spectrumStartIndex"] + frameNum
#         spectrumColor = spectrumColorList[s%numLayers]
#         new_photo_text = replaceChars(new_photo_text,i,7,spectrumColor)
#     # with open(writePath,'w') as file:
#         # file.write(new_photo_text)
#     svg2png(bytestring=new_photo_text,write_to=writePath)


# def generateImageStack(sourcePath,spectrumDict,spectrumColorList):
#     baseName = os.path.basename(sourcePath).split('.')[0]
#     photoStackDir = os.path.join(os.getcwd(),baseName+"_photoStack")
#     if not os.path.exists(photoStackDir):
#         os.mkdir(photoStackDir)
#     with open(sourcePath,'r') as file:
#         photo_text = file.read()
#         for i in range(len(spectrumColorList)):
#             writeImage(sourcePath,photo_text,photoStackDir,spectrumDict,spectrumColorList,i)
# # generateImageStack(photo_path,spectrumDict,spectrumColors)
# photoStackDir = os.path.join(os.getcwd(),"doge-tripping-ballz_photoStack")
# def getPhotoFilenames(dir):
#     files = os.listdir(dir)
#     filenames = []
#     for f in sorted(files,key=lambda x:int(x.split('.')[0].split('-')[-1][5:])):
#         filenames.append(os.path.join(dir,f))
#     return filenames

# compressedStackDir = os.path.join(os.getcwd(),'compressedStack')

# def compressImages(filenames,compressedStackDir):
    
#     if not os.path.exists(compressedStackDir):
#         os.mkdir(compressedStackDir)
#     for f in filenames:
#         img = Image.open(f).convert('RGB')
#         writePath = os.path.join(compressedStackDir,os.path.split(f)[1].split('.')[0]+'.jpg')
#         img.save(writePath,quality=5,optimize=True)

# def makeGIF(filenames):
#     gifPath = os.path.join(os.getcwd(),'doge-tripping-ballz.gif')
#     img, *imgs = [Image.open(f) for f in filenames[:10]]
#     img.save(fp=gifPath, format='GIF', append_images=imgs,save_all=True, duration=50, loop=0)
# uncompressedFiles = getPhotoFilenames(photoStackDir)
# compressedFiles = getPhotoFilenames(compressedStackDir)
# makeGIF(compressedFiles)
# compressImages(uncompressedFiles,compressedStackDir)

# img, *imgs = [Image.open(f).convert('RGB') for f in filenames[:10]]
# img.save(fp=gifPath, format='GIF', append_images=imgs,save_all=True, duration=50, loop=0)
# img = Image.open(filenames[0])
# rgb_im = img.convert('RGB')
# rgb_im.save(os.path.join(os.getcwd(),'compressed-doge.jpg'),quality=5,optimize=True)
# with imageio.get_writer(gifPath, mode='I', duration=.05) as writer:
    # for filename in filenames:
        # print(filename)
        # image = imageio.imread(filename)
        # writer.append_data(image)
# for filename in filenames:
    # images.append(imageio.imread(filename))
# imageio.mimsave(os.path.join(os.getcwd(),'doge-tripping-ballz.gif'), images, duration=.05)

# for i in spectrumDict:
    # print(spectrumDict[i]["startColor"])
    # print(spectrumColors[spectrumDict[i]["spectrumStartIndex"] + 1])
    # print('')

# print(spectrumColorsHEX)
# print(spectrumColorsHEX)
# print(45%40)
# print(len(spectrumColorsHEX))

# output_path = os.path.join(os.getcwd(),'doge-tripping-ballz-update.svg')
# png_path = os.path.join(os.getcwd(),'doge-tripping-ballz-update.png')
# original_png_path = os.path.join(os.getcwd(),'doge-tripping-ballz.png')
# images = []
# filenames = [original_png_path,png_path]


# original = open(photo_path,'r').read()
# svg2png(bytestring=original,write_to=original_png_path)

# with open(output_path,'w') as file:
#     file.write(output)