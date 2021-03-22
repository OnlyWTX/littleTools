from PIL import Image, ImageFilter
import os
import sys

def execute(input, output):
    fileList = os.listdir(input)
    for file in fileList:
        if('.' in file) and (file.split('.')[1] == 'png' or file.split('.')[1] == 'jpg'):
            imgFile = input + '/' + file
            fileName = file.split('.')[0]
            break
    im = Image.open(imgFile).convert('RGB').filter(ImageFilter.SHARPEN)
    im.save(output + '/' + fileName + '_res.png')
    return True

if __name__ == '__main__' :
    if execute(sys.argv[1], sys.argv[2]) is True:
        print('ok')