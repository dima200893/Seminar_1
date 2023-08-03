import csv
import pickle
from pathlib import Path

def conv_to_csv(file_name: Path) -> None:
    with (open(file_name, 'rb') as f_pickle,
          open(f'{file_name.stem}.csv', "w", newline='', encoding='utf-8') as f_csv):
        new_dict = pickle.load(f_pickle)

        csv_write = csv.writer(f_csv, dialect='excel', delimiter=',')
        csv_write.writerow(new_dict.keys())

        n= [str(i).split() for i in new_dict.values()]
        csv_write.writerow(n)

if __name__ == "__main__":
    conv_to_csv(Path("names.pickle"))
