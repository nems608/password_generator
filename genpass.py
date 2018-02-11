#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser(description='Generate easy to remember, random passwords', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-w', metavar='wordlist', type=str, help='Wordlist to get words from')
parser.add_argument('--csv', metavar='rows', type=int, help='Output in CSV format with \'rows\' passwords per column')
parser.add_argument('--min-word-length', metavar='min_len', type=int, default=4, help='Minimum length of words to use')
parser.add_argument('--max-word-length', metavar='min_len', type=int, default=10, help='Maximum length of words to use')
parser.add_argument('format_str', type=str, help='Format string for generating passwords.\n%%a: Alpha characters\n%%n: Numbers\n%%w: Words\n%%s: Special characters')
parser.add_argument('num_passwords', metavar='N', type=int, help='The number of passwords to generate')

if __name__ == '__main__':
    args = parser.parse_args()
