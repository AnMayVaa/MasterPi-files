import time
import sys
import signal
from common.ros_robot_controller_sdk import Board

# --- ส่วนของการ Setup ---
board = Board()
# -----------------------

def stop_leds(signum, frame):
    print("\nTurning off LEDs.")
    board.set_rgb([[1, 0, 0, 0], [2, 0, 0, 0]]) # ปิดไฟ
    sys.exit(0)

signal.signal(signal.SIGINT, stop_leds)

try:
    print("Traffic Light Simulation. Press Ctrl+C to stop.")
    while True:
        # 1. ไฟเขียว (Go)
        print("GREEN")
        board.set_rgb([[1, 0, 255, 0], [2, 0, 255, 0]])
        time.sleep(3)

        # 2. ไฟเหลือง (Warning)
        print("YELLOW")
        board.set_rgb([[1, 255, 255, 0], [2, 255, 255, 0]])
        time.sleep(1)

        # 3. ไฟแดง (Stop)
        print("RED")
        board.set_rgb([[1, 255, 0, 0], [2, 255, 0, 0]])
        time.sleep(3)

except KeyboardInterrupt:
    pass
