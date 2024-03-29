import re

filePath = input("Please provide a file path to a text file: ")
madLibsFile = open(filePath)
content = madLibsFile.read()

wordListRx = re.findall(r'(\w+)(\s|[?.!](\s?))', content)
builderList = []

for i in range(len(wordListRx)):
    rules = ['ADJECTIVE' in wordListRx[i],
             'NOUN' in wordListRx[i],
             'VERB' in wordListRx[i],
             'ADVERB' in wordListRx[i]]
    
    if any(rules):
        partOfSpeechTupleToList = [''.join(i) for i in wordListRx[i]]
        userResponse = input(f"Enter an {partOfSpeechTupleToList[0].lower()}: ")
        tupleToList = [''.join(i) for i in wordListRx[i]]
        builderList.extend([userResponse, tupleToList[1]])
    else:
        builderList += [''.join(i) for i in wordListRx[i]]

finalString = ''.join(builderList)
print(finalString)

