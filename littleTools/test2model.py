import math
pi = 3.1415926
Isc = 1367
Dn=input("请输入一个整数\n")
L=input("请输入纬度\n")
ws = 1.0/math.cos(-math.tan(L)*math.tan(deta))
deta =  23.45*math.sin(360*(284+Dn)/365.0)
H0 = 24/pi*Isc*(1+0.33*math.cos(360*Dn/365))*(math.cos(L)*math.cos(deta)*math.sin(ws)+2*pi*ws/360*math.sin(L)*math.sin(deta))
S0 = 2.0/15*ws

p1 = 0.23
p2 = 0.48
print('H/H0 = p1+p2*S/S0')
print('H0 = '+H0)
print('S0 = '+S0)
print('p1= '+p1)
print('p2= '+p2)
