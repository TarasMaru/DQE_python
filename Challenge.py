from re import compile
from argparse import ArgumentParser


def my_counter(file_name):
    try:
        file_data = open(file_name, mode='r', encoding='UTF-8')
        content = file_data.read()
        file_data.close()
    except Exception as Ex:
        print(f'Error message >>> {Ex}')
        quit()
    try:
        pattern = compile(r'\b[a-zA-Z]+')
        matches = pattern.findall(content)
        words_count = dict()
        for word in sorted(matches):
            words_count[word.upper().lower().capitalize()] = words_count.get(word.upper().lower().capitalize(), 0) + 1
        return words_count
    except Exception as E:
        return E


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-p', '--path', type=str, help='enter absolute file path', required=True)
    file_path = parser.parse_args().path
    print(my_counter(file_name=file_path))