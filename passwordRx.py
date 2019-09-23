import re

passwordStrengthRx = re.compile(r'''^
(?=.*[a-z])        # find any lowercase
(?=.*[A-Z])        # find any uppercase
(?=.*\d)           # find any digit
[a-zA-Z\d]{8,}     # find at least 8 characters, can be alpha(u&l) or num
$''', re.VERBOSE)

pw = passwordStrengthRx.findall('asdf2asfD')
print(pw)
