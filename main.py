import cv2
import winsound

capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)


while True:
    isTrue, frame = capture.read()
    isTrue, frame2 = capture.read()
    diff = cv2.absdiff(frame,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,20,255)
    ret,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame, contours , -1, (0,255,0), 2)
    for c in contours:
        area = cv2.contourArea(c)
        if area < 5000:
            continue
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        winsound.PlaySound("C:\\Users\\user\\Downloads\\alert_siren.wav",winsound.SND_ASYNC)
    cv2.imshow("video",frame)
    if cv2.waitKey(50) & 0xff==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()