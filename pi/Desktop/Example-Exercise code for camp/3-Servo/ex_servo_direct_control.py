import time
from common.ros_robot_controller_sdk import Board

# --- ส่วนของการ Setup ---
board = Board()
# -----------------------

try:
    print("Testing Direct Servo Control. Press Ctrl+C to exit.")

    # 1. ทดสอบที่คีบ (Servo 1: Gripper)
    print("Testing Servo 1: Gripper")
    board.pwm_servo_set_position(0.5, [[1, 1300]]) # เปิด
    time.sleep(1)
    board.pwm_servo_set_position(0.5, [[1, 1800]]) # ปิด
    time.sleep(1)

    # 2. ทดสอบข้อต่อคอ (Servo 3 & 4)
    print("Testing Servo 3 & 4: Neck Joints")
    board.pwm_servo_set_position(1, [[3, 700], [4, 2200]])
    time.sleep(1.5)
    board.pwm_servo_set_position(1, [[3, 500], [4, 2400]])
    time.sleep(1.5)

    # 3. ทดสอบการหมุนคอ (Servo 5: Neck Rotation)
    print("Testing Servo 5: Neck Rotation")
    board.pwm_servo_set_position(1, [[5, 580]])
    time.sleep(1.5)
    board.pwm_servo_set_position(1, [[5, 1500]])
    time.sleep(1.5)

    # 4. ทดสอบการก้ม-เงย (Servo 6: Head Pitch)
    print("Testing Servo 6: Head Pitch")
    board.pwm_servo_set_position(1, [[6, 1300]])
    time.sleep(1.5)
    board.pwm_servo_set_position(1, [[6, 1700]])
    time.sleep(1.5)

    print("Test Complete.")

except KeyboardInterrupt:
    print("\nProgram stopped by user.")
