from xml.dom.minidom import parse

fileName = open(r'C:\Users\wutian\Desktop\res.txt','w')
domTree = parse(r"C:\Users\wutian\Desktop\dem_data.xml")
dataSet = domTree.documentElement
xdo = dataSet.getElementsByTagName('XDO')
index = 0
length = xdo.length
while index < length:
    if xdo[index].hasAttribute('kernelType') and xdo[index].getAttribute('kernelType') == 'list':
        break
    if xdo[index].hasAttribute('value'):
        fileName.write(xdo[index].getAttribute('name') + '\t' + xdo[index].getAttribute('value') + '\n')
    index += 1

while index< length:
    if xdo[index].hasAttribute('value'):
        fileName.write(xdo[index].getAttribute('value') + '\n')
    index += 1
