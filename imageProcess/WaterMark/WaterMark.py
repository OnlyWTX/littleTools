from PIL import Image, ImageFilter
import os
import sys

def execute(input, output):
    fileList = os.listdir(input)
    files = []
    for file in fileList:
        if('.' in file) and (file.split('.')[1] == 'png' or file.split('.')[1] == 'jpg'):
            imgFile = input + '/' + file
            files.append(imgFile)

    if Image.open(files[0]).size[0] >= Image.open(files[1]).size[0]:
        image = files[0]
        imgFile = files[1]
    else:
        image = files[1]
        imgFile = files[0]       

    image = Image.open(image).convert('RGBA') 
    mark_im = Image.open(imgFile).convert('RGBA')
    bw, bh = image.size
    lw, lh = mark_im.size
    size = ((bw-lw, 0)
    layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
    layer.paste(mark_im, size)
    image = Image.alpha_composite(image.convert('RGBA'), layer)

    image.save(output + '/' + 'res.png')
    return True

if __name__ == '__main__' :
    if execute(sys.argv[1], sys.argv[2]) is True:
        print('ok')