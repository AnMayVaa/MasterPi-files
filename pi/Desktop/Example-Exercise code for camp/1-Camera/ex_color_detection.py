import cv2
import numpy as np

# เชื่อมต่อกับกล้อง
cap = cv2.VideoCapture('http://127.0.0.1:8080?action=stream')

if not cap.isOpened():
    print("Error: Couldn't open camera stream.")
    exit()

print("Color Detection is active. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. แปลงสีเป็น HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 2. กำหนดช่วงของสีแดงในระบบ HSV
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # 3. สร้าง Mask
    mask1 = cv2.inRange(hsv_frame, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_frame, lower_red2, upper_red2)
    mask = mask1 + mask2

    # 4. หา Contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 5. หา Contour ที่ใหญ่ที่สุดแล้ววาดกรอบ
    if len(contours) > 0:
        # หา contour ที่มีพื้นที่ใหญ่ที่สุด
        max_contour = max(contours, key=cv2.contourArea)

        # วาดกรอบสี่เหลี่ยมรอบ contour นั้น
        x, y, w, h = cv2.boundingRect(max_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Mask", mask) # แสดง Mask เพื่อช่วยในการดีบัก

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()