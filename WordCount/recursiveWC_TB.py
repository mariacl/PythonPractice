# Maria C. Laguardia
# Recursive wordcounts (method 2)
# Returns total words after counting recursively in a folder of markdown files. Uses TextBlob package.
# Wordcounting from .md files with TextBlob leaves out standalone markdown formatting (like hashes), whereas VSC and Ms Word count them as words, so worcounts may differ in these tools.


def countWords(arootdir):


    import os
    from textblob import TextBlob

    rootDir=arootdir
    
    totalwords = 0
    for root, dirs, files in  os.walk(rootDir):
    
        for fileid in files:
        
            if fileid.endswith('.md'):
             
                 fullpath = os.path.join(root, fileid)
                 with open(fullpath, 'r', encoding='utf-8') as f:
                    miblob = TextBlob(f.read())
                    totalwords = totalwords + len(miblob.words)
                    print(fullpath + ":" + str(len(miblob.words)))

    print("Total words in this doc set:" + str(totalwords))
   

