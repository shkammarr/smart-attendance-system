import csv
import os

DATABASE_FILE = "Database/persons.csv"


def load_persons():
    persons = {}

    if not os.path.exists(DATABASE_FILE):
        return persons

    with open(DATABASE_FILE, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            persons[int(row["PersonID"])] = {
                "name": row["Name"]
            }

    return persons


def get_name(person_id):

    persons = load_persons()

    if person_id in persons:
        return persons[person_id]["name"]

    return "Unknown"