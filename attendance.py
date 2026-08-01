import os
from datetime import datetime

import cv2

from database import get_name
from utils import mark_attendance, already_marked

# ==========================
# Paths
# ==========================

MODEL_PATH = "Trainer/trainer.yml"

CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

# ==========================
# Check Files
# ==========================

if not os.path.exists(MODEL_PATH):
    print("Error : Trainer model not found.")
    print("Run train_model.py first.")
    exit()

# ==========================
# Load Recognizer
# ==========================

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(MODEL_PATH)

# ==========================
# Load Face Detector
# ==========================

faceCascade = cv2.CascadeClassifier(CASCADE_PATH)

if faceCascade.empty():
    print("Error loading Haar Cascade.")
    exit()

# ==========================
# Camera
# ==========================

camera = cv2.VideoCapture(0)

camera.set(3, 640)
camera.set(4, 480)

if not camera.isOpened():
    print("Camera not detected.")
    exit()

print("=" * 50)
print("Universal Face Attendance System")
print("=" * 50)
print("Camera Started...")
print("Press Q to Exit\n")

# ==========================
# Colors
# ==========================

GREEN = (0,255,0)
RED = (0,0,255)
WHITE = (255,255,255)
BLUE = (255,0,0)

font = cv2.FONT_HERSHEY_SIMPLEX

# ==========================
# Prevent Duplicate
# ==========================

marked_people = set()

recognition_counter = {}
REQUIRED_FRAMES = 5

# ==========================
# Main Loop
# ==========================

while True:

    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=6,
        minSize=(150, 150)
    )

    for (x,y,w,h) in faces:

        face = gray[y:y + h, x:x + w]
        face = cv2.resize(face, (200, 200))

        person_id, confidence = recognizer.predict(face)

        print(f"Predicted ID: {person_id}, Confidence: {confidence:.2f}")

        confidence_percent = round(100 - confidence)

        # ----------------------------
        # Known Person
        # ----------------------------

        if confidence < 50:

            name = get_name(person_id)

            color = GREEN

            # Attendance
            recognition_counter[person_id] = recognition_counter.get(person_id, 0) + 1

            if recognition_counter[person_id] >= REQUIRED_FRAMES:

                if person_id not in marked_people:

                    if not already_marked(person_id):
                        mark_attendance(person_id, name)

                        print(f"Attendance Marked : {name}")

                    marked_people.add(person_id)

            cv2.putText(
                frame,
                f"{name}",
                (x,y-35),
                font,
                0.8,
                color,
                2
            )

            cv2.putText(
                frame,
                f"ID : {person_id}",
                (x,y-10),
                font,
                0.6,
                color,
                2
            )

            cv2.putText(
                frame,
                f"{confidence_percent}%",
                (x,y+h+25),
                font,
                0.6,
                color,
                2
            )

        # ----------------------------
        # Unknown Person
        # ----------------------------

        else:

            color = RED

            cv2.putText(
                frame,
                "Unknown",
                (x,y-10),
                font,
                0.8,
                color,
                2
            )

        # Rectangle

        cv2.rectangle(
            frame,
            (x,y),
            (x+w,y+h),
            color,
            2
        )

    # -------------------------
    # Date
    # -------------------------

    today = datetime.now().strftime("%d-%m-%Y")

    cv2.putText(
        frame,
        today,
        (10,30),
        font,
        0.7,
        BLUE,
        2
    )

    # -------------------------
    # Time
    # -------------------------

    now = datetime.now().strftime("%H:%M:%S")

    cv2.putText(
        frame,
        now,
        (10,60),
        font,
        0.7,
        BLUE,
        2
    )

    # -------------------------
    # Count
    # -------------------------

    cv2.putText(
        frame,
        f"Present : {len(marked_people)}",
        (10,90),
        font,
        0.7,
        GREEN,
        2
    )

    cv2.imshow("Universal Face Attendance System", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()