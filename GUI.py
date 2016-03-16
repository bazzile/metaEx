# -*- coding: utf-8 -*-
from Tkinter import *
import tkFileDialog
import tkMessageBox
import scanner


def ask_directory():
    directory = tkFileDialog.askdirectory()
    scanner.scanner(directory)
    tkMessageBox.showinfo("Информация", "Сканирование завершено!")
    root.quit()


def terminate():
    global root
    root.quit()

root = Tk()
root.title('Каталогизатор v.0.1')
root.resizable(width=FALSE, height=FALSE)
frame = Frame(root, width=300, height=70)
title = Label(root, text='Укажите корневую директорию', font="Arial 10 bold").pack(padx=10, pady=20)
button_go = Button(root, text='Директория...', command=ask_directory, fg='darkgreen').place(relx=0.5, rely=0.5, anchor=CENTER)
button_exit = Button(root, text='Выход', command=terminate, fg='red').place(relx=0.5, rely=0.75, anchor=CENTER)
frame.pack()


# Code to add widgets will go here...
root.mainloop()
