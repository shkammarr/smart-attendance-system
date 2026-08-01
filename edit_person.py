import csv
import os

DATABASE = "Database/persons.csv"

print("=" * 45)
print("EDIT PERSON")
print("=" * 45)

person_id = input("Enter Person ID : ").strip()

if not os.path.exists(DATABASE):
    print("Database not found.")
    exit()

rows = []

found = False

with open(DATABASE, "r", newline="") as file:

    reader = csv.reader(file)

    header = next(reader)

    for row in reader:

        if row[0] == person_id:

            found = True

            print("\nCurrent Name :", row[1])

            new_name = input("Enter New Name : ").strip().title()

            if new_name == "":
                print("Invalid Name.")
                exit()

            row[1] = new_name

        rows.append(row)

if not found:

    print("\nPerson not found.")
    exit()

with open(DATABASE, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(header)

    writer.writerows(rows)

print("\nPerson Updated Successfully!")