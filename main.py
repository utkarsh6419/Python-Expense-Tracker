"""A small CSV-backed expense tracker."""

import csv
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.csv")


def main():
    while True:
        print("\n1) Add expense  2) Show total  3) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            category = input("Category: ").strip()
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Enter a valid amount.")
                continue
            new_file = not DATA_FILE.exists()
            with DATA_FILE.open("a", newline="") as file:
                writer = csv.writer(file)
                if new_file:
                    writer.writerow(["category", "amount"])
                writer.writerow([category, amount])
        elif choice == "2":
            if not DATA_FILE.exists():
                print("No expenses yet.")
                continue
            with DATA_FILE.open(newline="") as file:
                entries = list(csv.DictReader(file))
            total = sum(float(entry["amount"]) for entry in entries)
            print(f"Total expenses: {total:.2f}")
        elif choice == "3":
            return
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
