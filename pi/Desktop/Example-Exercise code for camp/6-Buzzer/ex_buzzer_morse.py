import time
import sys
import signal
from common.ros_robot_controller_sdk import Board

# --- ส่วนของการ Setup ---
board = Board()
# -----------------------

def stop_buzzer(signum, frame):
    print("\nStopping buzzer.")
    board.set_buzzer(0, 0, 0, 1) # ปิดเสียง
    sys.exit(0)

signal.signal(signal.SIGINT, stop_buzzer)

try:
    print("Playing Morse Code: S.O.S. Press Ctrl+C to stop.")

    # --- S (... ) ---
    print("S")
    # เสียงดัง 0.2 วิ, เงียบ 0.2 วิ, ทำ 3 ครั้ง -> ใช้เวลาทั้งหมด (0.2 + 0.2) * 3 = 1.2 วินาที
    board.set_buzzer(2000, 0.2, 0.2, 3) 
    time.sleep(1.3) # รอให้เสียงเล่นจบ + เว้นวรรคเล็กน้อย

    # --- O (---) ---
    print("O")
    # เสียงดัง 0.6 วิ, เงียบ 0.2 วิ, ทำ 3 ครั้ง -> ใช้เวลาทั้งหมด (0.6 + 0.2) * 3 = 2.4 วินาที
    board.set_buzzer(2000, 0.6, 0.2, 3) 
    time.sleep(2.5) # รอให้เสียงเล่นจบ + เว้นวรรคเล็กน้อย

    # --- S (... ) ---
    print("S")
    # ใช้เวลาทั้งหมด 1.2 วินาที
    board.set_buzzer(2000, 0.2, 0.2, 3)
    time.sleep(1.3)

    print("Morse code sent.")

except KeyboardInterrupt:
    pass