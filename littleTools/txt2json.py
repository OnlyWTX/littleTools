import json
import re


file = open(r"F:\Download\ghcnd-stations.txt")
result = open(r'f:\download\res.json','w')
result.write('[')
line = file.readline()
while line:
    data1 = line[0:38]
    data2 = line[38:]
    
    res = {}


    # if data[0]:
    #     temp2 = re.sub(' +', ' ', data[0]).split(' ')
    #     res['staName'] = temp2[0]
    #     res['location'] = [temp2[2],temp2[1]]
    #     res['elevation'] = temp2[3]
    
    # res['area'] = data[1]
    # if len(data) > 2:
    #     if len(data) == 4:
    #         res['gsn'] = data[2]
    #         res['stationid'] = data[3]
    #     else:
    #         if data[2].isnumeric():
    #             res['stationid'] = data[2]
    #         else:
    #             res['gsn'] = data[2]
    json.dump(res,result)
    result.write(',')
    line = file.readline()

result.write(']')


