#!/usr/bin/python
import argparse
import string
import random
import datetime

parser = argparse.ArgumentParser(
                    description='Generate easy to remember, random passwords',
                    formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-w', metavar='wordlist', type=str,
                    help='Wordlist to get words from')
parser.add_argument('--csv', metavar='rows', type=int,
                help='Output in CSV format with \'rows\' passwords per column')
parser.add_argument('--min-word-length', metavar='min_len', type=int,
                    default=4, help='Minimum length of words to use')
parser.add_argument('--max-word-length', metavar='min_len', type=int,
                    default=10, help='Maximum length of words to use')
parser.add_argument('format_str', type=str,
                    help=('Format string for generating passwords.\n'
                        '%%a: Alpha character\n'
                        '%%n: Number\n'
                        '%%w: Lowercase word\n'
                        '%%W: Titlecase word\n'
                        '%%s: Special character\n'
                        '%%%%: Percent character\n'
                        '!-~: Any static ascii character'))
parser.add_argument('num_passwords', metavar='N', type=int,
                    help='The number of passwords to generate')

alpha = string.ascii_letters
numbers = string.digits
special = '!#$%&()*+-./:;<=>?@[]^_{}'

def generate_wordlist(path, min_len, max_len):
    global wordlist
    if path is None:
        wordlist = None
        return

    wordlist = []
    f = open(path, 'r')
    words = f.read().split('\n')
    f.close()
    for word in words:
        if min_len <= len(word) <= max_len:
            wordlist.append(word)

def random_alpha():
    return random.choice(alpha)

def random_number():
    charset = string.digits
    return random.choice(numbers)

def random_special():
    return random.choice(special)

def random_word(titlecase):
    if wordlist is None:
        raise Exception('No wordlist specified')

    word = random.choice(wordlist)
    if titlecase:
        word = word.title()
    else:
        word = word.lower()
    return word

def generate_passwords(format_str, num):
    passwords = []
    for i in range(num):
        password = ''
        c = 0
        while c < len(format_str):
            if format_str[c] != '%':
                password += format_str[c]
                c += 1
            else:
                if format_str[c+1] == 'a':
                    password += random_alpha()
                elif format_str[c+1] == 'n':
                    password += random_number()
                elif format_str[c+1] == 'w':
                    password += random_word(titlecase=False)
                elif format_str[c+1] == 'W':
                    password += random_word(titlecase=True)
                elif format_str[c+1] == 's':
                    password += random_special()
                elif format_str[c+1] == '%':
                    password += '%'
                else:
                    print(format_str[c:c+2])
                    raise Exception('Improper format string: %s' % format_str)
                c += 2
        passwords.append(password)
    return passwords

def output_passwords(passwords, rows):
    if rows is None:
        rows = len(passwords)

    output = []
    num_passwords = len(passwords)
    for i in range(rows):
        pass_idx = i
        line = ''
        while pass_idx < num_passwords:
            line += passwords[pass_idx]
            line += ','
            pass_idx += rows
        output.append(line[:-1])
    for line in output:
        print(line)

def calc_strength(format_str):
    strength = 1
    c = 0
    while c < len(format_str):
        if format_str[c] != '%':
            c += 1
        else:
            if format_str[c+1] == 'a':
                strength *= len(alpha)
            elif format_str[c+1] == 'n':
                strength *= len(numbers)
            elif format_str[c+1] in ['w', 'W']:
                strength *= len(wordlist)
            elif format_str[c+1] == 's':
                strength *= len(special)
            elif format_str[c+1] == '%':
                pass
            else:
                print(format_str[c:c+2])
                raise Exception('Improper format string: %s' % format_str)
            c += 2
    print('Strength: %d' % strength)
    hash_speed = 50*10**9
    crack_sec = strength / hash_speed
    t = str(datetime.timedelta(seconds=crack_sec))
    print('Time to crack: %s\n' % t)


if __name__ == '__main__':
    args = parser.parse_args()

    generate_wordlist(args.w, args.min_word_length, args.max_word_length)
    calc_strength(args.format_str)
    passwords = generate_passwords(args.format_str, args.num_passwords)
    output_passwords(passwords, args.csv)
