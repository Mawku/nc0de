import tkinter as tk
from tkinter import ttk
import webbrowser
import random
import pyperclip

def copyfunction(event):
    rand = random.randint(0, 333333)
    copytext = pyperclip.copy(rand)

def linkfunction(event):
    rand = random.randint(0, 333333)
    link = "https://nhentai.net/g/" + str(rand)
    webbrowser.open_new_tab(link)

def simplemode(event):
    simple = tk.Tk()
    simple.title("nc0de")
    simple.geometry("300x300")

    open_link = tk.Button(simple, text = "Open in a new tab")
    open_link.pack()
    open_link.bind("<Button-1>",linkfunction)

    copy = tk.Button(simple, text = "Copy to clipboard")
    copy.pack()
    copy.bind("<Button-1>",copyfunction)

def filemode(event):
    file = tk.Tk()
    file.title("nc0de")
    file.geometry("300x300")

    label = tk.Label(file, text="Never gonna give you up...")
    label.pack()

root = tk.Tk()
root.title("nc0de")
root.geometry("300x300")

label = tk.Label(root, text="Select mode")
label.pack()

simplemodebutton = tk.Button(root, text = "Simple Mode")
simplemodebutton.pack()
simplemodebutton.bind("<Button-1>",simplemode)

filemodebutton = tk.Button(root, text = "File Mode")
filemodebutton.pack()
filemodebutton.bind("<Button-1>",filemode)

root.mainloop()
