import cv2
import numpy as np

# Open the camera
cap = cv2.VideoCapture('http://127.0.0.1:8080?action=stream')  

# Set frame size (width, height)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Define color range for detecting black line
lower_color = np.array([0, 0, 0])       # Lower bound for black color
upper_color = np.array([180, 255, 50])  # Upper bound for black color

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Apply thresholding to detect the black line
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Divide the image into 3 horizontal sections
    height, width = mask.shape
    section_height = height // 3

    # Define 5 points for detection in each section
    detect_points = [
        (int(width * 0.1), section_height // 2),  # Top-left
        (int(width * 0.3), section_height // 2),  # Top-left-center
        (int(width * 0.5), section_height // 2),  # Top-center
        (int(width * 0.7), section_height // 2),  # Top-right-center
        (int(width * 0.9), section_height // 2),  # Top-right
        (int(width * 0.1), section_height + section_height // 2),  # Middle-left
        (int(width * 0.3), section_height + section_height // 2),  # Middle-left-center
        (int(width * 0.5), section_height + section_height // 2),  # Middle-center
        (int(width * 0.7), section_height + section_height // 2),  # Middle-right-center
        (int(width * 0.9), section_height + section_height // 2),  # Middle-right
        (int(width * 0.1), 2 * section_height + section_height // 2),  # Bottom-left
        (int(width * 0.3), 2 * section_height + section_height // 2),  # Bottom-left-center
        (int(width * 0.5), 2 * section_height + section_height // 2),  # Bottom-center
        (int(width * 0.7), 2 * section_height + section_height // 2),  # Bottom-right-center
        (int(width * 0.9), 2 * section_height + section_height // 2),  # Bottom-right
    ]

    # Initialize a dictionary to store detection status for all points
    detection_status = {}

    # Check if line passes through detection points
    for i, (x, y) in enumerate(detect_points):
        if mask[y, x] > 0:  # If the pixel value at this point is part of the line
            detection_status[f"Point {i + 1}"] = "Detected"
            cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)  # Mark detected points with green circles
        else:
            detection_status[f"Point {i + 1}"] = "Not Detected"
            cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)  # Mark undetected points with red circles

   

    # Show the original frame and the mask
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
