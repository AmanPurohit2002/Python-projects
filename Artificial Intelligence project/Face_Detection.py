import cv2

webcam=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


while True :
    _,image=webcam.read()

    rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    faces=face_cascade.detectMultiScale(rgb_image,1.5,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),4)


    cv2.imshow("Camera made by Aman Purohit", image)

    key=cv2.waitKey(10)

    if key ==27:
        break

webcam.release()
cv2.destroyAllWindows()