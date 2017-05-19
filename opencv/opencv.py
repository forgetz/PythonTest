import cv2

img = cv2.imread("brothers-457237_1280.jpg")
hc = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
faces = hc.detectMultiScale(img)

for face in faces:
	cv2.rectangle(img, (face[0], face[1]), (face[0] + face[2], face[0] + face[3]), (255, 0, 0), 2)

cv2.imwrite("Face4.jpg", img)