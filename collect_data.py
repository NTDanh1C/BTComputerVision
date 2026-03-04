import cv2
import os

user_name = input("Enter user name: ")
save_path = f"dataset/{user_name}"

if not os.path.exists(save_path):
    os.makedirs(save_path)
#model nhận diện khuôn mặt của opencv
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)
count = 0 #đếm số sample đã lấy

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = gray[y:y+h, x:x+w] #lấy ảnh có chứa khuôn mặt 
        count += 1
        cv2.imwrite(f"{save_path}/{count}.jpg", face_img)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Collecting Faces", frame)

    if cv2.waitKey(1) & 0xFF == 27 or count >= 100:
        break

cap.release()
cv2.destroyAllWindows()