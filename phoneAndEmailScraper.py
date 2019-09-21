import re, pyperclip

phoneRx = re.compile(r'''(
(\d{3}-)|(\(\d{3}\))?          # area code
(\s|-|\.)                      # seperator
\d{3}                          # first three digits
(\s|-|\.)                      # seperator
\d{4}                          # second four digits
(\s*(ext|x|ext.)\s*\d{2,5})?   # extension
)''', re.VERBOSE)

emailRx = re.compile(r'''(
[a-zA-Z0-9._%+-]+              # username
@                              # @ symbol
[a-zA-Z0-9.-]+                 # domain name
(\.[a-zA-Z]{2-4})              # dot-something
)''', re.VERBOSE)

# TODO: Find Matches in clilpboard text

# TODO: Copy Results to clipboard
