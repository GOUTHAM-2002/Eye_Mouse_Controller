import cv2
import mediapipe as mp
import pyautogui

# Initialize face_mesh detector from mediapipe
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Detecting the first camera
cam = cv2.VideoCapture(0)

# Get screen dimensions
screen_w, screen_h = pyautogui.size()

while True:
    success, frame = cam.read()  # Read frame from camera
    if not success:
        break  # Break loop if frame is not successfully read

    frame = cv2.flip(frame, 1)  # Flip camera horizontally
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame to RGB for mediapipe
    output = face_mesh.process(rgb_frame)  # Process the frame with mediapipe
    landmark_points = output.multi_face_landmarks  # Get the face landmarks

    frame_h, frame_w, _ = frame.shape  # Get frame dimensions

    if landmark_points:
        landmarks = landmark_points[0].landmark  # Get landmarks of the first face
        for id, landmark in enumerate(landmarks[474:478]):  # Select iris landmarks
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)  # Draw circles for landmarks

            if id == 1:  # Use landmark 475 for cursor movement
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(screen_x, screen_y)  # Move cursor

    cv2.imshow("Eye Controlled Mouse", frame)  # Display the frame
    if cv2.waitKey(1) & 0xFF == 27:  # Exit on pressing ESC key
        break

cam.release()  # Release the camera
cv2.destroyAllWindows()  # Close all OpenCV windows
