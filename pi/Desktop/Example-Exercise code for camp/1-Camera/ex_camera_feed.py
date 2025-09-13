import cv2
import time

# เชื่อมต่อกับกล้อง
cap = cv2.VideoCapture('http://127.0.0.1:8080?action=stream')

# ตรวจสอบว่าเชื่อมต่อสำเร็จหรือไม่
if not cap.isOpened():
    print("Error: Couldn't open camera stream.")
    exit()

print("Camera feed is active. Press 'q' to quit.")

while True:
    # อ่านภาพจากกล้องทีละเฟรม
    ret, frame = cap.read()

    # ถ้าอ่านภาพสำเร็จ
    if ret:
        # แสดงภาพในหน้าต่างชื่อ "Robot's Eye"
        cv2.imshow("Robot's Eye", frame)

    # รอรับการกดปุ่ม 'q' เพื่อออกจากโปรแกรม
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# คืนทรัพยากรและปิดหน้าต่างทั้งหมด
cap.release()
cv2.destroyAllWindows()
