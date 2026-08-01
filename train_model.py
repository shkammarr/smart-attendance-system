import cv2
import os
import numpy as np
from PIL import Image

# ----------------------------
# Paths
# ----------------------------

DATASET_PATH = "Dataset"
TRAINER_PATH = "Trainer"

os.makedirs(TRAINER_PATH, exist_ok=True)

recognizer = cv2.face.LBPHFaceRecognizer_create()

detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# ----------------------------
# Read Images
# ----------------------------

faces = []
ids = []

print("="*50)
print("Training Started...")
print("="*50)

person_count = 0
image_count = 0

for person_folder in os.listdir(DATASET_PATH):

    folder_path = os.path.join(DATASET_PATH, person_folder)

    if not os.path.isdir(folder_path):
        continue

    person_id = int(person_folder)

    person_count += 1

    for image_name in os.listdir(folder_path):

        image_path = os.path.join(folder_path, image_name)

        img = Image.open(image_path).convert('L')

        img_numpy = np.array(img, 'uint8')

        faces_detected = detector.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces_detected:

            faces.append(img_numpy[y:y+h, x:x+w])

            ids.append(person_id)

            image_count += 1


print(f"\nPersons Found : {person_count}")
print(f"Images Found  : {image_count}")

print("\nTraining Model...")

recognizer.train(faces, np.array(ids))

recognizer.save(os.path.join(TRAINER_PATH, "trainer.yml"))

print("\nModel Trained Successfully!")
print("Saved As : Trainer/trainer.yml")

print("="*50)

if len(faces)==0:
    print("No dataset found.")
    exit()