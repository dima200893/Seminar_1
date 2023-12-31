import csv
import pickle
from pathlib import Path

def print_pickl_str(file_name: Path) -> None:
    with open(file_name, "r", newline='', encoding='utf-8') as f_csv:
        print(pickle.dumps(f_csv.read()))

if __name__ == "__main__":
    print_pickl_str(Path("new_user.csv"))