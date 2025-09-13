import time
import sys
import signal
import common.sonar as Sonar

sonar = Sonar.Sonar()

def stop_sensor(signum, frame):
    print("\nStopping alert system.")
    sonar.setPixelColor(0, (0, 0, 0))
    sonar.setPixelColor(1, (0, 0, 0))
    sys.exit(0)

signal.signal(signal.SIGINT, stop_sensor)

# กำหนดค่าต่างๆ
ALERT_DISTANCE_CM = 20.0
COLOR_SAFE = (0, 255, 0)   # สีเขียว
COLOR_ALERT = (255, 0, 0) # สีแดง

try:
    print(f"Smart Alert System Activated. Alert distance: < {ALERT_DISTANCE_CM} cm")
    print("Press Ctrl+C to stop.")

    while True:
        distance_cm = sonar.getDistance() / 10.0
        print(f"Distance: {distance_cm:.1f} cm")

        # เขียนเงื่อนไขเพื่อตัดสินใจเปลี่ยนสีไฟ
        if distance_cm < ALERT_DISTANCE_CM:
            # อยู่ในระยะอันตราย -> ไฟสีแดง
            sonar.setPixelColor(0, COLOR_ALERT)
            sonar.setPixelColor(1, COLOR_ALERT)
        else:
            # อยู่ในระยะปลอดภัย -> ไฟสีเขียว
            sonar.setPixelColor(0, COLOR_SAFE)
            sonar.setPixelColor(1, COLOR_SAFE)

        time.sleep(0.1)

except KeyboardInterrupt:
    pass
