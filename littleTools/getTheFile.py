'''
 * @Author: wutian 
 * @Date: 2020-08-30 21:34:25 
 * @Last Modified by:   wutian 
 * @Last Modified time: 2020-08-30 21:34:25 
 * 获取路径下的所有文件名
'''
# -*- encoding:utf-8 -*-
import os

def getfiles(path,res):    #传进路径
    files = os.listdir(path)    #得到所有文件
    for file in files:
        file = path + '/' + file
        if os.path.isdir(file):
            getfiles(file,res)
        else:
            res.append(file)           

def path_file_other():
    '''
    1. path 路径就返回该路径下的所有文件
    2. file 文件就返回文件
    3. 其它就选择是否再创立该文件
    '''
    filename = input('Enter your path：')
    if os.path.isdir(filename):     #判断是否是路径
        print('it\'s a directory.')
        res = []        #保存所有文件并返回
        getfiles(filename,res)
        for file in res:        #可以不输出
            print(file)
        return res
    elif os.path.isfile(filename):      #判断是否是文件
        print('it\'s a file.')
        return filename
    else:
        print(filename + ' is not right.')
        if(input('make a directory named filename?')):
            os.makedirs(filename)
    


if __name__ == '__main__':
    path_file_other()
