import time
import sys
import signal
import common.sonar as Sonar

# --- ส่วนของการ Setup ---
sonar = Sonar.Sonar()
# -----------------------

def stop_leds(signum, frame):
    print("\nTurning off siren LEDs.")
    sonar.setPixelColor(0, (0, 0, 0))
    sonar.setPixelColor(1, (0, 0, 0))
    sys.exit(0)

signal.signal(signal.SIGINT, stop_leds)

# กำหนดค่าสี
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_OFF = (0, 0, 0)

try:
    print("Siren Light Simulation. Press Ctrl+C to stop.")
    while True:
        # สเต็ป 1: ซ้ายแดง - ขวาน้ำเงิน
        sonar.setPixelColor(0, COLOR_RED)
        sonar.setPixelColor(1, COLOR_BLUE)
        time.sleep(0.2)

        # สเต็ป 2: ซ้ายน้ำเงิน - ขวาแดง
        sonar.setPixelColor(0, COLOR_BLUE)
        sonar.setPixelColor(1, COLOR_RED)
        time.sleep(0.2)

except KeyboardInterrupt:
    pass