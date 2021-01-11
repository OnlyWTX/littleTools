import sys
import os
import json
import xmltodict


def execute(input, output):      # 读入xml文件，转为json文件
    fileList = os.listdir(input)
    # 跳出json数据
    for file in fileList:
        if ('.' in file) and (file.split('.')[1] == 'xml'):
            json_file = input + '/' + file
            fileName = file.split('.')[0]
            break

    dict_str = open(json_file,'r', encoding='utf-8').read()
    data = xmltodict.parse(dict_str, xml_attribs=False)     # 去掉了属性
    with open(output + '/' + fileName + '.json','w', encoding='utf-8') as file:
        json.dump(data,file,ensure_ascii=False,indent=4)
    return True

if __name__ == "__main__":
    if execute(sys.argv[1], sys.argv[2]) is True:
        print('ok')