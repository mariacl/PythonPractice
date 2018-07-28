
# coding: utf-8

# In[1]:


import re


# In[2]:


url = "en-us/.*html"


# In[6]:


if re.search(url, "esto es una url como la que queremos encontrar: /en-us/unaCarpeta/unapaginaweb.html"): print ("Found pattern")


# In[11]:


if re.search(url, "esto es una url de una imagen, que no coincide con el patrón regex: /en-us/tralala/blabla/imagen.png"):
    print ("Found pattern")
else:
    print ("Not found")
        


# In[15]:


inputgood = "/en-us/blablabla.html"
inputbad = "/en-us/dontfindme.jpg"

resultgood = re.sub('en-us',  'de-de', inputgood)
print (resultgood)
resultbad = re.sub('en-us',  'de-de', inputbad)
print (resultbad)


# In[24]:


with open('sample.txt') as thefile:
    for line in thefile:
        if re.search('en-us/.*html', line):
            matchSub = re.sub('en-us', 'de-de', str(match))
            print (matchSub)


# In[22]:


# this works but output file has to exist first, otherwise it just creates the empty file. Second run, it gets populated
input_file = open("sample.txt", "r")
output_file = open("output3.txt", "w")
for line in input_file:
    match = re.search('en-us/.*html', line) # en-us html strings
    if match:
        replaced = re.sub('en-us','de-de', line)
        output_file.write(replaced)
    else:
        output_file.write(line)
    


# In[33]:


# this works - we put the regex in a variable with re.compile to and the replacement substring in a strign variable
import re
input_file = open("sample.txt", "r")
output_file = open("output15.txt", "w")

lookfor = re.compile('en-us/.*html') # string pattern we are looking for. If you want the level separator / you need to include it, because .* won't match it.
replacewith = 'fr-fr' #substring replacement

for line in input_file:
    match = re.search(lookfor, line) # we put en-us html finds in a variable
    if match:
        replaced = re.sub('en-us', replacewith, line) # make ths substitution on found matches
        output_file.write(replaced) # write line with the replacement
    else:
        output_file.write(line) # write any other no matching lines


# In[32]:


# Next: create a def function and a UI to enter input and output files,and enter regex and replacement strings

import re

def replace (inputf, outputf, reg, subst):
    
    input_file = open(inputf, "r")
    output_file = open(outputf, "w")

    lookfor = re.compile(reg) # string pattern we are looking for. If you want the level separator / you need to include it, because .* won't match it.
    replacewith = subst #substring replacement

    for line in input_file:
        match = re.search(lookfor, line) # we put en-us html finds in a variable
        if match:
            replaced = re.sub('en-us', replacewith, line) # make ths substitution on found matches
            output_file.write(replaced) # write line with the replacement
        else:
            output_file.write(line) # write any other no matching lines

