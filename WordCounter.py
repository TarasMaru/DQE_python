from re import compile
from collections import Counter
from argparse import ArgumentParser


def my_counter(file_name):
    # Open and read file
    try:
        file_data = open(file_name, mode='r', encoding='UTF-8')
        content = file_data.read()
        file_data.close()
    except:
        print(f'File cannot be opened or read: {file_name}')
        quit()
    try:
        # Regex
        pattern = compile(r'\b[a-zA-Z]+')  # r'\b[a-zA-Z]+-?[a-zA-Z]*' - to capture hyphenated words
        matches = pattern.findall(content)
        # Count words occurrence
        words_count = Counter()
        for word in matches:
            words_count[word.upper().lower().capitalize()] += 1
        # sorting output
        sorted_dict = {}
        for word in sorted(dict(words_count).keys()):
            sorted_dict[word] = words_count[word]
        return sorted_dict
    except Exception as E:
        return E


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-p', '--path', type=str, help='enter absolute file path', required=True)
    args = parser.parse_args()
    file_path = args.path
    result = my_counter(file_name=file_path)
    print(result)

