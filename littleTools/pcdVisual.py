import sys
import os
import numpy as np
import open3d as o3d
from PIL import ImageGrab

def execute(input, output):
    try:
        fileList = os.listdir(input)
        # 跳出json数据
        for file in fileList:
            if ('.' in file) and (file.split('.')[1] == 'pcd'):
                pcd_file = input + '/' + file
                fileName = file.split('.')[0]
                break
        pcd = o3d.io.read_point_cloud(pcd_file)
        o3d.visualization.draw_geometries([pcd], window_name="Open3D0")
        pic = ImageGrab.grab()
        pic.save(output + '/' + fileName + '.jpg')
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    if execute(sys.argv[1], sys.argv[2]) is True:
        print('ok')