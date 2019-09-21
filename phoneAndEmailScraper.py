import re, pyperclip

phoneRx = re.compile(r'''(
(\d{3}|\(\d{3}\))?          # area code
(\s|-|\.)?                      # seperator
(\d{3})                          # first three digits
(\s|-|\.)                      # seperator
(\d{4})                          # second four digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension
)''', re.VERBOSE)


emailRx = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# this will be what it's like when I actually use the clipboard
# text = str(pyperclip.paste())

text = '''
(281) 230-3100 x456
Hobby Airport
281-640-3000
jeteve@msn.com
scitext@yahoo.com'''

matches = []
for groups in phoneRx.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRx.findall(text):
       matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses were found')

print(matches)
        

# TODO: Copy Results to clipboard
