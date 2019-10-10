import os, re

madLibsFile = open('C:\\Users\\mcolwell\\Documents\\Personal\\Github\\atbswp\\madlibsmaster.txt')
content = madLibsFile.read()
wordList = content.split()

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

