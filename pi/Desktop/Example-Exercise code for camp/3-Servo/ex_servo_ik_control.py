import time
from kinematics.arm_move_ik import ArmIK
from common.ros_robot_controller_sdk import Board

AK = ArmIK()
board = Board()
AK.board = board

try:
    print("Testing Inverse Kinematics Control. Press Ctrl+C to exit.")

    # 1. ไปยังท่าเริ่มต้น (สำคัญมาก!)
    print("Moving to Initial Position (x=0, y=6, z=18)...")
    AK.setPitchRangeMoving((0, 6, 18), 0, -90, 90, 1500)
    time.sleep(2)

    # 2. ขยับไปข้างหน้า (แกน Y)
    print("Moving Forward (y=13)...")
    AK.setPitchRangeMoving((0, 13, 18), 0, -90, 90, 1000)
    time.sleep(1.5)

    # 3. ขยับไปทางขวา (แกน X)
    print("Moving Right (x=5)...")
    AK.setPitchRangeMoving((5, 13, 18), 0, -90, 90, 1000)
    time.sleep(1.5)

    # 4. ขยับลง (แกน Z)
    print("Moving Down (z=12)...")
    AK.setPitchRangeMoving((5, 13, 12), 0, -90, 90, 1000)
    time.sleep(1.5)

    # 5. ขยับไปทางซ้าย (แกน X)
    print("Moving Left (x=-5)...")
    AK.setPitchRangeMoving((-5, 13, 12), 0, -90, 90, 1000)
    time.sleep(1.5)

    # กลับสู่ท่าเริ่มต้น
    print("Returning to Initial Position...")
    AK.setPitchRangeMoving((0, 6, 18), 0, -90, 90, 1000)
    print("IK Test complete.")

except KeyboardInterrupt:
    print("\nProgram stopped by user.")
    AK.setPitchRangeMoving((0, 6, 18), 0, -90, 90, 1000) # กลับท่าเริ่มต้นเมื่อหยุด