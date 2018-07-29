# Replace a substring

from tkinter import *
from tkinter.font import Font
import re

main = Tk()
main.title("Replace Stuff 1.0")
main.geometry("500x300")
main.configure(background = "light blue")

titleFont = Font(family="Verdana", size=16)
lableFont = Font(family="Verdana", size=10)


#Subrutinas

def replace ():
    
    # entradas de etiquetas
    inputf = entryBoxInputFile.get()
    outputf = entryBoxOutputFile.get()
    reg = entryBoxReg.get()
    change = entryBoxChange.get()
    subst = entryBoxSubst.get()

    input_file = open(inputf, "r")
    output_file = open(outputf, "w")

    lookfor = re.compile(reg) # string pattern we are looking for. If you want the level separator / you need to include it, because .* won't match it.
    replacewith = subst #substring replacement

    for line in input_file:
        match = re.search(lookfor, line) # we put en-us html finds in a variable
        if match:
            replaced = re.sub(change, replacewith, line) # make ths substitution on found matches
            output_file.write(replaced) # write line with the replacement
        else:
            output_file.write(line) # write any other no matching lines

def browseInput():
   pass


def browseOutput():
   pass

#Frames/labels

titleLabel = Label(main, text="Replace Stuff 1.0", font=titleFont, background = "light blue" )
titleLabel.grid(padx=10, pady= 5, row=0, column=0, sticky=W)

inputFileLabel =  Label(main, text="Input file path:", font=lableFont, background = "light blue" )
inputFileLabel.grid(padx=10, row=3, column=0, sticky=W)

outputFileLabel =  Label(main, text="Output file path:", font=lableFont, background = "light blue" )
outputFileLabel.grid(padx=10, row=4, column=0, sticky=W)

regLabel =  Label(main, text="Regex:", font=lableFont, background = "light blue" )
regLabel.grid(padx=10, row=5, column=0, sticky=W)

changeLabel =  Label(main, text="Substring to change:", font=lableFont, background = "light blue" )
changeLabel.grid(padx=10, row=6, column=0, sticky=W)

substLabel =  Label(main, text="Replace with:", font=lableFont, background = "light blue" )
substLabel.grid(padx=10, row=7, column=0, sticky=W)

#Entry boxes

entryBoxInputFile = Entry(main, width=30, bg="light grey")
entryBoxInputFile.grid(row=3, column=10, sticky=W)

entryBoxOutputFile =  Entry(main, width=30, bg="light grey")
entryBoxOutputFile.grid(row=4, column=10, sticky=W)

entryBoxReg = Entry(main, width=30, bg="light grey")
entryBoxReg.grid(row=5, column=10, sticky=W)

entryBoxChange = Entry(main, width=30, bg="light grey") # In case we want to give opportunity to enter something other than 'en-us'
entryBoxChange.grid(row=6, column=10, sticky=W)

entryBoxSubst = Entry(main, width=30, bg="light grey")
entryBoxSubst.grid(row=7, column=10, sticky=W)


#Importing buttons

ReplaceButton = Button(main, text="Replace", width=15, command = replace)
ReplaceButton.grid(pady=10, row=40, column=10, sticky=W)

BrowseButtonInput = Button(main, text="Browse", width=10, command = browseInput)
BrowseButtonInput.grid(padx=4,row=3, column=70, sticky=W)

BrowseButtonOutput = Button(main, text="Browse", width=10, command = browseOutput)
BrowseButtonOutput.grid(padx=4,row=4, column=70, sticky=W)
# ==============================

main.mainloop()


