import csv
import argparse
import os
from typing import List, Dict


def get_file_path(directory: str) -> str:  # return firstly encountered csv file in a specified directory
    for dir_root, dir_name, file_names in os.walk(directory):
        for file in file_names:
            if '.csv' == os.path.splitext(file)[1]:
                return os.path.join(dir_root, file)
            else:
                continue
    print('CSV file was not found.')
    quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Specify directory path where the desired file is located after -p parameter')
    parser.add_argument('-p', '--path', type=str, help='Enter a path to a directory', required=True)
    parser.add_argument('-b', '--beds', type=int, help='Enter a number of HRR you want to see', default=1)
    args = parser.parse_args()
    dict_of_hrr: Dict[str, float] = {}
    with open(f'{get_file_path(args.path)}', 'r') as f:
        f_csv = csv.DictReader(f)
        # the "DictReader" method  was chosen due to:
        # 1) code is more readable e.g.: line["HRR"] better than line[12].
        # 2) code is not sensitive to the columns' arrangement e.g.: line["HRR"] can get value no matter ether column
        # "HRR" is at the beginning or at the end of the file.
        try:
            next(f_csv)  # to skip the first line with "*Based on a 50% reduction in occupancy" value.
            for line in f_csv:
                dict_of_hrr[f'{line["HRR"]}'] = int(line['Available Hospital Beds'].replace(",", "")) / int(
                    line['Total Hospital Beds'].replace(",", ""))  # get unordered dict {HRR: percent_of_free_beds}
        except:
            print("Please make sure the correct file is in the specified directory and it is the only one.")
            quit()
    #  dict_of_hrr could have been made conversely, e.i.: {percent_of_free_beds: HRR} to avoid sorting (the next step)
    ordered_dict_of_hrr: List[str] = sorted(dict_of_hrr.items(), key=lambda x: x[1], reverse=True)
    if args.beds > len(dict_of_hrr):
        print("Value for -b parameter is too big.\nPlease try entering a smaller digit.")
        quit()
    else:
        # printing result
        [print(f'{ordered_dict_of_hrr[i][0]} -> {ordered_dict_of_hrr[i][1]:.1%}') for i in range(args.beds)]