# TO Find accuracy and Other metrics and send to Telegram bot with photos


import cv2
from cvzone.PoseModule import PoseDetector
import pyglet.media
import threading
import os
import requests
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Initialize webcam
cap = cv2.VideoCapture(0)  # webcam
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera can't open!!!")
    exit()

# Initialize pose detector and sound
detector = PoseDetector()
sound = pyglet.media.load("alarm.wav", streaming=False)

# Variables for detection and sending notifications
people = False
img_count, breakcount = 0, 0
photo_counter = 0

# Variables for evaluation metrics
ground_truths = []
predictions = []

def sendTelegram(img=None, img_name=None, metrics=None):
    path = r"D:\Desktop\MINOR PROJECTS\MInor project 5\smart cctv upgrade with multithreading"  # Replace with your actual path
    url = f'https://api.telegram.org/bot7475561030:AAEZd3PtrfYnJZN9AYfnRJ39wa4dKlrMPUU/sendPhoto'
    token = "7475561030:AAEZd3PtrfYnJZN9AYfnRJ39wa4dKlrMPUU"  # Replace with your actual token
    chat_id = "1744614668"  # Replace with your actual chat ID

    if img is not None and img_name is not None:
        # Ensure the directory exists
        if not os.path.exists(path):
            os.makedirs(path)

        # Construct the full file path
        file_path = os.path.join(path, img_name)

        # Save the image
        cv2.imwrite(file_path, img)

        # Open the file for sending
        with open(file_path, 'rb') as file:
            files = {'photo': file}
            params = {'chat_id': chat_id, 'caption': "People Detected!!!"}
            resp = requests.post(url, params=params, files=files)
            print(f'Response Code: {resp.status_code}')
            print(f'Response Content: {resp.text}')
    elif metrics is not None:
        metrics_message = (
            f"Detection Metrics:\n"
            f"Accuracy: {metrics['accuracy']}\n"
            f"True Positives (TP): {metrics['tp']}\n"
            f"False Positives (FP): {metrics['fp']}\n"
            f"True Negatives (TN): {metrics['tn']}\n"
            f"False Negatives (FN): {metrics['fn']}\n"
            f"Precision: {metrics['precision']}\n"
            f"Recall: {metrics['recall']}\n"
            f"F1 Score: {metrics['f1']}"
        )
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        params = {'chat_id': chat_id, 'text': metrics_message}
        resp = requests.post(url, params=params)
        print(f'Response Code: {resp.status_code}')
        print(f'Response Content: {resp.text}')

while True:
    success, img = cap.read()
    
    if not success:
        print("Failed to capture image")
        continue
    
    img = detector.findPose(img, draw=False)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
    img_name = f'image_{img_count}.png'

    teleThread = threading.Thread(target=sendTelegram, args=(img, img_name))
    soundThread = threading.Thread(target=sound.play, args=())

    # Assuming a method to get ground truth (replace with actual ground truth retrieval)
    ground_truth = 1  # Replace with actual ground truth label: 1 if person is expected, 0 otherwise

    if bboxInfo:
        cv2.rectangle(img, (120, 20), (470, 80), (0, 0, 255), cv2.FILLED)
        cv2.putText(img, "PEOPLE DETECTED!!!", (130, 60),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        breakcount += 1

        if breakcount >= 30:
            if not people:
                img_count += 1
                photo_counter += 1
                soundThread.start()
                teleThread.start()
                people = not people

        prediction = 1
    else:
        breakcount = 0
        if people:
            people = not people

        prediction = 0

    # Collect ground truth and prediction
    ground_truths.append(ground_truth)
    predictions.append(prediction)

    # Stop after taking 2 photos of any person
    if photo_counter >= 2:
        break

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Calculate evaluation metrics
conf_matrix = confusion_matrix(ground_truths, predictions)
tn, fp, fn, tp = conf_matrix.ravel()
accuracy = accuracy_score(ground_truths, predictions)
precision = precision_score(ground_truths, predictions)
recall = recall_score(ground_truths, predictions)
f1 = f1_score(ground_truths, predictions)

# Print the results
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"Accuracy: {accuracy}")
print(f"True Positives (TP): {tp}")
print(f"False Positives (FP): {fp}")
print(f"True Negatives (TN): {tn}")
print(f"False Negatives (FN): {fn}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")

# Send metrics to Telegram
metrics = {
    'accuracy': accuracy,
    'tp': tp,
    'fp': fp,
    'tn': tn,
    'fn': fn,
    'precision': precision,
    'recall': recall,
    'f1': f1
}
sendTelegram(metrics=metrics)

cv2.destroyAllWindows()
cap.release()
