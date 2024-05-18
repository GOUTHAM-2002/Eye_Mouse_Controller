import cv2
import mediapipe as mp
import pyautogui

face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)  # get the face_mesh detector from mediapipe
cam = cv2.VideoCapture(0)  # detecting the first camera
while True:
    _, frame = cam.read()  # read every frame from camera
    frame = cv2.flip(frame,1) #flip camera vertically
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert frame to rgb so that mediapipe can use it
    output = face_mesh.process(rgb_frame)  # mediapipe processing
    landmark_points = output.multi_face_landmarks  # initializes the face points to a variable
    frame_h, frame_w, _ = frame.shape #getting frame dimensions to draw
    if landmark_points:
        landmarks = landmark_points[0].landmark #landmark of the first face
        for id, landmark in enumerate(landmarks[474:478]):  # selecting only the iris landmarks
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))  #printing out the landmarks as circles
            if id ==1:
                pyautogui.moveTo(x,y) #moving cursor
    cv2.imshow("Eye controlled Mouse", frame)  # display the frame
    cv2.waitKey(1)  # wait 1 millisecond for a key and renders frame
