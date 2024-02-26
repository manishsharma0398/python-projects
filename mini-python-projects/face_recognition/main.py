import cv2
import face_recognition
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

my_image = face_recognition.load_image_file("faces/image.jpg")
image_encoding = face_recognition.face_encodings(my_image)

known_face_encodings = [image_encoding]
known_face_names = ["Manish"]

# list of expected students
students = known_face_names.copy()
