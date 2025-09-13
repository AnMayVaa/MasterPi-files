import cv2
import numpy as np

# ฟังก์ชันว่างๆ ที่จำเป็นสำหรับ createTrackbar
def nothing(x):
    pass

# สร้างหน้าต่างสำหรับ Trackbars
cv2.namedWindow("Trackbars")

# สร้าง Trackbars สำหรับค่า Lower-bound และ Upper-bound ของ HSV
# H: 0-179, S: 0-255, V: 0-255
cv2.createTrackbar("H_min", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("S_min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("V_min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("H_max", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("S_max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("V_max", "Trackbars", 255, 255, nothing)

# เชื่อมต่อกับกล้อง
cap = cv2.VideoCapture('http://127.0.0.1:8080?action=stream')

if not cap.isOpened():
    print("Error: Couldn't open camera stream.")
    exit()

print("Color Calibrator is active. Adjust trackbars to find your color range.")
print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # อ่านค่าจาก Trackbars
    h_min = cv2.getTrackbarPos("H_min", "Trackbars")
    s_min = cv2.getTrackbarPos("S_min", "Trackbars")
    v_min = cv2.getTrackbarPos("V_min", "Trackbars")
    h_max = cv2.getTrackbarPos("H_max", "Trackbars")
    s_max = cv2.getTrackbarPos("S_max", "Trackbars")
    v_max = cv2.getTrackbarPos("V_max", "Trackbars")

    # สร้าง lower และ upper bound จากค่าที่อ่านได้
    lower_bound = np.array([h_min, s_min, v_min])
    upper_bound = np.array([h_max, s_max, v_max])

    # สร้าง Mask
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

    # แสดงผล
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()