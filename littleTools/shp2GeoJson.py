import os
import shapefile
from json import dumps

def shpToGeoJson(file):
    #传入一个文件，在该目录下转换成geojson文件
    if file[-4:] != '.shp' and file[-4:] != '.SHP':
        print(file,' is not a shape file.')
        return
    reader = shapefile.Reader(file)
    fields = reader.fields[1:]
    field_names = [field[0] for field in fields]
    buffer = []
    for sr in reader.shapeRecords():
        atr = dict(zip(field_names, sr.record))
        geom = sr.shape.__geo_interface__
        buffer.append(dict(type="Feature", geometry=geom, properties=atr))
    
    temp = os.path.splitext(file)
    res = os.path.join(temp[0],'.json')
    geojson = open(res,'w',encoding='gbk')
    geojson.write(dumps({"type": "FeatureCollection","features": buffer}, indent=4) + '\n')
    geojson.close()
    print('Done.')

if __name__ == "__main__":
    file = input('Enter your file:')
    shpToGeoJson(file)