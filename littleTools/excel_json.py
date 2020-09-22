'''
 * @Author: wutian 
 * @Date: 2020-08-30 17:04:31 
 * @Last Modified by:   wutian 
 * @Last Modified time: 2020-08-30 17:04:31 
 *将excel转为json文件
'''
# -*- coding:UTF-8 -*-
import xlrd
import xlwt
import json
import os
import re

def temp_dict(temp):
    #一行的数据转为一个dict格式
    dict1 = {}      #将一行数据转为一个字典
    dict2 = {}      #将作者一栏也设置为字典格式
    dict1['reference'] = temp[2]
    dict1['classifications'] = [temp[0]]
    dict1['name'] = temp[1]
    dict1['decription'] = temp[3]
    dict1['detail'] = ''        #格式中有detail，但是数据中没有detail数据
    if temp[4] != '' or temp[5] !='' or temp[6] != '':       #作者存在的情况
        dict2['name'] = temp[4]
        dict2['email'] = temp[5]
        dict2['homepage'] = temp[6]
        dict1['authorship'] = dict2
    return dict1

def load_cell(file,res,index):
    #读取一个excel中每一个有用的单元格
    book = xlrd.open_workbook(file)     #打开文件
    table = book.sheets()[0]        #获取第一个工作表
    nrows,ncols = table.nrows,table.ncols   #获取行列数
    clsname = 'no_class'
    for i in range(1,nrows):        #从第二行开始，每次读倒数七个单元格
        temp = table.row_values(i,ncols-7,ncols)
        if temp[0] != '':       #因为类别合并单元格了，只能读一次，后面的单元格也是这个类别，保存下来
            clsname = temp[0]
        else:                   #类别为空的情况
            temp[0] = clsname
        if temp[1] != '':       #名称不是空的单元格，代表数据存在
            res.append(temp_dict(temp))
            index = index+1
    return index


def get_files(path,files):
    #根据路径保存该路径下面所有文件到files
    allfiles = os.listdir(path)     #得到所有文件
    for file in allfiles:
        temp = path + '/' +file
        if os.path.isdir(temp):         #文件夹的情况，继续找文件
            get_files(temp,files)
        elif os.path.isfile(temp) and re.search('.xlsx',temp):  #excel文件
            files.append(temp)

if __name__ == '__main__':
    files = []        #保存所有excel文件
    path = input('Enter your path(文件夹的绝对路径):')
    get_files(path,files)       #得到所有文件
    res = []            #保存所有结果
    index = 1
    for file in files:
        print(file+'   文件从序号%d'%index+'开始',end=',')
        index = load_cell(file,res,index)
        print('到序号%d'%index+'结束')
    with open("data1.json", 'w', encoding='utf-8') as f:     #存入json文件中
        json.dump(res, f, ensure_ascii=False)