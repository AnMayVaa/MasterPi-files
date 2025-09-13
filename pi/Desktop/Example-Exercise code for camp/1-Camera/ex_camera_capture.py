import cv2
import time

# เชื่อมต่อกับกล้อง
cap = cv2.VideoCapture('http://127.0.0.1:8080?action=stream')

if not cap.isOpened():
    print("Error: Couldn't open camera stream.")
    exit()

print("Camera feed is active.")
print("Press 's' to save a picture.")
print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow("Robot's Eye", frame)

    # --- ส่วนที่แก้ไข ---
    # รอรับการกดปุ่มจากคีย์บอร์ด
    key = cv2.waitKey(1) & 0xFF

    # ถ้ากด 'q' ให้ออกจาก Loop
    if key == ord('q'):
        break
    # ถ้ากด 's' ให้บันทึกภาพ
    elif key == ord('s'):
        # สร้างชื่อไฟล์จากเวลาปัจจุบันเพื่อไม่ให้ซ้ำกัน
        filename = f"capture_{int(time.time())}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")
    # --- จบส่วนที่แก้ไข ---

cap.release()
cv2.destroyAllWindows()
