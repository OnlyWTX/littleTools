import sys
import os
import cv2

def meanBy3x3(i, j, width, height,data):
    sum = 0
    len = 0
    for m in range(i-1, i+1):
        for n in range(j-1, j+1):
            if m>=0 and n>=0 and m<width and n <height:
                sum += data[m][n]
                len += 1
    return sum/len

def execute(input, output):
    try:
        fileList = os.listdir(input)
        # 跳出json数据
        for file in fileList:
            if ('.' in file) and (file.split('.')[1] == 'tiff'):
                tiff_file = input + '/' + file
                fileName = file.split('.')[0]
                break
        with open(tiff_file, 'rb') as f:
            data = cv2.imread(tiff_file)
            for i in range(data.shape[0]):
                for j in range(data.shape[1]):
                    if sum(data[i][j]) == 0:
                        data[i][j] = meanBy3x3(i, j, data.shape[0], data.shape[1],data)
        cv2.imwrite(output + '/result.tiff',data)
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    if execute(sys.argv[1], sys.argv[2]) is True:
        print('ok')