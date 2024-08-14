import cv2
import matplotlib.pyplot as plt
#load the pretrained classifier of hair cascade classifier
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#upload an image for test
image=cv2.imread('img.jpg')
grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(grey_image,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
print(f"no of face detected:{len(faces)}")
for(x,y,w,h)in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
img_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis('off')
plt.show()
