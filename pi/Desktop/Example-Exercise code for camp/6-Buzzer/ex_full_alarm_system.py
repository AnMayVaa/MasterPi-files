import time
import sys
import signal
import common.sonar as Sonar
import common.mecanum as mecanum
from common.ros_robot_controller_sdk import Board

# --- ส่วนของการ Setup ---
sonar = Sonar.Sonar()
chassis = mecanum.MecanumChassis()
board = Board()
# -----------------------

is_running = True
def stop_robot(signum, frame):
    global is_running
    is_running = False
    print("\nStopping the robot...")
    chassis.set_velocity(0, 0, 0)
    sonar.setPixelColor(0, (0, 0, 0))
    sonar.setPixelColor(1, (0, 0, 0))
    board.set_buzzer(0, 0, 0, 1)
    sys.exit(0)

signal.signal(signal.SIGINT, stop_robot)

try:
    # กำหนดค่าต่างๆ
    ALERT_DISTANCE_CM = 25.0
    forward_speed = 30
    is_beeping = False

    print("Automatic Braking System Activated. Press Ctrl+C to stop.")

    while is_running:
        distance_cm = sonar.getDistance() / 10.0
        print(f"Distance: {distance_cm:.1f} cm")

        if distance_cm < ALERT_DISTANCE_CM:
            # หยุดรถ
            chassis.set_velocity(0, 0, 0)
            # ไฟสีแดง
            sonar.setPixelColor(0, (255, 0, 0))
            sonar.setPixelColor(1, (255, 0, 0))
            # เปิดเสียงเตือน (ถ้ายังไม่เปิด)
            if not is_beeping:
                board.set_buzzer(2500, 0.3, 0.3, 0) # เสียงดัง 0.3 วิ, เงียบ 0.3 วิ, ซ้ำตลอด
                is_beeping = True
        else:
            # เดินหน้า (ทิศทาง 90 องศา)
            chassis.set_velocity(forward_speed, 90, 0)
            # ไฟสีเขียว
            sonar.setPixelColor(0, (0, 255, 0))
            sonar.setPixelColor(1, (0, 255, 0))
            # ปิดเสียงเตือน (ถ้าเปิดอยู่)
            if is_beeping:
                board.set_buzzer(0, 0, 0, 1)
                is_beeping = False

        time.sleep(0.1)

except KeyboardInterrupt:
    pass
