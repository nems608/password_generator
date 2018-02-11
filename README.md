usage: genpass.py [-h] [-w wordlist] [--csv rows] [--min-word-length min_len]
                  [--max-word-length min_len]
                  format_str N

Generate easy to remember, random passwords

positional arguments:
  format_str            Format string for generating passwords.
                        %a: Alpha character
                        %n: Number
                        %w: Lowercase word
                        %W: Titlecase word
                        %s: Special character
                        %%: Percent character
                        !-~: Any static ascii character
  N                     The number of passwords to generate

optional arguments:
  -h, --help            show this help message and exit
  -w wordlist           Wordlist to get words from
  --csv rows            Output in CSV format with 'rows' passwords per column
  --min-word-length min_len
                        Minimum length of words to use
  --max-word-length min_len
                        Maximum length of words to use
