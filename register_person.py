import cv2
import os
import csv

# -----------------------------
# Configuration
# -----------------------------
DATASET_DIR = "Dataset"
DATABASE_DIR = "Database"
DATABASE_FILE = os.path.join(DATABASE_DIR, "persons.csv")

CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

MAX_IMAGES = 50

# -----------------------------
# Create folders if missing
# -----------------------------
os.makedirs(DATASET_DIR, exist_ok=True)
os.makedirs(DATABASE_DIR, exist_ok=True)

# -----------------------------
# Create database if missing
# -----------------------------
if not os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["PersonID", "Name"])

# -----------------------------
# Load Haar Cascade
# -----------------------------
face_detector = cv2.CascadeClassifier(CASCADE_PATH)

if face_detector.empty():
    print("Failed to load Haar Cascade.")
    exit()

print("=" * 45)
print(" SMART ATTENDANCE SYSTEM ")
print("=" * 45)

person_id = input("Enter Person ID : ").strip().upper()
name = input("Enter Name      : ").strip().title()

if person_id == "" or name == "":
    print("Invalid input.")
    exit()

# -----------------------------
# Check Duplicate ID
# -----------------------------
with open(DATABASE_FILE, "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        if row[0] == person_id:
            print("\nPerson ID already exists!")
            exit()

# -----------------------------
# Save Person Details
# -----------------------------
with open(DATABASE_FILE, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([person_id, name])

# -----------------------------
# Create Dataset Folder
# -----------------------------
person_folder = os.path.join(DATASET_DIR, person_id)

os.makedirs(person_folder, exist_ok=True)

# -----------------------------
# Start Camera
# -----------------------------
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Unable to access camera.")
    exit()

print("\nCamera Started...")
print("Look towards the camera.")
print("Move your face slowly.")
print("Press Q to cancel.\n")

count = 0

while True:

    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(100, 100)
    )

    # Only one face should be visible
    if len(faces) != 1:

        cv2.putText(frame,
                    "Show exactly ONE face",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2)

        cv2.imshow("Register Person", frame)

        if cv2.waitKey(1) == ord('q'):
            break

        continue

    # One face detected
    (x, y, w, h) = faces[0]

    face = gray[y:y+h, x:x+w]
    face = cv2.resize(face, (200, 200))

    count += 1

    if count <= 10:
        instruction = "Look Straight"

    elif count <= 20:
        instruction = "Turn Left"

    elif count <= 30:
        instruction = "Turn Right"

    elif count <= 40:
        instruction = "Look Up"

    else:
        instruction = "Smile"

    filename = os.path.join(person_folder, f"{count}.jpg")
    cv2.imwrite(filename, face)

    cv2.rectangle(frame,
                  (x, y),
                  (x+w, y+h),
                  (0, 255, 0),
                  2)

    cv2.putText(frame,
                f"{count}/{MAX_IMAGES}",
                (15, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2)

    cv2.putText(
        frame,
        instruction,
        (15, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    cv2.imshow("Register Person", frame)

    key = cv2.waitKey(100)

    if key == ord('q'):
        break

    if count >= MAX_IMAGES:
        break

camera.release()
cv2.destroyAllWindows()

print("\nRegistration Completed")
print("--------------------------")
print("ID   :", person_id)
print("Name :", name)
print("Images Captured :", count)
print("--------------------------")