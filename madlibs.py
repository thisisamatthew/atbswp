import os, re

madLibsFile = open('C:\\Users\\mcolwell\\Documents\\Personal\\Github\\atbswp\\madlibsmaster.txt')
content = madLibsFile.read() # the file is now a string
wordList = content.split()

# this messes up the list value if it has punctuation in it.
# I need to figure out how to separate the punctuation in the split
for i in range(len(wordList)):
    rules = ['ADJECTIVE' in wordList[i],
             'NOUN' in wordList[i],
             'VERB' in wordList[i],
             'ADVERB' in wordList[i]]
    
    if any(rules):
        print(f"Enter an {wordList[i].lower()}.")
        userResponse = input()
        wordList[i] = userResponse

finalSentence = ' '.join(wordList)
print(finalSentence)

