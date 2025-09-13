import sys
import time
import signal
import common.mecanum as mecanum

chassis = mecanum.MecanumChassis()

def stop_robot(signum, frame):
    print("Stopping the robot...")
    chassis.set_velocity(0, 0, 0)
    sys.exit(0)

signal.signal(signal.SIGINT, stop_robot)

try:
    # กำหนดค่าต่างๆ
    move_speed = 50 # ความเร็วในการเดินหน้า
    move_duration = 2.0  # วินาที
    turn_rate = 0.5 # อัตราการหมุน (ลองปรับค่านี้)
    turn_duration = 1.0 # เวลาที่ใช้หมุน 90 องศา (ต้องปรับจูน)

    print("Executing square mission. Press Ctrl+C to stop.")

    for i in range(4):
        # 1. เดินหน้า
        print(f"Moving forward: side {i+1}")
        # แก้ไขทิศทางเดินหน้าให้เป็น 90 องศา
        chassis.set_velocity(move_speed, 90, 0) 
        time.sleep(move_duration)

        # 2. หยุดนิ่งๆ ก่อนหมุน
        chassis.set_velocity(0, 0, 0)
        time.sleep(0.5)

        # 3. หมุนตัวอยู่กับที่ (ตามเข็ม)
        print(f"Turning right: corner {i+1}")
        chassis.set_velocity(0, 0, turn_rate) # speed=0, yaw=-0.5
        time.sleep(turn_duration)

        # 4. หยุดสนิทหลังหมุนเสร็จ
        chassis.set_velocity(0, 0, 0)
        time.sleep(0.5)

    print("Mission Complete!")

except Exception as e:
    print(e)
    chassis.set_velocity(0, 0, 0)