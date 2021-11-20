import os
import re
from colors import *
import pyvips

photo_path = os.path.join(os.getcwd(),'doge-tripping-ballz.svg')

output = ''

with open(photo_path,'r') as file:
    photo_text = file.readlines()
    # colors = re.findall(r'(?<=fill:).{7}',photo_text)
    # rgbColors = [hex_to_rgb(c) for c in sorted(set(colors))]
    # sortedColors = [rgbColors[i] for i in sortColors(rgbColors)]
    for line in photo_text:
        pattern = re.findall(r'(?<=fill:).{7}',line)
        if pattern:
            line = re.sub(pattern[0],f'#ff{pattern[0][-4:]}', line)
            # print(line)
        output += line
    
output_path = os.path.join(os.getcwd(),'doge-tripping-ballz-update.svg')
png_path = os.path.join(os.getcwd(),'doge-tripping-ballz-update.png')
image = pyvips.Image.new_from_file(output_path,dpi=300)
image.write_to_file(png_path)
# with open(output_path,'w') as file:
#     file.write(output)