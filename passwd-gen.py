import random
import string
from typing import Set


DIGITS = string.digits
LETTERS = string.ascii_letters
PUNCTUATIONS = string.punctuation


def get_punc() -> Set[str]:
    use_punc = input('Would you like to include punctuation? Enter y for yes: ')
    if use_punc != 'y':
        return set()
    customize_punc = input('Customize punctuations to use (press enter to use default): ').strip()
    if len(customize_punc) == 0:
        return set(PUNCTUATIONS)
    return set(PUNCTUATIONS) & set(customize_punc)


def generate_password(candidate: Set[str], length: int) -> str:
    tmp = list(candidate)

    s = []
    for _ in range(3):
        random.shuffle(tmp)
        s += tmp

    random.shuffle(s)
    s = s[:min(length * 3, len(s))]
    random.shuffle(s)
    s = s[:min(length * 2, len(s))]
    random.shuffle(s)
    return ''.join(s[:length])


def main():
    print(
        'Thanks for using password generator.\n'
        'The password generated will be based on the 62 basic characters as follow:\n'
        '{}{}'.format(DIGITS, LETTERS, PUNCTUATIONS)
    )
    while True:
        length = input("\nWhat's the length of the password you want? ")
        if length.isdigit():
            length = int(length)
            if 0 < length <= 64:
                break
        print('Please enter a valid position integer with maximum length of 64.')

    punc = get_punc()
    exclude = input('Any character to exclude? Enter without any delimiter: ')
    candidate = set(DIGITS + LETTERS) | punc - set(exclude)

    result = generate_password(candidate, length)
    print(result)


if __name__ == "__main__":
    main()
