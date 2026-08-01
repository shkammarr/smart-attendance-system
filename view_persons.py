import csv
import os

DATABASE = "Database/persons.csv"

os.system("cls")

print("=" * 45)
print("REGISTERED PERSONS")
print("=" * 45)

try:

    with open(DATABASE, "r") as file:

        reader = csv.reader(file)

        next(reader)

        print(f"{'ID':<15}{'NAME'}")

        print("-" * 40)

        for row in reader:

            print(f"{row[0]:<15}{row[1]}")

except FileNotFoundError:

    print("Database not found.")

print("\n")