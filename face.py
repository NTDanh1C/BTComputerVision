import cv2 as cv
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

cap = cv.VideoCapture(0)

points = [1, 33, 61, 199, 263]   # tự chỉnh số lượng

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    res = face_mesh.process(rgb)

    if res.multi_face_landmarks:
        for face_landmarks in res.multi_face_landmarks:
            h, w, _ = frame.shape

            for p in points:
                lm = face_landmarks.landmark[p]
                x = int(lm.x * w)
                y = int(lm.y * h)

                cv.circle(frame, (x, y), 4, (0,255,0), -1)

    cv.imshow("Face", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()