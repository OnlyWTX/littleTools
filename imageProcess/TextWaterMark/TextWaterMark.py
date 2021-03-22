from PIL import Image, ImageFilter, ImageFont, ImageDraw
import matplotlib.font_manager as fm # to create font
import os
import sys

def execute(input, output, font='Helvetica', text='test', font_size=40, font_color=(0, 0, 0, 255)):
    fileList = os.listdir(input)
    for file in fileList:
        if('.' in file) and (file.split('.')[1] == 'png' or file.split('.')[1] == 'jpg'):
            imgFile = input + '/' + file
            break

    image = Image.open(imgFile).convert('RGBA') 
    txt = Image.new('RGBA', image.size, (0, 0, 0, 0))
    bw, bh = txt.size
    font = ImageFont.truetype(fm.findfont(fm.FontProperties(family='DejaVu Sans')),font_size)
    fw, fh = font.getsize(text)
    size = (bw - fw, 0)
    d = ImageDraw.Draw(txt, 'RGBA')
    d.text(size, text, fill=font_color, font=font)
    image = Image.alpha_composite(image.convert('RGBA'), txt)
    image.save(output + '/' + 'res.png')
    return True

if __name__ == '__main__' :
    if execute(sys.argv[1], sys.argv[2], sys.argv[3]) is True:
        print('ok')