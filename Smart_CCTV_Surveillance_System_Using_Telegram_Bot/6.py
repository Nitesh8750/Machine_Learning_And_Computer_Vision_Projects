# Smart CCTV Survellance Telegram Bot Project 
# It Also Categorise between known and Unknown Person

import cv2
import face_recognition
import os
import numpy as np
import pyglet.media
import threading
import requests

# Load reference images and encode faces
reference_images_path = 'reference_images'
known_face_encodings = []
known_face_names = []

for filename in os.listdir(reference_images_path):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(reference_images_path, filename)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(filename.split('.')[0])  # Use the filename (without extension) as the name

# Video capture
cap_2 = cv2.VideoCapture(0)  # Webcam

def sendTelegram(img, img_name):
    path = r"D:\Desktop\MINOR PROJECTS\MInor project 5\smart cctv upgrade with multithreading"  # Replace with your actual path
    url = f'https://api.telegram.org/bot7475561030:AAEZd3PtrfYnJZN9AYfnRJ39wa4dKlrMPUU/sendPhoto'
    token = "7475561030:AAEZd3PtrfYnJZN9AYfnRJ39wa4dKlrMPUU"  # Replace with your actual token
    chat_id = "1744614668"  # Replace with your actual chat ID
    caption = "Unknown person detected!"

    if not os.path.exists(path):
        os.makedirs(path)

    file_path = os.path.join(path, img_name)
    cv2.imwrite(file_path, img)

    with open(file_path, 'rb') as file:
        files = {'photo': file}
        params = {'chat_id': chat_id, 'caption': caption}
        resp = requests.post(url, params=params, files=files)
        print(f'Response Code: {resp.status_code}')
        print(f'Response Content: {resp.text}')

people = False
img_count = 0
sound = pyglet.media.load("alarm.wav", streaming=False)

while True:
    success_2, img_2 = cap_2.read()
    
    if not success_2:
        print("Failed to capture image from webcam")
        continue
    
    # Rotate image to vertical orientation
    #img_2 = cv2.rotate(img_2, cv2.ROTATE_90_CLOCKWISE)
    
    # Detect faces
    face_locations = face_recognition.face_locations(img_2)
    face_encodings = face_recognition.face_encodings(img_2, face_locations)

    unknown_face_found = False
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        if True not in matches:
            unknown_face_found = True
            cv2.rectangle(img_2, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(img_2, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            cv2.putText(img_2, "UNKNOWN", (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    if unknown_face_found:
        cv2.rectangle(img_2, (120, 20), (470, 80), (0, 0, 255), cv2.FILLED)
        cv2.putText(img_2, "UNKNOWN PEOPLE DETECTED!!!", (130, 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

        if not people:
            img_name = f'image_{img_count}.png'
            img_count += 1
            threading.Thread(target=sound.play).start()
            threading.Thread(target=sendTelegram, args=(img_2, img_name)).start()
            people = not people
    else:
        if people:
            people = not people

    cv2.imshow("Webcam Stream", img_2)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap_2.release()
cv2.destroyAllWindows()
