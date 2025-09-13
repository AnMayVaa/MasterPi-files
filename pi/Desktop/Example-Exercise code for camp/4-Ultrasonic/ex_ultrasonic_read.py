import time
import sys
import signal
import common.sonar as Sonar

# --- ส่วนของการ Setup ---
sonar = Sonar.Sonar()
# -----------------------

def stop_sensor(signum, frame):
    print("\nStopping sensor reading.")
    # ปิดไฟ LED ก่อนจบโปรแกรม
    sonar.setPixelColor(0, (0, 0, 0))
    sonar.setPixelColor(1, (0, 0, 0))
    sys.exit(0)

signal.signal(signal.SIGINT, stop_sensor)

try:
    print("Reading distance... Press Ctrl+C to stop.")
    while True:
        # 1. อ่านค่าจากเซ็นเซอร์ (ได้เป็น mm)
        distance_mm = sonar.getDistance()

        # 2. แปลงเป็น cm
        distance_cm = distance_mm / 10.0

        # 3. พิมพ์ผลลัพธ์
        print(f"Distance: {distance_cm:.1f} cm")

        time.sleep(0.2)

except KeyboardInterrupt:
    pass