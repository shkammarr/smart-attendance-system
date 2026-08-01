import os

# ----------------------------
# Project Folders
# ----------------------------

DATABASE_FOLDER = "Database"
ATTENDANCE_FOLDER = os.path.join(DATABASE_FOLDER, "Attendance")
DATASET_FOLDER = "Dataset"
TRAINER_FOLDER = "Trainer"

# ----------------------------
# Files
# ----------------------------

PERSONS_FILE = os.path.join(DATABASE_FOLDER, "persons.csv")
TRAINER_FILE = os.path.join(TRAINER_FOLDER, "trainer.yml")

# ----------------------------
# Camera
# ----------------------------

CAMERA_ID = 0
IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480

# ----------------------------
# Face Detection
# ----------------------------

FACE_WIDTH = 200
FACE_HEIGHT = 200

# ----------------------------
# Recognition
# ----------------------------

CONFIDENCE_THRESHOLD = 50

# ----------------------------
# Attendance
# ----------------------------

EXCEL_SHEET_NAME = "Attendance"

# ----------------------------
# Create folders automatically
# ----------------------------

os.makedirs(DATABASE_FOLDER, exist_ok=True)
os.makedirs(ATTENDANCE_FOLDER, exist_ok=True)
os.makedirs(DATASET_FOLDER, exist_ok=True)
os.makedirs(TRAINER_FOLDER, exist_ok=True)

