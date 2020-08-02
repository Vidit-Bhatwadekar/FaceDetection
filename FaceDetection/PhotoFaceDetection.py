
import cv2

inp_model = input('Detection: ')
inp_img = input('jpg name (including extention): ')

if inp_model == 'Eyes':
    model = 'haarcascade_eye.xml'
elif inp_model == 'Face':
    model = 'haarcascade_frontalface_default.xml'
elif inp_model == 'Left Eye':
    model = 'haarcascade_lefteye_2splits.xml'
elif  inp_model == 'Right Eye':
    model == 'haarcascade_righteye_2splits.xml'
else:
    raise Exception('Invalid input')

face_cascade = cv2.CascadeClassifier('Models/' + model)
img = cv2.imread(inp_img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()

cv2.release()
