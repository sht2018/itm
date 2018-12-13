import cv2

while True:
    cap = cv2.VideoCapture("bus_station_6094_960x540.mp4")

    while(True):
          # Capture frame-by-frame 15 ret, frame = cap.read() 16 17 # Our operations on the frame come here 1
          ret, frame = cap.read()
          with open('test1.txt', 'r') as f1:
              global a
              a = f1.readline()
              print("a = "+str(a))

          cv2.putText(frame,'there are '+a+' person',(0,40),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,255,255),2)
          gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)




          # Display the resulting frame 21
          cv2.imshow('frame',gray)
          if cv2.waitKey(1) & 0xFF == ord('q'):
               break  # When everything done, release the capture 26
cap.release()
cv2.destroyAllWindows()
