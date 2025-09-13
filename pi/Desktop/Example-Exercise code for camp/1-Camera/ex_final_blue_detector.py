import cv2
import numpy as np

# เชื่อมต่อกับกล้อง
stream_url = 'http://127.0.0.1:8080?action=stream'
cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Error: Couldn't open camera stream.")
    exit()

print("Blue Color Detector is active. Press 'q' to quit.")

# --- ส่วนที่สำคัญที่สุด ---
# นำค่า H, S, V ทั้ง 6 ค่าที่จดไว้จาก Calibrator มาใส่ตรงนี้!
# นี่คือค่าตัวอย่างสำหรับ "สีน้ำเงิน"
H_MIN = 101
S_MIN = 135
V_MIN = 80
H_MAX = 125
S_MAX = 255
V_MAX = 255

# สร้าง lower และ upper bound จากค่าที่เราหามาได้
lower_blue = np.array([H_MIN, S_MIN, V_MIN])
upper_blue = np.array([H_MAX, S_MAX, V_MAX])
# --------------------------

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # สร้าง Mask โดยใช้ค่าสีน้ำเงินที่เราตั้งไว้
    mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 500:
            x, y, w, h = cv2.boundingRect(max_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) # วาดกรอบสีน้ำเงิน

    cv2.imshow("Blue Detector", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()