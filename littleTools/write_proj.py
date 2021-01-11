from osgeo import gdal,ogr,osr
import os

#打开文件
file_prj = r"C:\Users\wutian\Desktop\test\1.prj"

#定义坐标系
def defCoS(file,file_prj):
    #传进来一个shp文件，当前目录下新建pri文件，并写入beijing54坐标系

    #创建目标文件
    target = file.split('.')
    target = target[0]
    target = open(target + '.prj','w')
    #读取坐标并存入
    src = open(file_prj,'r')
    lines = src.readlines()
    target.write(lines[0])
def process_line(geom,trans,line):
    #对线进行投影变换
    print('1:',geom)
    n = geom.GetPointCount()
    for i in range(n):
        temp_x, temp_y = geom.GetX(i), geom.GetY(i)
        point = trans.TransformPoint(temp_x,temp_y)
        geom.SetPoint(i,point[0],point[1])
        line.AddPoint(point[0],point[1])
    print('2:',geom)
def beijing54TowebMercator(file,path):
    #将beijing54 转换为 WEB墨卡托

    # 支持中文路径
    gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8", "YES")
    # 属性表字段支持中文
    gdal.SetConfigOption("SHAPE_ENCODING", "GBK")
 
    strVectorFile = path + ".shp"
    # 如果存在File，则删除
    if os.path.isfile(strVectorFile):
        os.remove(strVectorFile)
        os.remove(path + ".dbf")
        os.remove(path + ".shx")
        os.remove(path + ".prj")
 
    # 注册所有的驱动
    ogr.RegisterAll()
 
    # 创建ESRI的shp文件
    strDriverName = "ESRI Shapefile"
    oDriver = ogr.GetDriverByName(strDriverName)
    # print(oDriver)
    if oDriver == None:
        print(strDriverName, "驱动不可用！")
        return
 
    # 创建数据源
    oDS = oDriver.CreateDataSource(strVectorFile)
    # print(oDS)
    if oDS == None:
        print(strVectorFile, "创建文件失败！")
        return
 
    # 创建空间参考系
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(3857)
 
    # 创建图层
    papszLCO = []
    oLayer = oDS.CreateLayer("Line", srs, ogr.wkbLineString, papszLCO)
    if oLayer == None:
        print("图层创建失败")
        return
 
    # 创建属性表
    # FieldID的整型属性
    oFieldID = ogr.FieldDefn("FieldID", ogr.OFTInteger)
    oLayer.CreateField(oFieldID, 1)
 
    # FeatureName的字符型属性，字符长度为100
    oFieldName = ogr.FieldDefn("FieldName", ogr.OFTString)
    oFieldName.SetWidth(100)
    oLayer.CreateField(oFieldName, 1)
 
    oDefn = oLayer.GetLayerDefn()

    #转换
    beijing54 = osr.SpatialReference()
    beijing54.ImportFromEPSG(2437)
    web_mercator  = osr.SpatialReference()
    web_mercator.ImportFromEPSG(3857)
    trans = osr.CoordinateTransformation(beijing54, web_mercator)
    #打开文件，对所有几何形状进行投影转换
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataSource = driver.Open(file,1)
    if dataSource is None:
        print('can\'t open!')
        return
    layer = dataSource.GetLayer(0)      #打开图层
    feat = layer.GetNextFeature()
    i = 0
    while feat:

        #对每一个几何形状进行一次投影转换
        geom = feat.GetGeometryRef()

        #新建一条线段
        oFeaturePentagon = ogr.Feature(oDefn)
        oFeaturePentagon.SetField(0, i)
        i = i+1
        oFeaturePentagon.SetField(1, "线段")
        line = ogr.Geometry(ogr.wkbLineString)
        #投影转换线上的点
        process_line(geom,trans,line)

        oFeaturePentagon.SetGeometry(line)
        oLayer.CreateFeature(oFeaturePentagon)   
        feat = layer.GetNextFeature()
    dataSource.Destroy()        #释放文件
    print('done')

test = r"C:\Users\wutian\Desktop\test\2.shp"
path = r"C:\Users\wutian\Desktop\test\2_target"
beijing54TowebMercator(test,path)