import sys
import time
import signal
import common.mecanum as mecanum

chassis = mecanum.MecanumChassis()

# ฟังก์ชันสำหรับหยุดหุ่นยนต์เมื่อกด Ctrl+C
def stop_robot(signum, frame):
    print("Stopping the robot...")
    chassis.set_velocity(0, 0, 0)
    sys.exit(0)

signal.signal(signal.SIGINT, stop_robot)

try:
    print("Testing basic 4-direction movements. Press Ctrl+C to stop.")

    # 1. เดินหน้า (ทิศทาง 90 องศา)
    print("Moving Forward (Direction 90)")
    chassis.set_velocity(50, 90, 0)
    time.sleep(2)

    # 2. ถอยหลัง (ทิศทาง 270 องศา)
    print("Moving Backward (Direction 270)")
    chassis.set_velocity(50, 270, 0)
    time.sleep(2)

    # 3. สไลด์ซ้าย (ทิศทาง 180 องศา)
    print("Strafing Left (Direction 180)")
    chassis.set_velocity(50, 180, 0)
    time.sleep(2)

    # 4. สไลด์ขวา (ทิศทาง 0 องศา)
    print("Strafing Right (Direction 0)")
    chassis.set_velocity(50, 0, 0)
    time.sleep(2)

    # หยุดการทำงาน
    chassis.set_velocity(0, 0, 0)
    print("Test Complete!")

except Exception as e:
    print(e)
    chassis.set_velocity(0, 0, 0)
