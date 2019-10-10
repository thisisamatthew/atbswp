import shutil, os, re

dateRx = re.compile(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3?\d))
((19|20)\d\d)
(.*?)$
""", re.VERBOSE)

# TODO: Loop over the files in the working directory.

for amerFilename in os.listdir('.')
    mo = dateRx.search(amerFilename)
 
    if mo == none:
        continue

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absworkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename)

# TODO: Get the full, absolute file paths.



# TODO: Rename the files.


