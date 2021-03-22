from PIL import Image
import os
import sys

def execute(method, input, output):
    fileList = os.listdir(input)
    for file in fileList:
        if('.' in file) and (file.split('.')[1] == 'png' or file.split('.')[1] == 'jpg'):
            imgFile = input + '/' + file
            fileName = file.split('.')[0]
            break
    
    im = Image.open(imgFile)
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 30), subplot_kw={'xticks': [], 'yticks': []})
    fig.subplots_adjust(hspace=0.05, wspace=0.05)
    ax.set_title(str(interp_method), size=20)
    plt.tight_layout()

    im_g.save(output + '/' + fileName + '_res.png')
    return True

if __name__ == '__main__' :
    if execute(sys.argv[1], sys.argv[2], sys.argv[3]) is True:
        print('ok')