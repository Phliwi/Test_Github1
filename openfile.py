from tkinter import *
from tkinter import filedialog as fd
import os
import sys
import fileinput

from search import file

textToSearch = "Плательщик="
textToReplace = "Плательщик=ИНН"


# открытие файла
def insert_text():
    file_name = fd.askopenfilename(filetypes=(("TXT files", "*.txt"),
                                              ("CSV files", "*.csv"),
                                              ("All files", "*.*")))
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()


def format_text():
    texts = file.filename
    f = open(texts, 'w')
    for line in fileinput.input(f):
        if textToSearch in line:
            f.write(line.replace(textToSearch, textToReplace))
        else:
            f.write(line.replace(textToSearch, 'Не смог найти поставил это'))


# сохранение файла
def extract_text():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("CSV files", "*.csv"),
                                                ("All files", "*.*")))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()


root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insert_text)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extract_text)
b2.grid(row=1, column=2, sticky=S)
b3 = Button(text="Форматировать", command=format_text)
b3.grid(row=1, column=3, sticky=N)

root.mainloop()
