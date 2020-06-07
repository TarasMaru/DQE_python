import csv
import json
import argparse
import os
from typing import List, Dict
from pprint import pprint

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Specify csv file path after -c, and json file path after -j')
    parser.add_argument('-c', '--csv', type=str, help='Enter a path to you csv file', required=True)
    parser.add_argument('-j', '--json', type=str, help='Enter a path to you json file', default=f'{os.getcwd()}\\user_details.json')
    args = parser.parse_args()

    col_types: List = [int, str, str, str, str, str, int]

    #  1. check if entered csv is valid.
    #  2. check if entered json path is valid in terms of directories existence.
    #  3. check if entered json path is valid in terms of file extension.
    #  4. check if entered csv path is valid in terms of file extension.
    if os.path.exists(args.csv) and os.path.isdir(os.path.dirname(args.json)) \
            and os.path.splitext(args.json)[1] == '.json' and os.path.splitext(args.csv)[1] == '.csv':
        with open(f'{args.csv}', 'r') as f:
            csv_data = csv.reader(f)

            headers = tuple(next(csv_data))  # tuple of csv file headers.

            list_dict_data: List[Dict] = []  # desired data structure: list of dictionaries.

            for row in csv_data:
                row_typed = tuple(convert(value) for convert, value in zip(col_types, row))
                list_dict_data.append({headers[0]: row_typed[0], headers[1]: row_typed[1], headers[2]: row_typed[2],
                                       headers[3]: row_typed[3], headers[4]: row_typed[4], headers[6]: row_typed[6]})

        with open(f'{args.json}', 'w') as f:
            json.dump(list_dict_data, f, indent=2, sort_keys=True)

        pprint(list_dict_data, indent=2, sort_dicts=True)
        print(f"This output was written into {args.json}")

    else:
        print("Invalid path(s)\nPlease try again...")


