import functools
from collections import Counter
from re import compile


def char_adviser(subset_inner):
    numb_of_attempts: int = 0
    loop_count: int = 1
    word_most_common_inner: str = subset_inner.most_common(1)[0][0]
    times_most_common: int = char_frequency_dict.most_common(1)[0][1]
    sum_of_chars = sum(subset_inner.values())
    probability: float = round((times_most_common / sum_of_chars)*100, 2)
    while True:
        is_present: str = "N/A"
        while is_present not in ["y", "n"]:
            is_present = input(f"Is ' {word_most_common_inner} ' character in the word? (probability of that = {probability}%), y/n | ")
        if is_present == 'y':
            numb_of_attempts += 1
            return word_most_common_inner, numb_of_attempts
        else:
            if loop_count == len(subset_inner):
                print("I have no new character to propose, please be more attentive, I'm starting over")
                loop_count = 0
                numb_of_attempts = 0
            asked_letter.append(word_most_common_inner)
            word_most_common_inner: str = subset_inner.most_common(loop_count + 1)[loop_count][0]
            times_most_common: int = char_frequency_dict.most_common(loop_count + 1)[loop_count][1]
            probability: float = round((times_most_common / sum_of_chars)*100, 2)
            numb_of_attempts += 1
            loop_count += 1


def check_pattern(word_pattern_inner: str, word_most_common_inner: str) -> str:
    while True:
        if word_pattern_inner.count('_') == 1:
            print(f'I guessed your word - "{word_pattern_inner.replace("_",f"{word_most_common_inner}")}" in {total_numb_of_attempts} attempt(s).')
            return 'finish'
        word_pattern_gener: str = input(f'Supersede all "_" with "{word_most_common_inner}" in your pattern {word_pattern_inner} | ')  # .lower().replace(" ", "")
        word_pattern_inner_re = compile(f'{word_pattern_inner.replace("_", f"[{word_most_common_inner}_{word_most_common_inner.upper()}]")}')
        iscorrect: list = word_pattern_inner_re.findall(word_pattern_gener)
        if len(iscorrect) > 0 and iscorrect[0] != word_pattern_inner.replace(" ", "").lower():
            return word_pattern_gener
        else:
            print("please enter valid pattern")


try:
    file_name = input('Enter the path to the "word.txt" file | ')
    file_data_object = open(file_name, mode='r', encoding='UTF-8')
    content = file_data_object.read()
    file_data_object.close()

    w_length_str = input("How many characters does your word have? (use digits) | ")
    if w_length_str.isdigit():
        w_length_int = int(w_length_str)
    else:
        print('Be more attentive')
        quit()

    word_pattern: str = "_" * w_length_int
    print(f"Here is your pattern {word_pattern}. Please use letters' case as in your document")
    word_length: int = len(word_pattern)
    subset = [word for word in content.split() if len(word) == word_length]
    asked_letter = []
    if len(subset) == 0:
        print(f"Are you sure about your word's length? Please check it and try again!")
        quit()
    char_frequency_dict = Counter()
    total_numb_of_attempts = 0
    while True:
        print(f"Data set volume to choose from has {len(subset)} words")
        for char in functools.reduce(lambda x, y: x+y, subset):
            if char.lower() not in word_pattern.lower() and char.lower() not in asked_letter:
                char_frequency_dict[char.lower()] += 1
        word_most_common_outer, attempts = char_adviser(char_frequency_dict)
        total_numb_of_attempts += attempts
        valid_pattern: str = check_pattern(word_pattern, word_most_common_outer)
        if valid_pattern != 'finish':
            pattern_replaced = valid_pattern.replace('_', "[À-Ža-zA-Z']")
            prefix = r'\\b'+pattern_replaced
            re_pattern = compile(prefix[1:])
            matches = re_pattern.findall(" ".join(subset))
            subset: list = matches
            if len(subset) == 1:
                print(f'I guessed your word - "{subset[0]}" in {total_numb_of_attempts} attempt(s) ')
                break
            elif len(subset) == 0:
                print(f'I have found nothing by your pattern {valid_pattern}')
                break
            else:
                word_pattern: str = valid_pattern
                char_frequency_dict.clear()
        else:
            break

except Exception as Ex:
    print(f'Error message >>> {Ex}')
    quit()






