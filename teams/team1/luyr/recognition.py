from aip import AipImageClassify
import serial.tools.list_ports
import numpy as np
#import picamera
import serial
import time
import csv
import cv2


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



def Call_API(path, client):
    """ 调用植物识别 """
    image = get_file_content('pic.jpg')
    result = client.plantDetect(image);
    
   
    try:
        result = result['result']
        if result[0]['score'] > 0.5:
            species = result[0]['name']
            print(species)
        else:
            species = 'fail'
            print("recognition failed")
            return species
    except KeyError:
        species = 'fail'
        print("recognition error")
        return species
            
    

def capture(client, cap):

    ret, frame = cap.read()

    
    cv2.imwrite('flower.jpg',frame)
    flower = cv2.imread('flower.jpg', cv2.IMREAD_COLOR)
    
    #cv2.imshow('flower',flower)
    #camera.capture('flower.jpg',resize=(320,240))
    #camera.close()
    result = Call_API('flower.jpg', client)

    while (result == 'fail') :
        Call_API('flower.jpg', client) 

    return result
    cv2.waitKey(1)


    return 0




def Search_Data(a):
    with open('database.csv', 'r') as f:
        reader = csv.reader(f) 
        for row in reader: 
            if row[0] == a:
            	return row[1]


def main():
    '''initialize API'''
    APP_ID = 'xxxxxxxx'
    API_KEY = 'xxxxxxxx'
    SECRET_KEY = 'xxxxxxxx'
    client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

    '''open camera'''
    cap = cv2.VideoCapture(0)
    #camera = picamera.PiCamera()

    '''initialize serial'''
    ser = serial.Serial('/dev/ttyACM1', 9600,timeout=1)
    print(ser.name)

    while (True):


        species = capture(client, cap)
        #capture(client, camera)

        with open('/run/user/1000/gvfs/smb-share:server=192.168.0.100,share=share_pi/switch.txt', 'r') as f:
            mc = f.read()

        receive = ser.readline()
        receives = receive.split()
        print(receive)
        if len(receives) == 1 or len(receives) == 0:
            pass
        else:
            ard_1 = (int(receives[0])-50)//70
            ard_2 = float(receives[1])
            with open('/run/user/1000/gvfs/smb-share:server=192.168.0.100,share=share_pi/upload.txt', 'w') as f:
                f.write( str(ard_1) + ',' +str(ard_2)+','+ species)

        ser.write(mc.encode())
        print(mc)
        time.sleep(1)
        
        ser.write('400'.encode())

            


    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()    
    


    
