import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
np_pose = mp.solutions.pose

#Video Feed
cap = cv2.VideoCapture(0)

import cv2
import mediapipe as mp

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize MediaPipe pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils


with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the image horizontally for a mirror-like effect (optional)
        frame = cv2.flip(frame, 1)

        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Improve performance by marking the image as read-only
        rgb_frame.flags.writeable = False

        # Process the frame with MediaPipe
        results = pose.process(rgb_frame)

        # Allow drawing on the image again
        rgb_frame.flags.writeable = True

        # Convert RGB back to BGR for OpenCV display
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

        try:
            landmark = results.pose_landmark.landmark # tries to get list of body points
        except:
            pass # quitely pass the frame if it dosen't detect person or crash 

        # Draw pose landmarks on the frame
        if results.pose_landmarks:
            mp_drawing.draw_landmarks( 
                frame, 
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS, 
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),  # red dots (BGR)
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)  # blue lines
                
             )


        # Show the frame
        cv2.imshow("Pose Detection", frame)

        # Break loop with 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
