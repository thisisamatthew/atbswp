import os, re

madLibsFile = open('C:\\Users\\silenus\\Documents\\Github\\atbswp\\madlibsmaster.txt')
content = madLibsFile.read() # the file is now a string
# wordList = content.split()
wordListRx = re.findall(r'(\w+)(\s|[?.!](\s?))', content)
builderList = []
# this messes up the list value if it has punctuation in it.
# I need to figure out how to separate the punctuation in the split
for i in range(len(wordListRx)):
        rules = ['ADJECTIVE' in wordListRx[i],
                 'NOUN' in wordListRx[i],
                 'VERB' in wordListRx[i],
                 'ADVERB' in wordListRx[i]]
    
        if any(rules):
            partOfSpeechTupleToList = [''.join(i) for i in wordListRx[i]]
            userResponse = input(f"Enter an {partOfSpeechTupleToList[0].lower()}: ")
            tupleToList = [''.join(i) for i in wordListRx[i]]
            builderList += userResponse
            builderList += tupleToList[1]
        else:
            builderList += [''.join(i) for i in wordListRx[i]]




# tupleToList = [''.join(i) for i in finalString]

finalString = ''.join(builderList)
print(finalString)

