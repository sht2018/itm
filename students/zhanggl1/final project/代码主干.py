import cv2
import numpy as np
from matplotlib import pyplot as plt
import serial
import serial.tools.list_ports
import time
import mcpi.minecraft as minecraft
import mcpi.block as block

texture=51
light=89
fire=51
body=1
down= 152
middle=42
up=98
inside=5
bomb= 46
glass= 20
def attack(x,y,z):
                for cattack in range(8):
                        for dattack in range(5):
                                mc.setBlock(x-5-cattack,y+6,z-2+dattack,fire)
                                mc.setBlock(x-4-cattack,y+11,z-2+dattack,fire)
def set_head(x,y,z):
        mc.setBlock(x-3,y-1,z,down)
        for a in range(3):
                mc.setBlock(x-4,y-1,z-1+a,down)
                mc.setBlock(x-5,y-1,z-1+a,down)
        for b in range(5):
                mc.setBlock(x-6,y-1,z-2+b,down)
                mc.setBlock(x-7,y-1,z-2+b,down)
        for c in range(7):
                for d in range(7):
                        mc.setBlock(x-8-c,y-1,z-3+d,down)
        for d in range(2):
                mc.setBlock(x-3,y+d,z,down)
                mc.setBlock(x-4,y+d,z-1,down)
                mc.setBlock(x-4,y+d,z+1,down)
                mc.setBlock(x-5,y+d,z-1,down)
                mc.setBlock(x-5,y+d,z+1,down)
                mc.setBlock(x-6,y+d,z-2,down)
                mc.setBlock(x-6,y+d,z+2,down)
                mc.setBlock(x-7,y+d,z-2,down)
                mc.setBlock(x-7,y+d,z+2,down)
                for e in range(7):
                        mc.setBlock(x-8-e,y+d,z-3,down)
                        mc.setBlock(x-8-e,y+d,z+3,down)
        for iin in range(7):
                mc.setBlock(x-8-iin,y,z-2,down)
                mc.setBlock(x-8-iin,y,z+2,down)
        mc.setBlock(x-2,y+2,z,middle)
        mc.setBlock(x-3,y+2,z-1,middle)
        mc.setBlock(x-3,y+2,z+1,middle)
        mc.setBlock(x-4,y+2,z-1,middle)
        mc.setBlock(x-4,y+2,z+1,middle)
        mc.setBlock(x-5,y+2,z-2,middle)
        mc.setBlock(x-5,y+2,z+2,middle)
        mc.setBlock(x-6,y+2,z-2,middle)
        mc.setBlock(x-6,y+2,z+2,middle)
        for f in range(8):
                mc.setBlock(x-7-f,y+2,z-3,middle)
                mc.setBlock(x-7-f,y+2,z+3,middle)
        mc.setBlock(x-1,y+3,z,up)
        mc.setBlock(x-2,y+3,z,up)
        mc.setBlock(x-3,y+3,z-1,up)
        mc.setBlock(x-3,y+3,z+1,up)
        mc.setBlock(x-4,y+3,z-1,up)
        mc.setBlock(x-4,y+3,z+1,up)
        mc.setBlock(x-5,y+3,z-2,up)
        mc.setBlock(x-5,y+3,z+2,up)
        mc.setBlock(x-6,y+3,z-2,up)
        mc.setBlock(x-6,y+3,z+2,up)
        for g in range(8):
                mc.setBlock(x-7-g,y+3,z-3,up)
                mc.setBlock(x-7-g,y+3,z+3,up)
        mc.setBlock(x-1,y+4,z,up)
        mc.setBlock(x-2,y+4,z-1,up)
        mc.setBlock(x-2,y+4,z+1,up)
        mc.setBlock(x-3,y+4,z-1,up)
        mc.setBlock(x-3,y+4,z+1,up)
        mc.setBlock(x-4,y+4,z-2,up)
        mc.setBlock(x-4,y+4,z+2,up)
        mc.setBlock(x-5,y+4,z-2,up)
        mc.setBlock(x-5,y+4,z+2,up)
        for h in range(9):
                mc.setBlock(x-6-h,y+4,z-3,up)
                mc.setBlock(x-6-h,y+4,z+3,up)
        for i in range(3):
                mc.setBlock(x-i,y+5,z-1,up)
                mc.setBlock(x-i,y+5,z,up)
                mc.setBlock(x-i,y+5,z+1,up)
        mc.setBlock(x-2,y+5,z,light)
        for j in range(5):
                mc.setBlock(x-2-j,y+5,z-2,up)
                mc.setBlock(x-2-j,y+5,z+2,up)
        for k in range(5):
                mc.setBlock(x-6-k,y+5,z-3,up)
                mc.setBlock(x-6-k,y+5,z+3,up)
        for n in range(1):
                for l in range(5):
                        for m in range(3):
                                mc.setBlock(x-3-l,y+5-n,z-1+m,inside)
                        for o in range(5):
                                mc.setBlock(x-6-l,y+5-n,z-2+o,inside)
        mc.setBlock(x-10,y+5,z-2,light)
        mc.setBlock(x-10,y+5,z+2,light)
        for p in range(4):
                for q in range(5):
                        mc.setBlock(x-11-p,y+4,z-2+q,inside)
        for qqe in range(5):
                        mc.setBlock(x-14,y+4,z-2+qqe,up)
        for r in range(2):
                for s in range(4):
                        for t in range(3):
                                mc.setBlock(x-5-s,y+4-r,z-1+t,inside)
        mc.setBlock(x-6,y+4,z,bomb)
        mc.setBlock(x-7,y+4,z,bomb)
        mc.setBlock(x-8,y+4,z,bomb)
        for inin in range(15):
                mc.setBlock(x-inin,y,z+3,0)
                mc.setBlock(x-inin,y,z-3,0)
                mc.setBlock(x-inin,y-1,z+3,0)
                mc.setBlock(x-inin,y-1,z-3,0)

def set_body(x,y,z):
        for u in range(14):
                for w in range(5):
                        mc.setBlock(x-15-body*14-u,y-1,z-2+w,down)
                        mc.setBlock(x-15-body*14-u,y+4,z-2+w,inside)
                mc.setBlock(x-15-body*14-u,y,z-2,down)
                mc.setBlock(x-15-body*14-u,y,z+2,down)
                mc.setBlock(x-15-body*14-u,y+1,z-3,down)
                mc.setBlock(x-15-body*14-u,y+1,z+3,down)
                mc.setBlock(x-15-body*14-u,y+2,z-3,middle)
                mc.setBlock(x-15-body*14-u,y+2,z+3,middle)
                for v in range(2):
                        mc.setBlock(x-15-body*14-u,y+3+v,z-3,up)
                        mc.setBlock(x-15-body*14-u,y+3+v,z+3,up)
        for aa in range(5):
                mc.setBlock(x-28-body*14,y+4,z-2+aa,up)
        for bb in range(4):
                mc.setBlock(x-21-body*14-bb,y+4,z,inside)
        for ad in range(3):
                for ab in range(8):
                        for ac in range(5):
                                mc.setBlock(x-19-body*14-ab,y+5-ad,z-2+ac,inside)
        for ae in range(3):
                mc.setBlock(x-21-body*14-ae,y+4,z,bomb)
        mc.setBlock(x-21-body*14,y+4,z-1,bomb)
        mc.setBlock(x-21-body*14-2,y+4,z+1,bomb)
        mc.setBlock(x-21-body*14-1,y+3,z,bomb)
def set_control_tower(x,y,z):
        for cc in range(8):
                for dd in range(5):
                        mc.setBlock(x-19-cc,y+6,z-2+dd,inside)
                        mc.setBlock(x-19-cc,y+8,z-2+dd,inside)
                        mc.setBlock(x-19-cc,y+7,z-2+dd,glass)
                        mc.setBlock(x-18-cc,y+11,z-2+dd,inside)
        mc.setBlock(x-20,y+6,z,light)
        for ee in range(7):
                for ff in range(5):
                        mc.setBlock(x-18-ee,y+9,z-2+ff,up)
                        mc.setBlock(x-18-ee,y+10,z-2+ff,glass)
        mc.setBlock(x-19,y+9,z,light)
        mc.setBlock(x-20,y+10,z,inside)
        mc.setBlock(x-21,y+10,z,bomb)
        mc.setBlock(x-22,y+10,z,bomb)
        mc.setBlock(x-23,y+10,z,inside)
        for gg in range(6):
                for hh in range(3):
                       mc.setBlock(x-19-gg,y+12,z-1+hh,inside)
        for ii in range(3):
                mc.setBlock(x-20,y+13+ii,z,light)
                mc.setBlock(x-22,y+13+ii,z,light)
                mc.setBlock(x-24,y+13+ii,z,light)
def set_bottom(x,y,z,num):
        for jj in range(3):
                mc.setBlock(x-15-14*num,y-1,z-1+jj,down)
                mc.setBlock(x-15-14*num,y,z-1+jj,down)
        for kk in range(5):
                mc.setBlock(x-15-14*num,y+1,z-2+kk,down)
                mc.setBlock(x-15-14*num,y+2,z-2+kk,middle)
                mc.setBlock(x-15-14*num,y+3,z-2+kk,up)
                mc.setBlock(x-15-14*num,y+4,z-2+kk,up)
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "Arduino" in p[1]:
	    ser=serial.Serial(port=p[0])
	    break
time.sleep(2)
ser.write("6".encode())
time.sleep(2)
cap = cv2.VideoCapture(1)
a=54
b=10
c=490
d=458
leftup=(54,10)
rightlow=(490,458)
flag=True

while(flag):
    time.sleep(0.1)
    # Capture frame-by-frame
    ret, frame = cap.read(1)
    # Our operations on the frame come here
    img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord('a'):
        a-=10
        leftup=(a,b)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        b+=10
        leftup=(a,b)
    if cv2.waitKey(1) & 0xFF == ord('d'):
        a+=10
        leftup=(a,b)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        b-=10
        leftup=(a,b)
    if cv2.waitKey(1) & 0xFF == ord('j'):
        c-=10
        rightlow=(c,d)
    if cv2.waitKey(1) & 0xFF == ord('k'):
        d+=10
        rightlow=(c,d)
    if cv2.waitKey(1) & 0xFF == ord('l'):
        c+=10
        rightlow=(c,d)
    if cv2.waitKey(1) & 0xFF == ord('i'):
        d-=10
        rightlow=(c,d)    
    cv2.rectangle(img,leftup,rightlow,(255,255,255),1)
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
print (a,b,c,d)
area=[]
#cv2.imshow('',img[a:(a+(1*(c-a)//8)), b:(b+(1*(d-b)//8))])
post=[]
for i in range(1,9):
    for j in range(1,9):
        area.append(img[a+((i-1)*(d-a)//8):a+(i*(d-a)//8), b+((j-1)*(c-b)//8):b+(j*(c-b)//8)])




ships=[]
ships2=[]
for i in range(0,64):
    ships.append(0)
    ships2.append(0)









import collections
 
#定义字典存放颜色分量上下限
#例如：{颜色: [min分量, max分量]}
#{'red': [array([160,  43,  46]), array([179, 255, 255])]}
 
def getColorList():
    dict = collections.defaultdict(list)
 
    # 黑色
    
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 46])
    color_list = []
    color_list.append(lower_black)
    color_list.append(upper_black)
    dict['black'] = color_list
    
    # #灰色
    '''
    lower_gray = np.array([0, 0, 46])
    upper_gray = np.array([180, 43, 220])
    color_list = []
    color_list.append(lower_gray)
    color_list.append(upper_gray)qqqqqqqqq
    dict['gray']=color_list
    '''
    # 白色
    
    lower_white = np.array([0, 0, 221])
    upper_white = np.array([180, 30, 255])
    color_list = []
    color_list.append(lower_white)
    color_list.append(upper_white)
    dict['white'] = color_list
    
 
    #红色
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red']=color_list
 
    # 红色2
    '''
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red2'] = color_list
    
    #橙色
    
    lower_orange = np.array([11, 43, 46])
    upper_orange = np.array([25, 255, 255])
    color_list = []
    color_list.append(lower_orange)
    color_list.append(upper_orange)
    dict['orange'] = color_list
    
    
    #黄色
    
    lower_yellow = np.array([26, 43, 46])
    upper_yellow = np.array([34, 255, 255])
    color_list = []
    color_list.append(lower_yellow)
    color_list.append(upper_yellow)
    dict['yellow'] = color_list
    '''
    #绿色
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    color_list = []
    color_list.append(lower_green)
    color_list.append(upper_green)
    dict['green'] = color_list
    
    #青色
    '''
    lower_cyan = np.array([78, 43, 46])
    upper_cyan = np.array([99, 255, 255])
    color_list = []
    color_list.append(lower_cyan)
    color_list.append(upper_cyan)
    dict['cyan'] = color_list
    '''
    #蓝色
    '''
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    color_list = []
    color_list.append(lower_blue)
    color_list.append(upper_blue)
    dict['blue'] = color_list
    '''
    
    # 紫色
    
    lower_purple = np.array([125, 43, 46])
    upper_purple = np.array([155, 255, 255])
    color_list = []
    color_list.append(lower_purple)
    color_list.append(upper_purple)
    dict['purple'] = color_list
    
    return dict

def get_color(frame):
    print('go in get_color')
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    maxsum = -100
    color = None
    color_dict = getColorList()
    for d in color_dict:
        mask = cv2.inRange(hsv,color_dict[d][0],color_dict[d][1])
        cv2.imwrite(d+'.jpg',mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary,None,iterations=2)
        img, cnts, hiera = cv2.findContours(binary.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        for c in cnts:
            sum+=cv2.contourArea(c)
        if sum > maxsum :
            maxsum = sum
            color = d
 
    return color
for i in range(len(ships)):
    ships[i]=get_color(area[i])
x = 1
y = 120
z = 1

mc = minecraft.Minecraft.create()
for i in range(0,8):
    for j in range(0,8):
        if ships[i*8+j]=="red":
            set_head(x+i*15,y,z+j*15)
            #attack(x+i*15,y,z+j*15)
        elif ships[i*8+j]=="green":
            set_body(x+i*15-15,y,z+j*15)
            set_control_tower(x+i*15-30,y,z+j*15)
            set_bottom(x+i*15-15,y,z+j*15,2)
            #attack(x+i*15,y,z+j*15)

#mc

for m in range(3):

    while(flag):
        print(a)
        time.sleep(0.1)
        # Capture frame-by-frame
        ret, frame = cap.read(1)
        # Our operations on the frame come here
        img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
        # Display the resulting frame
        '''
        if cv2.waitKey(1) & 0xFF == ord('a'):
            a-=10
            leftup=(a,b)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            b+=10
            leftup=(a,b)
        if cv2.waitKey(1) & 0xFF == ord('d'):
            a+=10
            leftup=(a,b)
        if cv2.waitKey(1) & 0xFF == ord('w'):
            b-=10
            leftup=(a,b)
        if cv2.waitKey(1) & 0xFF == ord('j'):
            c-=10
            rightlow=(c,d)
        if cv2.waitKey(1) & 0xFF == ord('k'):
            d+=10
            rightlow=(c,d)
        if cv2.waitKey(1) & 0xFF == ord('l'):
            c+=10
            rightlow=(c,d)
        if cv2.waitKey(1) & 0xFF == ord('i'):
            d-=10
            rightlow=(c,d)
        '''
        cv2.rectangle(img,leftup,rightlow,(255,255,255),1)
        cv2.imshow('frame',img)
        '''if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        '''
        resp=ser.readline()
        rs=str(resp)
        if 'ready'in rs:
            flag=False
        else:
            pass
    flag=True
    cv2.destroyAllWindows()
    area=[]
    for i in range(1,9):
        for j in range(1,9):
            area.append(img[a+((i-1)*(d-a)//8):a+(i*(d-a)//8), b+((j-1)*(c-b)//8):b+(j*(c-b)//8)])

    for i in range(len(ships2)):
        ships2[i]=get_color(area[i])
        print (ships2[i])
    score=0
    
    flag2=True
    for i in range(0,8):
        for j in range(0,8):
            if ships2[i*8+j]=="green":
                if ships[i*8+j]!= "green"and ships[i*8+j]!="red":
                    ser.write("5".encode())
                    time.sleep(2)
                elif ships[i*8+j]=="green":
                    attack(x+i*15,y,z+j*15)
                    ser.write("10".encode())
                    score+=1
                    time.sleep(2)
                elif ships[i*8+j]=="red":
                    attack(x+i*15,y,z+j*15)
                    ser.write("10".encode())
                    score+=1
                    time.sleep(2)
                ships[i*8+j]=="white"
                flag2=False
                break
        if flag2==False:
            break
        
        '''
        elif ships2[i]=="red":
            if ships[i]!= "green"and ships[i]!="red" :
                if i==0 or i ==63 :
                    ser.write("5".encode())
                    time.sleep(2)
                elif i>=1 and ships[i-1]=="white" and i<63 and ships[i+1]=="white":
                    ser.write("5".encode())
                    time.sleep(2)
                    
                else:
                    ser.write("10".encode())
                    attack(x+i*15-15,y,z+j*15-15)
                    attack(x+i*15+15,y,z+j*15+15)
                    if ships[i-1] == "red" and ships[i-1]!= "green":
                        score+=1
                    if ships[i+1] == "red" and ships[i+1]!= "green":
                        score +=1
            else: #ships[i]=="green" or ships[i]=="red":
                attack(x+i*15,y,z+j*15)
                score+=1
                if i==0 or i ==63 :
                    pass
                elif i>=1 and ships[i-1]=="white" and i<63 and ships[i+1]=="white":
                    pass
                else:
                    attack(x+i*15-15,y,z+j*15-15)
                    attack(x+i*15+15,y,z+j*15+15)
                    if ships[i-1] != "white":
                        score+=1
                    if ships[i+1] !="white":
                        score +=1
                ser.write("10".encode())
                
                time.sleep(2)
            
            ships[i]=="white"
            break
        '''
    ser.write("9".encode())
    time.sleep(2)
time.sleep(2)
ser.write("1".encode())
time.sleep(5)
