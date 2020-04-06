from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd


# import csv


# клик в заголовке
# clicks = 0

# функция клика по кнокпке
# def click_button():
#    global clicks
#    clicks += 1
#    root.title("Clicks {}".format(clicks))


def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")


# root = Tk()
# root.title("Графическая программа на Python")
# root.geometry("400x300+300+250")

btn = Button(text="Click Me",  # текст кнопки
             background="#555",  # фоновый цвет кнопки
             foreground="#ccc",  # цвет текста
             padx="20",  # отступ от границ до содержимого по горизонтали
             pady="8",  # отступ от границ до содержимого по вертикали
             font="16",  # высота шрифта
             # command=click_button  команда клика
             )
btn.pack()

main_menu = Menu()
file_menu = Menu(font=("Verdana", 13, "bold"), tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", command=edit_click)
main_menu.add_cascade(label="View")


# конец меню

# начало выбора файла
def insert_text():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()


def extract_text():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("HTML files", "*.html;*.htm"),
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
b2.grid(row=1, column=1, sticky=W)
# конец выбора файла


root.config(menu=main_menu)
root.mainloop()
