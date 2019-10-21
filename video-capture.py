import cv2 as cv2

captura = cv2.VideoCapture(0)

while(1):
    ret, frame = captura.read()

    b,g,r = cv2.split(frame)

    t, u = cv2.threshold(r,100,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("Video", u)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
 
captura.release()
cv2.destroyAllWindows()