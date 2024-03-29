#! python3

# py.exe mcb.pyw save <keyword> - saves clipboard to keyword
# py.exe mcb.pyw <keyword> - loads keyword to clipboard
# py.exe mcb.pyw list - loads all keywords to clipboard

# EXPLAINER FOR MYSELF
# with sys.argv, the filename (mcb.pyw) is argv[0], so sys.argv == 3
# because we have the filename, save, and the keywoard,
# which are [0], [1], and [2], which are 3 total arguments.

# the other two usage situation -- <keyword> and list --
# fall under sys.argv == 2, because we only have two arguments:
# the filename and <keyword> or list. filename is always [0]
# and then <keyword> or list are at [1], which is a total of
# two arguments

import shelve, pyperclip, sys, time
time.sleep(5)
mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
