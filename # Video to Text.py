# Video to Text
import cv2

video_path = input('Paste Video link')
cap = cv2.VideoCapture(video_path)

fps = cap.get(cap.CAP_PROP_FPS)