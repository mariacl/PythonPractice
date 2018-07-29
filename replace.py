# Replace a substring

from tkinter import *
import re

main = Tk()
main.title("Replace Stuff 1.0")
main.geometry("400x400")



#Subrutinas


def replace ():
    
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



#Frames/labels
Label(main, text="Replace en-us 1.0", font=16).grid(row=0, column=0, sticky=W)


#EntryBox

entryBoxInputFile = Entry(main, width=20, bg="light grey")
entryBoxInputFile.grid(row=3, column=0, sticky=W)

entryBoxOutputFile =  Entry(main, width=20, bg="light grey")
entryBoxOutputFile.grid(row=4, column=0, sticky=W)

entryBoxReg = Entry(main, width=20, bg="light grey")
entryBoxReg.grid(row=5, column=0, sticky=W)

entryBoxChange = Entry(main, width=20, bg="light grey") # In case we want to give opportunity to enter something other than 'en-us'
entryBoxChange.grid(row=6, column=0, sticky=W)

entryBoxSubst = Entry(main, width=20, bg="light grey")
entryBoxSubst.grid(row=7, column=0, sticky=W)





#Importing buttons

ReplaceButton = Button(main, text="Replace", width=30, command = replace)
ReplaceButton.grid(row=7, column=10, sticky=W)

main.mainloop()
# ==============================

