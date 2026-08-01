import os
import csv
import shutil
import subprocess

# ----------------------------
# Paths
# ----------------------------

DATABASE = "Database/persons.csv"
DATASET = "Dataset"

print("=" * 45)
print("DELETE PERSON")
print("=" * 45)

person_id = input("Enter Person ID : ").strip()

# ----------------------------
# Check Database
# ----------------------------

if not os.path.exists(DATABASE):
    print("Database not found.")
    exit()

rows = []

found = False
name = ""

with open(DATABASE, "r", newline="") as file:

    reader = csv.reader(file)

    header = next(reader)

    for row in reader:

        if row[0] == person_id:

            found = True
            name = row[1]

        else:
            rows.append(row)

if not found:

    print("\nPerson not found.")
    exit()

# ----------------------------
# Confirmation
# ----------------------------

print("\nPerson Found")

print("ID   :", person_id)
print("Name :", name)

choice = input("\nDelete this person? (Y/N): ").upper()

if choice != "Y":

    print("Cancelled.")
    exit()

# ----------------------------
# Rewrite Database
# ----------------------------

with open(DATABASE, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(header)

    writer.writerows(rows)

# ----------------------------
# Delete Dataset
# ----------------------------

folder = os.path.join(DATASET, person_id)

if os.path.exists(folder):

    shutil.rmtree(folder)

# ----------------------------
# Retrain
# ----------------------------

print("\nRetraining model...")

subprocess.run(["python", "train_model.py"])

print("\nPerson Deleted Successfully!")