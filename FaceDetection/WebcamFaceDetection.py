
import cv2

inp = input('Detection: ')

if inp == 'Eyes':
    model = 'haarcascade_eye.xml'
elif inp == 'Face':
    model = 'haarcascade_frontalface_default.xml'
elif inp == 'Left Eye':
    model = 'haarcascade_lefteye_2splits.xml'
elif  inp == 'Right Eye':
    model == 'haarcascade_righteye_2splits.xml'
else:
    raise Exception('Invalid input')

face_cascade = cv2.CascadeClassifier('Model/' + model)
capture = cv2.VideoCapture(0)

while True:
    _, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', img)
    key = cv2.waitKey(30) & 0xff
    if key==27:
        break
capture.release()
