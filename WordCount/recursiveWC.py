# Maria C. Laguardia
# Recursive wordcounts (method 1)
# Returns total words after counting recursively in a folder of markdown files. 

import os

# Enter root directory below and uncomment:
# rootDir = 'C:\\blabla\\rebla\\recontrablabla\\md'
num_words = 0

for dirName, subdirList, fileList in os.walk(rootDir):
   print('Found directory: %s' % dirName)
   for fname in fileList:
       fullpath = os.path.join(dirName, fname)
       with open(fullpath, 'r') as f:
           for line in f:
               words = line.split()
               num_words += len(words)

print("Total words:")
print(num_words)

