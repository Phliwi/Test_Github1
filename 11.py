import os
import sys
import fileinput

# первое слово
fileToSearch = open('11.txt')
textToSearch1 = "Плательщик="
textToReplace1 = "Плательщик=ИНН"


for line in fileinput.input(fileToSearch):
    if textToSearch1 in line:
        fileToSearch.write(line.replace(textToSearch1, textToReplace1))
    else:
        print('Match Not Found!!')
    fileToSearch.write(line.replace(textToSearch1, 'Не смог найти поставил это'))
fileToSearch.close()

input('\n\n Press Enter to exit...')
