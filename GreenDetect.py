# initialize openCV
import cv2

# Initialize Arduino connect with python
import serial
import time

# Initialize Serial Signal
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)


# read what signal does OPENCV provide
def readSign(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def detectColor(camera):

    cap = cv2.VideoCapture(camera)
    if not cap.isOpened():
        print("Error: Could not open camera")
    else:
        # Loop through the video frames
        while True:
            # Read a frame from the camera
            ret, frame = cap.read()

            # Check if the frame was successfully read
            if not ret:
                print("Error: Could not read frame from camera")
                break

            # Convert the frame to the HSV color space
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Define a range of blue color in HSV color space
            lower_green = (40, 50, 50)
            upper_green = (80, 255, 255)

            # Threshold the HSV image to get only blue colors
            green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)

            # Find contours of blue regions in the image
            contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            green_detected = False
            # Draw contours on the original image
            for contour in contours:
                area = cv2.contourArea(contour)

                if area > 500:
                    cv2.drawContours(frame, [contour], 0, (255, 0, 0), 2)
                    green_detected = True

            if green_detected:
                value = readSign("1")
                print("1")
            else:
                value = readSign("0")
                print("0")

            # Display the frame9999
            cv2.imshow('Camera', frame)

            # Wait for 1 millisecond and check if the 'q' key was pressed
            if cv2.waitKey(1) == ord('q'):
                break

        # Save the last frame as an image file
        cv2.imwrite('last_frame.jpg', frame)

        # Release the camera and close the window
        cap.release()
        cv2.destroyAllWindows()
    return green_detected


detectColor(1)