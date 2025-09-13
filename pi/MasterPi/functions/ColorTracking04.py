#!/usr/bin/python3
# coding=utf8
import sys
import cv2
import time
import signal
import threading
import numpy as np

sys.path.append('/home/pi/MasterPi/')
import common.pid as PID
import common.misc as Misc
import common.yaml_handle as yaml_handle
from common import board
from kinematics import transform

# -------------------------------
# Camera source (IP Webcam)
# -------------------------------
cap = cv2.VideoCapture("http://127.0.0.1:8080?action=stream")

# -------------------------------
# PID setup
# -------------------------------
x_pid = PID.PID(P=0.28, I=0.03, D=0.03)  # for horizontal (servo 6)
y_pid = PID.PID(P=0.28, I=0.03, D=0.03)  # for vertical   (servo 3)

x_dis = 1500  # initial PWM value for servo 6
y_dis = 1500  # initial PWM value for servo 3

x_pid.SetPoint = 320  # frame center X (assume 640x480)
y_pid.SetPoint = 240  # frame center Y (assume 640x480)

# -------------------------------
# HSV color ranges (example)
# -------------------------------
colors = {
    'red':   [(0, 120, 70), (10, 255, 255)],
    'green': [(35, 100, 100), (85, 255, 255)],
    'blue':  [(100, 150, 0), (140, 255, 255)]
}
target_color = 'blue'  # default

# -------------------------------
# Graceful exit
# -------------------------------
stop_event = threading.Event()
def signal_handler(sig, frame):
    stop_event.set()
    cap.release()
    cv2.destroyAllWindows()
signal.signal(signal.SIGINT, signal_handler)

# -------------------------------
# Main Loop
# -------------------------------
print(f"Target color set to: {target_color}")
while not stop_event.is_set():
    ret, frame = cap.read()
    if not ret:
        print("Cannot access camera stream")
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Mask for selected color
    lower, upper = colors[target_color]
    mask = cv2.inRange(hsv, np.array(lower), np.array(upper))

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        c = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(c)
        if area > 500:  # filter noise
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = box.astype(int)

            # Draw bounding box
            cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)

            # Center of object
            M = cv2.moments(c)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

                # -------------------------------
                # PID control
                # -------------------------------
                x_pid.update(cx)
                y_pid.update(cy)

                x_dis += int(x_pid.output)
                y_dis += int(y_pid.output)

                # Clamp servo range
                x_dis = int(Misc.map_value(x_dis, 500, 2500, 500, 2500))
                y_dis = int(Misc.map_value(y_dis, 500, 2500, 500, 2500))

                # Send to board
                board.pwm_servo_set_position(
                    0.02, [[6, x_dis], [3, y_dis]]
                )

                cv2.putText(frame, f"Tracking {target_color}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Color Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
