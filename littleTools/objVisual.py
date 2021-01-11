import sys
import os
from vispy import scene, io
from PIL import ImageGrab
import time

def execute(input, output):
    try:
        fileList = os.listdir(input)
        # 跳出json数据
        for file in fileList:
            if ('.' in file) and (file.split('.')[1] == 'obj'):
                obj_file = input + '/' + file
                fileName = file.split('.')[0]
                break

        canvas = scene.SceneCanvas(keys='interactive', show=True)
        view = canvas.central_widget.add_view()
        verts, faces, normals, nothing = io.read_mesh(obj_file)
        mesh = scene.visuals.Mesh(vertices=verts, faces=faces, shading='smooth')
        view.add(mesh)
        view.camera = scene.TurntableCamera()
        view.camera.depth_value = 10
        
        canvas.app.run()
        pic = ImageGrab.grab()
        pic.save(output + '/' + fileName + '.jpg')

        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    if execute(sys.argv[1], sys.argv[2]) is True:
        print('ok')