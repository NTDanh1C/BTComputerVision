import cv2 as cv
import numpy as np

cap = cv.VideoCapture("C:\\Users\\ADMIN\\Downloads\\bang_chuyen.mp4")
count = 0 # đếm số vật thể hình tròn
vat_the = [] #lưu lại vật thể
line_x = 100 #tọa độ line màu đỏ

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #chuyển sang ảnh xám
    gray = cv.medianBlur(gray, 5) #làm sạch nhiễu
    
    circles = cv.HoughCircles(
        gray,
        cv.HOUGH_GRADIENT,
        dp=1,
        minDist=10,
        param1=50,
        param2=50,
        minRadius=10,
        maxRadius=100
    )
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circles in circles[0, :]:
            x, y, r = circles[0], circles[1], circles[2]
            cv.circle(frame, (x, y), r, (0, 0, 255), 2)

    cv.imshow("frame", frame)
    if cv.waitKey(100) == ord('q'):
        break
cv.destroyAllWindows()